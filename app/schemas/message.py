from pydantic import BaseModel, Field
from datetime import datetime, timezone


class MessageSchema(BaseModel):
    sender_username: str = Field(..., description="Username of the sender")
    receiver_username: str = Field(..., description="Username of the receiver")
    content: str = Field(..., min_length=1, max_length=1000,
                         description="Message content")
    timestamp: float = Field(
        default_factory=lambda: datetime.now(timezone.utc).timestamp(), description="Post creation timestamp")

    class Config:
        from_attributes = True
