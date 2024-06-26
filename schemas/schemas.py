from pydantic import BaseModel
from typing import Optional

class CreateBookSchema(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

class UpdateBookSchema(BaseModel):
    title:Optional[str]
    author:Optional[str]
    year:Optional[int]
    isbn:Optional[str]




class BookOutSchema(BaseModel):
    id:int
    title: str
    author: str
    year: int
    isbn: str
    class Config:
        orm_mode=True
