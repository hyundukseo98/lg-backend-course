from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.repository import user
from app.dto.content import ContentTypeList
from app.dto.recommendation import RcmdCreate
from app.service.recommendation_service import recommendation_service

router = APIRouter()
    
@router.get("/", response_model=ContentTypeList)
def get_recommendations(
    user_id: Optional[int] = Query(None, gt=0, alias="userId", description="사용자 ID (1 이상)"),
    db: Session = Depends(get_db)
):
    """
    컨텐츠 추천 조회
    - user_id 있으면: 개인화 추천
    - user_id 없으면: 일반 추천 (최신 컨텐츠)
    """
    try:
        # 사용자 존재 확인
        if user_id and not user.get_by_id(db, user_id):
            raise HTTPException(status_code=404, detail="User not found")

        return recommendation_service.get_recommendations(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_recommendation(rcmd: RcmdCreate, db: Session = Depends(get_db)):
    """
    추천 컨텐츠 추가
    """
    try:
        return recommendation_service.add_recommendation(db, rcmd)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{user_id}/{content_id}")
def delete_recommendation(user_id: int, content_id: int, db: Session = Depends(get_db)):
    """
    추천 컨텐츠 삭제
    """
    try:
        return recommendation_service.delete_recommendation(db, user_id, content_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# 참고: 완성된 함수 예시 (학습 참고용)
# ============================================================================

@router.get("/stats")
def get_user_recommendation_stats(
    user_id: Optional[int] = Query(gt=0, description="사용자 ID (1 이상)"),
    db: Session = Depends(get_db)
):
    """
    사용자 추천 통계 조회
    """
    try:
        return recommendation_service.get_user_recommendation_stats(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))