from pydantic import BaseModel,EmailStr, constr
from date_stuff import create_customised_datetime
from typing import Optional



class User(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=6, max_length=30)
    created_at: Optional[str] = None
    

class CreateUser(User):
    pass

class UserOpt(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: str = create_customised_datetime()
