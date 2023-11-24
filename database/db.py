from db_session import SqlAlchemyBase
import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Column, String, DateTime, func


class Pallete(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "palletes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_color = Column(String)
    second_color = Column(String)
    third_color = Column(String)
    fourth_color = Column(String)
    unique_string: Mapped[str]
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    likes: Mapped[int]


