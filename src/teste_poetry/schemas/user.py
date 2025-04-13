from pydantic import BaseModel, EmailStr

class User (BaseModel):
    name: str
    age: int
    email: EmailStr
    password: str


class UserPublic (BaseModel):
    name: str
    age: int
    email: EmailStr



class UserPublicDB (BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

class UserDB (User):
    id: int

class UserList (BaseModel):
    users: list[UserPublicDB]