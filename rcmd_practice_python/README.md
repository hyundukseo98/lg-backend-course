# Movie Recommendation API

FastAPI 기반 영화 추천 시스템 백엔드 (계층형 아키텍처 적용)

## 프로젝트 구조

```
rcmd_practice/                    # 영화 추천 시스템 프로젝트
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI 애플리케이션 진입점
│   ├── controller/              # API 컨트롤러 계층 (HTTP 요청/응답 처리)
│   │   ├── __init__.py
│   │   ├── admin.py             # 관리자 API (DB 초기화 등)
│   │   ├── contents.py          # 컨텐츠 관련 API
│   │   ├── users.py             # 사용자 관련 API
│   │   └── recommendations.py   # 추천 관련 API
│   ├── service/                 # 비즈니스 로직 계층 (Service 계층)
│   │   ├── __init__.py
│   │   └── recommendation_service.py # 추천 비즈니스 로직
│   ├── repository/              # 데이터 접근 계층 (Repository 계층)
│   │   ├── __init__.py
│   │   ├── base.py              # Repository 기본 클래스
│   │   ├── content.py           # 컨텐츠 Repository
│   │   ├── user.py              # 사용자 Repository
│   │   └── recommendation.py    # 추천 Repository
│   ├── models/                  # 데이터베이스 모델 (Entity/DAO 계층)
│   │   ├── __init__.py
│   │   ├── content.py           # 컨텐츠 모델
│   │   ├── user.py              # 사용자 모델
│   │   └── recommendation.py    # 추천 모델
│   ├── dto/                     # API 입출력 스키마 (DTO 계층)
│   │   ├── __init__.py
│   │   ├── content.py           # 컨텐츠 DTO
│   │   ├── user.py              # 사용자 DTO
│   │   └── recommendation.py    # 추천 DTO
│   ├── core/                    # 핵심 설정
│   │   ├── config.py            # 환경 설정
│   │   ├── database.py          # 데이터베이스 연결
│   │   └── sql_loader.py        # SQL 파일 로더
│   ├── utils/                   # 유틸리티 함수들
│   │   └── content_utils.py     # 컨텐츠 관련 유틸리티
│   └── todo/                    # 실습용 TODO 파일들
│       ├── contents.py          # 컨텐츠 API 실습
│       ├── recommendations.py   # 추천 API 실습
│       └── recommendation_service.py # 서비스 계층 실습
├── sql/                         # 데이터베이스 스크립트
│   ├── create_schema.sql        # 스키마 생성
│   ├── create_tables.sql        # 테이블 생성
│   ├── drop_schema.sql          # 스키마 삭제
│   └── sample_data.sql          # 샘플 데이터
├── .env                         # 환경변수 (DB 연결 정보)
├── requirements.txt             # 의존성 패키지
├── startup.py                   # 서버 시작 스크립트
├── README.md                    # 프로젝트 문서
└── FASTAPI_TUTORIAL.md          # FastAPI 실습 가이드
```

## 아키텍처 특징

### 계층형 아키텍처 (Layered Architecture)
```
Client → Controller → Service → Repository → Database
   ↑        ↓           ↓          ↓
  JSON     DTO       Domain     DAO/ORM
```

#### 각 계층의 역할
- **Controller Layer** (`app/controller/`): HTTP 요청/응답 처리, 라우팅, API 엔드포인트
- **Service Layer** (`app/service/`): 비즈니스 로직 처리, 복잡한 업무 규칙
- **Repository Layer** (`app/repository/`): 데이터베이스 접근 추상화, CRUD 작업
- **Model Layer** (`app/models/`): 데이터베이스 테이블 정의 (SQLAlchemy ORM)
- **DTO Layer** (`app/dto/`): API 입출력 데이터 검증 및 전송 (Pydantic)
- **Core Layer** (`app/core/`): 설정, 데이터베이스 연결 등 핵심 기능
- **Utils Layer** (`app/utils/`): 공통 유틸리티 함수들

### 설계 패턴
- **Repository Pattern**: Repository 클래스를 통한 데이터 접근 추상화
- **Service Pattern**: 비즈니스 로직의 캡슐화 및 재사용
- **DTO Pattern**: Pydantic 스키마를 통한 데이터 전송 객체
- **Dependency Injection**: FastAPI의 Depends를 활용한 의존성 주입
- **Configuration Management**: Pydantic Settings를 통한 환경 설정

## 설치 및 실행

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정
`.env` 파일에서 데이터베이스 연결 정보 수정:
```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/rcmd_practice
PORT=8080
```

### 4. 서버 실행
```bash
# 방법 1: startup.py 사용 (권장)
python startup.py

# 방법 2: uvicorn 직접 사용
uvicorn app.main:app --reload

# 방법 3: 다른 포트로 실행
uvicorn app.main:app --reload --port 8080
```

### 5. 데이터베이스 초기화
서버 실행 후 다음 API로 데이터베이스 초기화:
```bash
# POST 요청으로 DB 초기화
curl -X POST http://localhost:8000/api/v1/admin/init-db

# 또는 Swagger UI에서: http://localhost:8080/docs
```

## API 엔드포인트

### 관리자 API
- `POST /api/v1/admin/init-db` - 데이터베이스 초기화
- `GET /api/v1/admin/status` - 데이터베이스 상태 확인

### 추천 관련
- `GET /api/v1/recommendations/` - 영화 추천 조회 (일반/개인화)
  - Query Parameter: `user_id` (선택사항)
- `POST /api/v1/recommendations/` - 추천 영화 추가
- `DELETE /api/v1/recommendations/{user_id}/{content_id}` - 추천 삭제
- `GET /api/v1/recommendations/stats?user_id={user_id}` - 사용자 추천 통계

### 컨텐츠 관련
- `POST /api/v1/contents/` - 컨텐츠 데이터 추가
- `GET /api/v1/contents/` - 컨텐츠 목록 조회 (필터링, 페이징)
- `GET /api/v1/contents/{content_id}` - 특정 컨텐츠 조회
- `GET /api/v1/contents/search/title?title=검색어` - 제목 검색
- `GET /api/v1/contents/latest/top?limit=10` - 최신 컨텐츠

### 사용자 관련
- `POST /api/v1/users/` - 사용자 생성
- `GET /api/v1/users/` - 사용자 목록 조회

## 데이터베이스 구조

### 주요 테이블
- **contents**: 컨텐츠 정보 (영화, 드라마 등)
- **users**: 사용자 정보
- **rcmd_user_content**: 사용자별 추천 관계 테이블

### 인덱스 최적화
- `idx_type`: 컨텐츠 타입별 검색 최적화
- `idx_year`: 연도별 검색 최적화
- `idx_genre`: 장르별 검색 최적화
- `idx_name`: 사용자명 검색 최적화

## 계층형 아키텍처의 장점

### 1. 관심사 분리 (Separation of Concerns)
- 각 계층이 명확한 책임을 가짐
- HTTP 처리, 비즈니스 로직, 데이터 접근이 분리됨

### 2. 확장성 (Scalability)
- 새로운 기능 추가 시 해당 계층만 수정
- 비즈니스 로직 변경이 API나 데이터베이스에 영향 없음

### 3. 테스트 용이성 (Testability)
- 각 계층별 독립적 단위 테스트 가능
- Mock 객체를 통한 격리된 테스트

### 4. 유지보수성 (Maintainability)
- 코드 변경 시 영향 범위 최소화
- 계층별 책임이 명확하여 버그 추적 용이

### 5. 재사용성 (Reusability)
- Service 계층의 비즈니스 로직을 여러 Controller에서 재사용
- Repository 기본 클래스를 통한 코드 재사용

### 6. 기술 독립성 (Technology Independence)
- 데이터베이스 변경 시 Repository 계층만 수정
- 프론트엔드 변경 시 Controller 계층만 수정

## 개발 가이드

### API 개발 순서
1. **DTO 정의**: 입출력 데이터 구조 설계
2. **Model 정의**: 데이터베이스 테이블 구조 설계
3. **Repository 구현**: 기본적인 데이터 접근 로직
4. **Service 구현**: 비즈니스 로직 및 복잡한 처리
5. **Controller 구현**: HTTP 엔드포인트 및 라우팅

### 코딩 컨벤션
- **Controller**: HTTP 상태 코드, 에러 처리에 집중
- **Service**: 비즈니스 규칙, 트랜잭션 처리에 집중
- **Repository**: 단순한 데이터 접근, SQL 쿼리에 집중
- **DTO**: 데이터 검증, 직렬화에 집중

### 네이밍 규칙
- **camelCase**: API 요청/응답에서 사용 (`userId`, `contentId`)
- **snake_case**: Python 내부 코드에서 사용 (`user_id`, `content_id`)
- **alias 설정**: Pydantic에서 둘 다 지원

## 실습 가이드

자세한 FastAPI 실습 내용은 [FASTAPI_TUTORIAL.md](./FASTAPI_TUTORIAL.md)를 참고하세요.

### 주요 실습 내용
- 계층형 아키텍처 이해
- Controller, Service, Repository 계층 활용법
- API 엔드포인트 구현
- 데이터 검증 및 에러 처리
- 의존성 주입 활용

### 실습 파일 위치
- `app/todo/contents.py` - 컨텐츠 API 실습
- `app/todo/recommendations.py` - 추천 API 실습
- `app/todo/recommendation_service.py` - 서비스 계층 실습

## API 문서

서버 실행 후 다음 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:
- **Swagger UI**: http://localhost:8080/docs

## 기술 스택

- **Backend Framework**: FastAPI 0.115.0
- **Database ORM**: SQLAlchemy 2.0.36
- **Database Driver**: PyMySQL 1.1.1
- **Data Validation**: Pydantic 2.10.0
- **Configuration**: Pydantic Settings 2.6.1
- **Environment**: Python-dotenv 1.0.1
- **Security**: Cryptography 43.0.3
- **ASGI Server**: Uvicorn 0.32.0

## 배포 및 운영

### 포트 변경
```bash
# 환경변수로 포트 설정
export PORT=8080 && python startup.py

# 또는 uvicorn 직접 사용
uvicorn app.main:app --port 8080
```

### 프로덕션 배포
```bash
# Gunicorn 사용
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
```

## 라이센스

이 프로젝트는 교육 목적으로 제작되었습니다.