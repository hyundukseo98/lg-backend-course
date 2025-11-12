from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class Content(Base):
    __tablename__ = "contents"
    
    content_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)