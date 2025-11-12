from sqlalchemy.orm import Session
from typing import List, Optional
from app.repository.base import CRUDBase
from app.models.content import Content

class CRUDContent(CRUDBase):
    """
    컨텐츠 데이터 접근 계층
    - 컨텐츠 관련 모든 데이터베이스 작업 담당
    - 비즈니스 로직과 데이터 접근 로직 분리
    """
    def __init__(self):
        super().__init__(Content)

    def get_by_id(self, db: Session, content_id: int) -> Optional[Content]:
        """ID로 컨텐츠 조회"""
        return db.query(Content).filter(Content.content_id == content_id).first()
    
    def get_latest_contents(self, db: Session, limit: int = 10) -> List[Content]:
        """최신 컨텐츠 조회 (추천 시스템에서 사용)"""
        return db.query(Content).order_by(Content.created_at.desc()).limit(limit).all()

    def get_by_type(self, db: Session, type: str) -> Optional[Content]:
        """컨텐츠 타입으로 조회"""
        return db.query(Content).filter(Content.type == type).first()
    
    def get_by_title(self, db: Session, title: str) -> Optional[Content]:
        """컨텐츠 제목으로 조회"""
        return db.query(Content).filter(Content.title == title).first()
    
    def get_by_genre(self, db: Session, genre: str, skip: int = 0, limit: int = 10) -> List[Content]:
        """장르별 컨텐츠 조회"""
        return db.query(Content).filter(Content.genre == genre).offset(skip).limit(limit).all()
    
    def get_by_year_range(self, db: Session, start_year: int, end_year: int) -> List[Content]:
        """연도 범위로 컨텐츠 조회"""
        return db.query(Content).filter(
            Content.year >= start_year,
            Content.year <= end_year
        ).all()
    
    def search_by_title(self, db: Session, title_keyword: str) -> List[Content]:
        """제목으로 컨텐츠 검색"""
        return db.query(Content).filter(Content.title.contains(title_keyword)).all()

# 싱글톤 인스턴스 생성
content = CRUDContent()