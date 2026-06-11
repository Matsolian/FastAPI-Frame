from pydantic import BaseModel, ConfigDict
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column


from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str          
    foo: str
    bar: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

