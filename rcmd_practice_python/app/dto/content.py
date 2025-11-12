from pydantic import BaseModel
from datetime import datetime
from typing import List

class ContentBase(BaseModel):
    title: str
    type: str
    year: int
    genre: str

class ContentCreate(ContentBase):
    pass

class ContentCreated(BaseModel):
    content_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Content(ContentBase):
    content_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ContentsByType(BaseModel):
    type: str
    contents: List[Content]

class ContentTypeList(BaseModel):
    recommendations: List[ContentsByType]