import uuid
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class PostSchema(BaseModel):
    post_id: str = Field(default_factory=lambda: str(
        uuid.uuid4()), description="Auto-generated Unique ID of the post")
    user_name: str = Field(..., description="User who created the post")
    title: str = Field(..., min_length=1, max_length=50,
                       description="Title of the post")
    content: str = Field(..., min_length=1, max_length=500,
                         description="Text content of the post")
    hashtags: List[str] = Field(
        default=[], description="List of hashtags associated with the post")
    timestamp: float = Field(
        default_factory=lambda: datetime.now(timezone.utc).timestamp(), description="Post creation timestamp")

    class Config:
        from_attributes = True
