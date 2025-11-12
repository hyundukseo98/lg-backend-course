from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.repository import content
from app.dto.content import ContentCreate, ContentCreated, Content, ContentTypeList
from app.utils.content_utils import group_contents_by_type

router = APIRouter()

@router.post("/", response_model=ContentCreated, status_code=status.HTTP_201_CREATED)
def create_content(content_data: ContentCreate, db: Session = Depends(get_db)):
    """
    새 컨텐츠 생성
    CRUD 계층을 통한 데이터 생성 예시
    """
    try:
        # CRUD 계층 활용
        return content.create(db, obj_in=content_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{content_id}", response_model=Content)
def get_content(content_id: int, db: Session = Depends(get_db)):
    """
    컨텐츠 ID로 조회 (Path Parameter 예시)
    """
    db_content = content.get_by_id(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content

@router.get("/", response_model=ContentTypeList)
def get_contents(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    genre: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """
    컨텐츠 목록 조회 (필터링 및 페이징)
    """
    try:
        if genre:
            # 장르별 조회
            contents = content.get_by_genre(db, genre=genre, skip=skip, limit=limit)
        elif year:
            # 연도별 조회
            contents = content.get_by_year_range(db, start_year=year, end_year=year)
        else:
            # 전체 조회
            contents =  content.get_multi(db, skip=skip, limit=limit)
        
        return group_contents_by_type(contents)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/search/title", response_model=ContentTypeList)
def search_contents_by_title(
    title: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    """
    컨텐츠 제목 검색
    """
    try:
        contents = content.search_by_title(db, title_keyword=title)
        if not contents:
            raise HTTPException(status_code=404, detail="No contents found")
        return group_contents_by_type(contents)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/latest/top", response_model=ContentTypeList)
def get_latest_contents(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    """
    최신 컨텐츠 조회
    """
    try:
        contents = content.get_latest_contents(db, limit=limit)
        return group_contents_by_type(contents)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))