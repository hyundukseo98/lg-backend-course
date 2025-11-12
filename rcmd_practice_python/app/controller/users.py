from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.repository import user
from app.dto.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    사용자 ID로 조회
    CRUD 계층을 통한 단일 데이터 조회 예시
    """
    db_user = user.get_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[UserResponse])
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    사용자 목록 조회 (페이징)
    CRUD 계층의 페이징 기능 활용 예시
    """
    try:
        # CRUD 계층의 페이징 메서드 활용
        return user.get_all_users(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    새 사용자 생성
    CRUD 계층을 통한 데이터 생성 및 중복 확인 예시
    """
    try:
        # 중복 확인 (CRUD 계층 활용)
        existing_user = user.get_by_name(db, user_data.name)
        if existing_user:
            raise HTTPException(status_code=409, detail="User with this name already exists")
        
        # 사용자 생성 (CRUD 계층 활용)
        db_user = user.create(db, obj_in=user_data)
        return {
            "user_id": db_user.user_id,
            "name": db_user.name,
            "message": "User created successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/search/name", response_model=List[UserResponse])
def search_users_by_name(
    name: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    """
    사용자 이름 검색
    CRUD 계층의 검색 기능 활용 예시
    """
    try:
        # CRUD 계층의 검색 메서드 활용
        users = user.search_users(db, name_keyword=name)
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
