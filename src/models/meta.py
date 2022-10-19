from typing import List
from pydantic import BaseModel


class File(BaseModel):
    name: str
    type: str
    time: int


class MetaData(BaseModel):
    data: List[File]
