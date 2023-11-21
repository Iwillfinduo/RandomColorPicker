from db_session import SqlAlchemyBase

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Column, String


class Pallete(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "palletes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_color = Column(String)
    second_color = Column(String)
    third_color = Column(String)
    fourth_color = Column(String)
    unique_string: Mapped[str]
    likes: Mapped[int]


