from pydantic import BaseModel
from typing import List, Optional
from datetime import date

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import text, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.database import Base, int_pk


class Task(Base):
    id = Mapped[int_pk]
    description=Mapped[str]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id})")

    def __repr__(self):
        return str(self)


# class BasicModel(BaseModel):
#     """
#     Base Class for regular model
#     """
#
# class Task(BasicModel):
#     id: str
#     description: str

