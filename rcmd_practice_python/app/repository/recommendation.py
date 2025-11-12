from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import Content, User, RcmdUserContent
from app.dto.recommendation import RcmdCreate

class CRUDRecommendation:
    """
    추천 데이터 접근 계층
    - 추천 관련 모든 데이터베이스 작업 담당
    - 복잡한 조인 쿼리 및 추천 로직 처리
    """
    
    def get_user_recommendations(self, db: Session, user_id: int) -> List[Content]:
        """사용자별 추천 컨텐츠 조회"""
        return db.query(Content).join(
            RcmdUserContent, Content.content_id == RcmdUserContent.content_id
        ).filter(RcmdUserContent.user_id == user_id).all()
    
    def create_recommendation(self, db: Session, rcmd: RcmdCreate) -> RcmdUserContent:
        """새 추천 생성"""
        db_rcmd = RcmdUserContent(user_id=rcmd.user_id, content_id=rcmd.content_id)
        db.add(db_rcmd)
        db.commit()
        db.refresh(db_rcmd)
        return db_rcmd
    
    def get_recommendation(self, db: Session, user_id: int, content_id: int) -> Optional[RcmdUserContent]:
        """특정 사용자-컨텐츠 추천 조회"""
        return db.query(RcmdUserContent).filter(
            RcmdUserContent.user_id == user_id,
            RcmdUserContent.content_id == content_id
        ).first()
    
    def delete_recommendation(self, db: Session, user_id: int, content_id: int) -> bool:
        """추천 삭제"""
        rcmd = self.get_recommendation(db, user_id, content_id)
        if rcmd:
            db.delete(rcmd)
            db.commit()
            return True
        return False
    
    def get_user_recommendation_count(self, db: Session, user_id: int) -> int:
        """사용자별 추천 컨텐츠 수"""
        return db.query(RcmdUserContent).filter(RcmdUserContent.user_id == user_id).count()
    
    def get_content_recommendation_count(self, db: Session, content_id: int) -> int:
        """컨텐츠별 추천받은 사용자 수"""
        return db.query(RcmdUserContent).filter(RcmdUserContent.content_id == content_id).count()
    
    def get_popular_contents(self, db: Session, limit: int = 10) -> List[tuple]:
        """인기 컨텐츠 조회 (추천 수 기준)"""
        return db.query(
            Content.content_id,
            Content.type, 
            Content.title, 
            Content.year, 
            Content.genre,
            db.func.count(RcmdUserContent.user_id).label('recommendation_count')
        ).join(
            RcmdUserContent, Content.content_id == RcmdUserContent.content_id
        ).group_by(
            Content.content_id, Content.title, Content.year, Content.genre
        ).order_by(
            db.func.count(RcmdUserContent.user_id).desc()
        ).limit(limit).all()
    
    def get_users_without_recommendations(self, db: Session) -> List[User]:
        """추천이 없는 사용자들 조회"""
        return db.query(User).outerjoin(RcmdUserContent).filter(
            RcmdUserContent.user_id.is_(None)
        ).all()
    
    def bulk_delete_user_recommendations(self, db: Session, user_id: int) -> int:
        """사용자의 모든 추천 삭제"""
        deleted_count = db.query(RcmdUserContent).filter(
            RcmdUserContent.user_id == user_id
        ).delete()
        db.commit()
        return deleted_count

# 싱글톤 인스턴스 생성
recommendation = CRUDRecommendation()