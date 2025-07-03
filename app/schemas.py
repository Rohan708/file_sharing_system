from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str

class LoginSchema(BaseModel):
    username: str
