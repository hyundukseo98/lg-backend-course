# Movie Recommendation API

Spring Boot 기반 영화 추천 시스템 백엔드 (실무 프로젝트 구조)

## 프로젝트 구조

```
rcmd_practice_spring/
├── src/
│   ├── main/
│   │   ├── java/com/example/rcmd/
│   │   │   ├── RcmdPracticeSpringApplication.java  # Spring Boot 애플리케이션 진입점
│   │   │   ├── controller/          # API 컨트롤러들 (완성된 구현)
│   │   │   │   ├── ContentController.java      # 컨텐츠 관련 API
│   │   │   │   └── RecommendationController.java # 추천 관련 API
│   │   │   ├── todo/                # TODO 과제용 컨트롤러들
│   │   │   │   ├── ContentTodoController.java  # 컨텐츠 API 과제
│   │   │   │   └── RecommendationTodoController.java # 추천 API 과제
│   │   │   ├── repository/          # 데이터 접근 계층
│   │   │   │   ├── ContentRepository.java        # 컨텐츠 Repository
│   │   │   │   ├── UserRepository.java           # 사용자 Repository
│   │   │   │   └── RecommendationRepository.java # 추천 Repository
│   │   │   ├── service/             # 비즈니스 로직 계층
│   │   │   │   ├── ContentService.java           # 컨텐츠 Service
│   │   │   │   ├── UserService.java              # 사용자 Service
│   │   │   │   └── RecommendationService.java    # 추천 Service
│   │   │   └── models/              # 데이터 모델
│   │   │       ├── entity/          # JPA 엔티티
│   │   │       │   ├── Content.java     # 컨텐츠 엔티티
│   │   │       │   ├── User.java        # 사용자 엔티티
│   │   │       │   ├── RcmdUserContent.java # 추천 엔티티
│   │   │       │   └── RcmdUserContentId.java # 복합키 클래스
│   │   │       └── dto/             # DTO 클래스
│   │   │           ├── ContentCreate.java # 컨텐츠 생성 DTO
│   │   │           ├── ContentResponse.java # 컨텐츠 응답 DTO
│   │   │           ├── RcmdContentResponse.java # 추천 컨텐츠 응답 DTO
│   │   │           ├── UserCreate.java  # 사용자 생성 DTO
│   │   │           ├── UserResponse.java # 사용자 응답 DTO
│   │   │           └── RcmdCreate.java  # 추천 생성 DTO
│   │   └── resources/
│   │       ├── application.yml      # 애플리케이션 설정
│   │       └── data.sql             # 샘플 데이터 (자동 로딩)
│   └── test/
├── build.gradle                     # Gradle 의존성 관리
├── gradlew                          # Gradle Wrapper 스크립트
└── README.md                        # 프로젝트 문서
```

## 아키텍처 특징

### 계층 구조 (Layered Architecture)
- **API Layer**: Spring Boot 컨트롤러들
- **Service Layer**: 비즈니스 로직 처리
- **Repository Layer**: 데이터 접근 계층

### 설계 패턴
- **Repository Pattern**: JPA Repository를 통한 데이터 접근
- **Dependency Injection**: Spring의 @Autowired를 활용
- **Configuration Management**: Spring Boot의 application.yml 사용

## 설치 및 실행

1. MySQL Docker 컨테이너 실행
```bash
docker run --name mysql-rcmd -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_DATABASE=rcmd_practice -p 3306:3306 -d mysql:8.0
```

**참고**: 애플리케이션 시작 시 샘플 데이터(영화 100개, 사용자 10명, 추천 데이터)가 자동으로 로딩됩니다.

2. 프로젝트 빌드
```bash
./gradlew build
```

3. 서버 실행
```bash
java -jar build/libs/rcmd-practice-spring-0.0.1-SNAPSHOT.jar
```

또는 개발 모드로 실행:
```bash
./gradlew bootRun
```

## API 엔드포인트

### 추천 관련
- `GET /recommendations?userId={user_id}` - 사용자별 컨텐츠 추천 조회
- `POST /recommendations` - 추천 컨텐츠 추가
- `DELETE /recommendations/{userId}/{contentId}` - 추천 삭제

### 컨텐츠 관련
- `POST /contents` - 컨텐츠 데이터 추가

## TODO 과제용 API 엔드포인트

### TODO 컨텐츠 관련 (과제)
- `POST /todo/contents` - **[TODO]** 컨텐츠 데이터 추가 (구현 필요)

### TODO 추천 관련 (과제)
- `GET /todo/recommendations?userId={user_id}` - **[TODO]** 사용자별 컨텐츠 추천 조회 (구현 필요)
- `POST /todo/recommendations` - **[TODO]** 추천 컨텐츠 추가 (구현 필요)
- `DELETE /todo/recommendations/{userId}/{contentId}` - **[TODO]** 추천 삭제 (구현 필요)

## TODO 과제 수행 가이드

### 과제 목표
1. **ContentTodoController**: `createContent()` 메서드 완성
2. **RecommendationTodoController**: 3개 메서드 완성
   - `getRecommendations()`: 추천 조회 로직
   - `addRecommendation()`: 추천 추가 로직
   - `deleteRecommendation()`: 추천 삭제 로직

### 과제 수행 순서
1. TODO 주석을 참고하여 단계별로 구현
2. ContentTodoController에서 컨텐츠 생성 로직 구현
3. RecommendationTodoController에서 추천 관련 로직 구현

### 학습 포인트
- CRUD 패턴 이해
- Spring Boot 컨트롤러 구조
- 예외 처리 및 HTTP 상태 코드
- 서비스 계층 활용

## 실무 프로젝트 구조의 장점

1. **관심사 분리**: 각 모듈이 명확한 책임을 가짐
2. **확장성**: 새로운 기능 추가가 용이
3. **테스트 용이성**: 각 계층별 독립적 테스트 가능
4. **유지보수성**: 코드 변경 시 영향 범위 최소화
5. **재사용성**: Service 클래스를 통한 코드 재사용

## API 문서

**완성된 API**: http://localhost:8090 에서 확인 가능