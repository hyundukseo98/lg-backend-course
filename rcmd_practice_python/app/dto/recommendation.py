from pydantic import BaseModel

class RcmdCreate(BaseModel):
    user_id: int
    content_id: int