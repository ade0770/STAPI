from pydantic import BaseModel
from typing import List, Optional

class BasicModel(BaseModel):
    """
    Base Class for regular model
    """

class Task(BasicModel):
    id: str
    description: str

