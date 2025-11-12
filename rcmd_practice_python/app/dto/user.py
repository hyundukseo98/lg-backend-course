from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True