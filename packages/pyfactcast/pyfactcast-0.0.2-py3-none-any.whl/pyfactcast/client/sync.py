import logging
import grpc
from types import TracebackType
from typing import Iterable, List, Optional, Type
from json import dumps

from pyfactcast.grpc.generated.FactStore_pb2_grpc import RemoteFactStoreStub
from pyfactcast.grpc.generated.FactStore_pb2 import (
    MSG_Empty,
    MSG_String,
    MSG_SubscriptionRequest,
    MSG_Notification,
)

from pyfactcast.client.auth.basic import BasicAuth
from pyfactcast.client.config import (
    ClientConfiguration,
    get_client_configuration,
    log_level,
)
from pyfactcast.client.entities import Fact

log = logging.getLogger()
log.setLevel(log_level)


def get_synchronous_grpc_client(
    client_configuration: Optional[ClientConfiguration] = None,
) -> RemoteFactStoreStub:

    if not client_configuration:
        client_configuration = get_client_configuration()

    options = None
    if client_configuration.ssl_target_override:
        options = (
            (
                "grpc.ssl_target_name_override",
                client_configuration.ssl_target_override,
            ),
        )

    root_cert = None
    if client_configuration.root_cert_path:
        with open(client_configuration.root_cert_path) as f:
            root_cert = f.read().encode("UTF-8")

    channel_credentials = grpc.ssl_channel_credentials(root_certificates=root_cert)

    call_credentials = _construct_call_credentials(client_configuration)

    if call_credentials:
        grpc_credentials = grpc.composite_channel_credentials(
            channel_credentials, call_credentials
        )
    else:
        grpc_credentials = channel_credentials

    channel = grpc.secure_channel(
        target=client_configuration.server,
        credentials=grpc_credentials,
        options=options,
    )

    return RemoteFactStoreStub(channel)


def _construct_call_credentials(
    client_configuration: ClientConfiguration,
) -> Optional[grpc.CallCredentials]:

    if (
        client_configuration.credentials
    ):  # This would be perfect for walrus but flake and mypy can  not handle that atm
        call_credentials = grpc.metadata_call_credentials(
            BasicAuth(
                client_configuration.credentials.username,
                client_configuration.credentials.password,
            )
        )
        return call_credentials
    return None


def _fact_filter(msg: MSG_Notification) -> bool:
    if msg.type == msg.Fact:
        return True
    elif msg.type == msg.Catchup:
        log.info("Caught up!")
    else:
        log.debug(f"Received Notification of type: {msg.type}")
    return False


class FactStore:
    def __init__(self, client: Optional[RemoteFactStoreStub] = None) -> None:
        self._client = client

    def __enter__(self) -> "FactStore":
        if not self._client:
            self.client = get_synchronous_grpc_client()
        else:
            self.client = self._client
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        # TODO: Implement proper channel termination
        pass

    def enumerate_namespaces(self) -> List[str]:
        res: List[str] = self.client.enumerateNamespaces(MSG_Empty()).embeddedString

        return res

    def enumerate_types(self, namespace: str) -> List[str]:
        message = MSG_String()
        message.embeddedString = namespace
        res: List[str] = self.client.enumerateTypes(message).embeddedString

        return res

    def subscribe(self, *, namespace: str, continuous: bool = False) -> Iterable[Fact]:
        msg = MSG_SubscriptionRequest(
            json=dumps({"specs": [{"ns": namespace}], "continuous": continuous})
        )
        res = self.client.subscribe(msg)

        return map(Fact.from_msg, filter(_fact_filter, res))
