from typing import TYPE_CHECKING, Union, Callable, ClassVar
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as SA_UUID
from sqlmodel import Relationship, Field, Column, ForeignKey
from .base import SQLModelBase, PydanticModelBase

# if TYPE_CHECKING:
#     from .account import Account

class Domain(SQLModelBase, table=True):
    __tablename__: ClassVar[Union[str, Callable[..., str]]] = "domains"

    name: str = Field()


class DomainCreate(PydanticModelBase):
    name: str
    # account_id: UUID
