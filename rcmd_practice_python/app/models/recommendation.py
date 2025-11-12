from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class RcmdUserContent(Base):
    __tablename__ = "rcmd_user_content"
    
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    content_id = Column(Integer, ForeignKey("contents.content_id"), primary_key=True)