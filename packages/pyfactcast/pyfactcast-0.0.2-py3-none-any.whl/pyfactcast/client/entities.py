from typing import Type, TypeVar
from pyfactcast.grpc.generated.FactStore_pb2 import MSG_Notification
from pydantic import BaseModel, Json

F = TypeVar("F", bound="Fact")


class CatchUp:
    pass


class Fact(BaseModel):
    header: Json
    payload: Json

    @classmethod
    def from_msg(cls: Type[F], msg: MSG_Notification) -> F:
        return cls(header=msg.fact.header, payload=msg.fact.payload)
