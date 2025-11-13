from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.dto.content import ContentTypeList
from app.dto.recommendation import RcmdCreate
from app.repository import user
from app.todo.recommendation_service import recommendation_service

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
        # TODO: 사용자가 존재하는지 확인하고 없다면 404 에러를 던집니다

        # TODO: Service 계층을 호출하여 추천 결과를 반환하세요

        pass  # 이 줄을 삭제하고 Service 호출 코드를 작성하세요
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