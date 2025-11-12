# FastAPI 실습 가이드 - 영화 추천 시스템

## 목차
1. [FastAPI 기본 개념](#1-fastapi-기본-개념)
2. [프로젝트 구조 이해](#2-프로젝트-구조-이해)
3. [계층형 아키텍처 이해](#3-계층형-아키텍처-이해)
4. [API 엔드포인트 작성법](#4-api-엔드포인트-작성법)
5. [HTTP 메서드별 구현](#5-http-메서드별-구현)
6. [데이터 검증과 스키마](#6-데이터-검증과-스키마)
7. [의존성 주입](#7-의존성-주입)
8. [Service 계층 활용](#8-service-계층-활용)
9. [에러 처리](#9-에러-처리)
10. [실습 과제](#10-실습-과제)

---

## 1. FastAPI 기본 개념

### FastAPI란?
- **Python 웹 프레임워크**로 REST API를 쉽게 만들 수 있음
- **자동 문서화** (Swagger UI) 제공
- **타입 힌트** 기반으로 데이터 검증 자동화
- **비동기 처리** 지원으로 높은 성능
- **Pydantic** 모델을 통한 강력한 데이터 검증

### 기본 구조
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

---

## 2. 프로젝트 구조 이해

```
rcmd_practice/                    # 영화 추천 시스템 프로젝트
├── app/
│   ├── controller/              # API 컨트롤러 계층 (HTTP 요청/응답 처리)
│   │   ├── admin.py             # 관리자 API (DB 초기화 등)
│   │   ├── contents.py          # 컨텐츠 관련 API ← 실습 영역
│   │   ├── users.py             # 사용자 관련 API
│   │   └── recommendations.py   # 추천 관련 API ← 실습 영역
│   ├── service/                 # 비즈니스 로직 계층
│   │   └── recommendation_service.py
│   ├── repository/              # 데이터 접근 계층
│   │   ├── base.py              # Repository 기본 클래스
│   │   ├── content.py           # 컨텐츠 Repository
│   │   ├── user.py              # 사용자 Repository
│   │   └── recommendation.py    # 추천 Repository
│   ├── models/                  # 데이터베이스 모델 (SQLAlchemy)
│   │   ├── content.py           # 컨텐츠 테이블 모델
│   │   ├── user.py              # 사용자 테이블 모델
│   │   └── recommendation.py    # 추천 테이블 모델
│   ├── dto/                     # API 입출력 스키마 (Pydantic)
│   │   ├── content.py           # 컨텐츠 DTO
│   │   ├── user.py              # 사용자 DTO
│   │   └── recommendation.py    # 추천 DTO
│   ├── core/                    # 핵심 설정
│   │   ├── config.py            # 환경 설정
│   │   ├── database.py          # DB 연결 및 세션 관리
│   │   └── sql_loader.py        # SQL 파일 로더
│   ├── utils/                   # 유틸리티 함수들
│   │   └── content_utils.py     # 컨텐츠 관련 유틸리티
│   ├── todo/                    # 실습용 TODO 파일들
│   │   ├── contents.py          # 컨텐츠 API 실습
│   │   ├── recommendations.py   # 추천 API 실습
│   │   └── recommendation_service.py # 서비스 계층 실습
│   └── main.py                  # FastAPI 애플리케이션 진입점
├── sql/                         # 데이터베이스 스크립트
├── .env                         # 환경변수 (DB 연결 정보)
├── requirements.txt             # Python 의존성
├── startup.py                   # 서버 시작 스크립트
└── README.md                    # 프로젝트 문서
```

---

## 3. 계층형 아키텍처 이해

### 데이터 흐름
```
Client → Controller → Service → Repository → Database
   ↑        ↓           ↓          ↓
  JSON     DTO       Domain     DAO/ORM
```

### 각 계층의 역할

#### 1. **Controller 계층** (`app/controller/`)
- **역할**: HTTP 요청/응답 처리, 라우팅
- **책임**: URL 매핑, 파라미터 검증, 응답 형식 지정
```python
@router.get("/", response_model=List[Content])
def get_recommendations(user_id: Optional[int] = Query(None)):
    return recommendation_service.get_recommendations(db, user_id)
```

#### 2. **Service 계층** (`app/service/`)
- **역할**: 비즈니스 로직 처리
- **책임**: 업무 규칙, 복잡한 로직, 여러 Repository 조합
```python
class RecommendationService:
    def get_recommendations(self, db: Session, user_id: Optional[int]):
        if user_id:
            return self._get_personalized_recommendations(db, user_id)
        else:
            return self._get_general_recommendations(db)
```

#### 3. **Repository 계층** (`app/repository/`)
- **역할**: 데이터베이스 접근 추상화
- **책임**: CRUD 작업, SQL 쿼리, 데이터 매핑
```python
def get_user_recommendations(db: Session, user_id: int):
    return db.query(Content).join(...).filter(...).all()
```

#### 4. **Model 계층** (`app/models/`)
- **역할**: 데이터베이스 테이블 정의
- **책임**: 테이블 구조, 관계 정의
```python
class Content(Base):
    __tablename__ = "contents"
    content_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
```

#### 5. **DTO 계층** (`app/dto/`)
- **역할**: API 입출력 데이터 검증
- **책임**: 데이터 직렬화/역직렬화, 검증 규칙
```python
class ContentResponse(BaseModel):
    content_id: int
    title: str
    type: str
    
    class Config:
        from_attributes = True  # ORM 객체 자동 변환
```

---

## 4. API 엔드포인트 작성법

### 기본 라우터 생성
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()

@router.get("/")
def get_items(db: Session = Depends(get_db)):
    return {"message": "Get all items"}
```

### 라우터 등록 (main.py)
```python
from app.controller import recommendations, contents, admin

# API v1 prefix 적용
API_PREFIX = "/api/v1"

app.include_router(
    recommendations.router, 
    prefix=f"{API_PREFIX}/recommendations", 
    tags=["recommendations"]
)
app.include_router(
    contents.router, 
    prefix=f"{API_PREFIX}/contents", 
    tags=["contents"]
)
app.include_router(
    admin.router, 
    prefix=f"{API_PREFIX}/admin", 
    tags=["admin"]
)
```

### URL 구조 (RESTful API)
```
# 관리자 API
POST /api/v1/admin/init-db              → 데이터베이스 초기화
GET /api/v1/admin/status                → DB 상태 확인

# 추천 관련
GET /api/v1/recommendations/            → 추천 목록 조회
POST /api/v1/recommendations/           → 추천 추가
DELETE /api/v1/recommendations/{user_id}/{content_id} → 추천 삭제
GET /api/v1/recommendations/stats?user_id=1 → 사용자 통계

# 컨텐츠 관련
POST /api/v1/contents/                  → 컨텐츠 생성
GET /api/v1/contents/                   → 컨텐츠 목록 조회
GET /api/v1/contents/{content_id}       → 특정 컨텐츠 조회
GET /api/v1/contents/search/title?title=검색어 → 제목 검색
GET /api/v1/contents/latest/top?limit=10 → 최신 컨텐츠
```

---

## 5. HTTP 메서드별 구현

### GET - 데이터 조회
```python
# 조건부 조회 (Query Parameter 활용)
@router.get("/", response_model=ContentTypeList)
def get_contents(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    genre: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """컨텐츠 목록 조회 (필터링 및 페이징)"""
    if genre:
        contents = content.get_by_genre(db, genre=genre, skip=skip, limit=limit)
    elif year:
        contents = content.get_by_year_range(db, start_year=year, end_year=year)
    else:
        contents = content.get_multi(db, skip=skip, limit=limit)
    
    return group_contents_by_type(contents)

# Path Parameter 활용
@router.get("/{content_id}", response_model=Content)
def get_content(content_id: int, db: Session = Depends(get_db)):
    db_content = content.get_by_id(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content
```

### POST - 데이터 생성
```python
@router.post("/", response_model=ContentCreated, status_code=status.HTTP_201_CREATED)
def create_content(
    content_data: ContentCreate,  # Request Body
    db: Session = Depends(get_db)
):
    """새 컨텐츠 생성"""
    try:
        return content.create(db, obj_in=content_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### DELETE - 데이터 삭제
```python
@router.delete("/{user_id}/{content_id}")
def delete_recommendation(
    user_id: int,      # Path Parameter
    content_id: int,   # Path Parameter
    db: Session = Depends(get_db)
):
    """추천 영화 삭제"""
    return recommendation_service.delete_recommendation(db, user_id, content_id)
```

---

## 6. 데이터 검증과 스키마

### Pydantic 스키마의 종류

#### 1. **Base 스키마** - 공통 필드
```python
class ContentBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    type: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1900, le=2030)
    genre: str = Field(min_length=1, max_length=100)
```

#### 2. **Create 스키마** - 생성 요청
```python
class ContentCreate(ContentBase):
    pass  # Base의 모든 필드가 필수
```

#### 3. **Response 스키마** - 응답 데이터
```python
class Content(ContentBase):
    content_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True  # SQLAlchemy 객체 자동 변환

class ContentCreated(BaseModel):
    """생성 응답용 (최소 정보만)"""
    content_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
```

#### 4. **camelCase/snake_case 호환**
```python
class RcmdCreate(BaseModel):
    user_id: int = Field(alias="userId", gt=0)
    content_id: int = Field(alias="contentId", gt=0)
    
    class Config:
        populate_by_name = True  # userId와 user_id 둘 다 허용
```

---

## 7. 의존성 주입

### Query Parameters
```python
# camelCase/snake_case 호환
user_id: Optional[int] = Query(None, alias="userId", description="사용자 ID")

# 필수 파라미터
title: str = Query(..., min_length=1, description="검색할 제목")

# 기본값이 있는 파라미터
skip: int = Query(0, ge=0, description="건너뛸 개수")
limit: int = Query(10, ge=1, le=100, description="조회 개수")
```

### Database 의존성
```python
from app.core.database import get_db

@router.get("/")
def get_data(db: Session = Depends(get_db)):
    # get_db() 함수가 자동으로 호출되어 DB 세션 주입
    # 요청 완료 후 자동으로 세션 종료
```

---

## 8. Service 계층 활용

### Service vs Repository vs Controller
```python
# ✅ 간단한 CRUD - Controller에서 직접 Repository 호출
@router.get("/{content_id}", response_model=Content)
def get_content(content_id: int, db: Session = Depends(get_db)):
    db_content = content_repository.get_by_id(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content

# ✅ 복잡한 비즈니스 로직 - Service 계층 활용
@router.get("/", response_model=List[Content])
def get_recommendations(user_id: Optional[int], db: Session = Depends(get_db)):
    return recommendation_service.get_recommendations(db, user_id)
```

---

## 9. 에러 처리

### HTTPException 사용
```python
from fastapi import HTTPException, status

# 404 - 리소스 없음
if not db_content:
    raise HTTPException(status_code=404, detail="Content not found")

# 409 - 중복/충돌
if existing_recommendation:
    raise HTTPException(status_code=409, detail="Already recommended")

# 400 - 잘못된 요청
if invalid_data:
    raise HTTPException(status_code=400, detail="Invalid input data")
```

---

## 10. 실습 과제

### 🎯 과제 1: 컨텐츠 생성 API 완성하기
**파일**: `app/todo/contents.py`의 `create_content` 함수

**구현해야 할 것**:
1. `content_repository.create(db, obj_in=content_data)` 호출
2. 생성된 컨텐츠를 return으로 반환
3. 예외 발생 시 `HTTPException(status_code=400, detail=str(e))` 발생

---

### 🎯 과제 2: 추천 조회 API 완성하기
**파일**: `app/todo/recommendations.py`의 `get_recommendations` 함수

**구현해야 할 것**:
1. `recommendation_service.get_recommendations(db, user_id)` 호출
2. 결과를 return으로 반환

---

### 🎯 과제 3: Service 계층 로직 완성하기
**파일**: `app/todo/recommendation_service.py`의 `_get_personalized_recommendations` 함수

**구현해야 할 것**:
1. **사용자 존재 확인**: `user_repository.get_by_id(db, user_id)`
2. **404 에러 발생**: `raise HTTPException(status_code=404, detail="User not found")`
3. **개인화 추천 조회**: `recommendation_repository.get_user_recommendations(db, user_id)`
4. **추천이 없으면**: `self._get_latest_contents(db, limit=10)` 반환

---

### 🧪 테스트 방법

1. **서버 실행**: 
   ```bash
   python startup.py
   # 또는
   uvicorn app.main:app --reload --port 8080
   ```

2. **데이터베이스 초기화**:
   ```bash
   curl -X POST http://localhost:8080/api/v1/admin/init-db
   ```

3. **API 문서 접속**: `http://localhost:8080/docs`

4. **테스트 시나리오**:
   ```
   1. POST /api/v1/admin/init-db (DB 초기화)
   2. POST /api/v1/contents (컨텐츠 생성)
   3. GET /api/v1/contents (컨텐츠 목록)
   4. GET /api/v1/recommendations (일반 추천)
   5. GET /api/v1/recommendations?userId=1 (개인화 추천)
   ```

---

### 🎯 실습 순서 (권장)

1. **컨텐츠 생성** - 가장 간단한 Repository 호출
2. **추천 조회** - Service 호출 학습
3. **Service 로직** - 비즈니스 로직 학습

### 💡 디버깅 팁

- **에러 발생 시**: 터미널의 에러 메시지 확인
- **데이터 확인**: `/docs`에서 GET API로 데이터 상태 확인
- **단계별 테스트**: 한 번에 하나씩 구현하고 테스트
- **Postman 호환**: camelCase/snake_case 모두 지원

### 🏗️ 아키텍처 학습 포인트

1. **계층 분리**: Controller → Service → Repository → DB
2. **단일 책임**: 각 계층이 명확한 역할
3. **의존성 방향**: 상위 계층이 하위 계층 호출
4. **재사용성**: Service와 Repository 로직 재사용
5. **API 버전 관리**: `/api/v1` prefix 사용
6. **관리 기능**: 별도 admin API로 분리
