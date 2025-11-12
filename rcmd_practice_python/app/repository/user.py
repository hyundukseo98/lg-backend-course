from sqlalchemy.orm import Session
from typing import List, Optional
from app.repository.base import CRUDBase
from app.models.user import User

class CRUDUser(CRUDBase):
    """
    사용자 데이터 접근 계층
    - 사용자 관련 모든 데이터베이스 작업 담당
    - 사용자 검증 및 조회 로직 제공
    """
    def __init__(self):
        super().__init__(User)

    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        """사용자 ID로 조회"""
        return db.query(User).filter(User.user_id == user_id).first()
    
    def get_by_name(self, db: Session, name: str) -> Optional[User]:
        """사용자 이름으로 조회"""
        return db.query(User).filter(User.name == name).first()
    
    def get_all_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """모든 사용자 조회 (페이징)"""
        return db.query(User).offset(skip).limit(limit).all()
    
    def search_users(self, db: Session, name_keyword: str) -> List[User]:
        """이름으로 사용자 검색"""
        return db.query(User).filter(User.name.contains(name_keyword)).all()
    
    def exists(self, db: Session, user_id: int) -> bool:
        """사용자 존재 여부 확인"""
        return db.query(User).filter(User.user_id == user_id).first() is not None

# 싱글톤 인스턴스 생성
user = CRUDUser()