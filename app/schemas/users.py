import uuid
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class UserSchema(BaseModel):
    name: str = Field(..., description="Name of the User")
    user_name: str = Field(..., description="UserName")
    email: str = Field(..., description="Email of the User")
    age: int = Field(..., description="Age of the User")
    timestamp: float = Field(
        default_factory=lambda: datetime.now(timezone.utc).timestamp(), description="Post creation timestamp")

    class Config:
        from_attributes = True
