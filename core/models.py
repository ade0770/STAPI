from pydantic import BaseModel
from typing import List, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Tasks(Base):
    """
    table Tasks in mydb
    """
    __tablename__='tasks'

    id = Column(Integer, primary_key=True, index=True)
    description=Column(String, index=True)


class BasicModel(BaseModel):
    """
    Base Class for regular model
    """

class Task(BasicModel):
    id: str
    description: str

