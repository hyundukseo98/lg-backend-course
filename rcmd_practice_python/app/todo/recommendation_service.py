from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repository import content, user, recommendation
from app.dto.content import Content, ContentTypeList
from app.dto.recommendation import RcmdCreate
from app.utils.content_utils import group_contents_by_type


class RecommendationService:
    """추천 서비스 - 비즈니스 로직 처리"""
    
    def get_recommendations(self, db: Session, user_id: Optional[int] = None) -> ContentTypeList:
        """
        영화 추천 조회
        - user_id 있으면: 개인화 추천
        - user_id 없으면: 일반 추천 (최신 영화)
        """
        if user_id:
            contents = self._get_personalized_recommendations(db, user_id)
        else:
            contents = self._get_latest_contents(db)

        # List[Content]를 ContentTypeList로 변환
        return group_contents_by_type(contents)
    
    def _get_personalized_recommendations(self, db: Session, user_id: int) -> List[Content]:
        """개인화 추천 로직"""
        # TODO: 개인화 추천 컨텐츠 조회
        user_recommendations = None
    
        # TODO: 추천이 없으면 최신 컨텐츠 10개 반환
        
        # Content DTO로 변환
        return [Content.model_validate(content_obj) for content_obj in user_recommendations]
    
    def _get_latest_contents(self, db: Session, limit: int = 10) -> List[Content]:
        # TODO: 최신 컨텐츠 조회
        latest_contents = None

        return [Content.model_validate(content_obj) for content_obj in latest_contents]
    
    def add_recommendation(self, db: Session, rcmd: RcmdCreate) -> dict:
        """추천 영화 추가"""
        # 사용자 존재 확인
        db_user = user.get_by_id(db, rcmd.user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # 컨텐츠 존재 확인
        db_content = content.get_by_id(db, rcmd.content_id)
        if not db_content:
            raise HTTPException(status_code=404, detail="Content not found")
        
        # 중복 추천 확인
        existing = recommendation.get_recommendation(db, rcmd.user_id, rcmd.content_id)
        if existing:
            raise HTTPException(status_code=409, detail="Content already recommended to user")
        
        # 추천 생성
        recommendation.create_recommendation(db, rcmd)
        
        return {
            "message": "Recommendation added successfully",
            "user_id": rcmd.user_id,
            "content_id": rcmd.content_id,
            "title": db_content.title
        }
    
    def delete_recommendation(self, db: Session, user_id: int, content_id: int) -> dict:
        """추천 영화 삭제"""
        deleted = recommendation.delete_recommendation(db, user_id, content_id)
        
        if not deleted:
            raise HTTPException(status_code=404, detail="Recommendation not found")
        
        return {
            "message": "Recommendation deleted successfully",
            "user_id": user_id,
            "content_id": content_id
        }
    
    def get_user_recommendation_stats(self, db: Session, user_id: int) -> dict:
        """사용자 추천 통계 조회"""
        # 사용자 존재 확인
        db_user = user.get_by_id(db, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # 추천 수 조회
        recommendation_count = recommendation.get_user_recommendation_count(db, user_id)
        
        # 추천 컨텐츠 목록 조회
        user_recommendations = recommendation.get_user_recommendations(db, user_id)
        
        # 장르별 선호도 분석
        genre_preferences = self._analyze_genre_preferences(user_recommendations)
        
        return {
            "user_id": user_id,
            "user_name": db_user.name,
            "total_recommendations": recommendation_count,
            "genre_preferences": genre_preferences,
            "favorite_genre": max(genre_preferences.items(), key=lambda x: x[1])[0] if genre_preferences else None
        }
    
    def _analyze_genre_preferences(self, user_recommendations: List) -> dict:
        """장르별 선호도 분석"""
        genre_preferences = {}
        for content_obj in user_recommendations:
            genre = content_obj.genre or "Unknown"
            genre_preferences[genre] = genre_preferences.get(genre, 0) + 1
        return genre_preferences


# 서비스 인스턴스 생성
recommendation_service = RecommendationService()