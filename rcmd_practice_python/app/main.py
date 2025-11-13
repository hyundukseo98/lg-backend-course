from fastapi import FastAPI
from app.controller import contents, users, recommendations, admin
from app.core.database import init_db_if_needed
from app.todo import contents_todo, recommendations_todo
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 앱 시작 시 자동 데이터베이스 초기화
logger.info("🚀 Starting Content Recommendation API...")
logger.info("🔄 Initializing database...")
init_db_if_needed()
logger.info("✅ Database initialization completed!")
logger.info("🎬 Content Recommendation API is ready!")

# FastAPI 앱 생성
app = FastAPI(
    title="Content Recommendation API",
    description="FastAPI 기반 콘텐츠 추천 시스템 (실습용 - 자동 DB 초기화)",
    version="1.0.0"
)

# 공통 API prefix 설정
API_PREFIX = "/api/v1"

# API 라우터 등록
app.include_router(contents.router, prefix=f"{API_PREFIX}/contents", tags=["contents"])
app.include_router(users.router, prefix=f"{API_PREFIX}/users", tags=["users"])
app.include_router(recommendations.router, prefix=f"{API_PREFIX}/recommendations", tags=["recommendations"])
app.include_router(admin.router, prefix=f"{API_PREFIX}/admin", tags=["admin"])

app.include_router(contents_todo.router, prefix=f"{API_PREFIX}/example/contents", tags=["contents_todo"])
app.include_router(recommendations_todo.router, prefix=f"{API_PREFIX}/example/recommendations", tags=["recommendations_todo"])

@app.get("/")
def read_root():
    return {
        "message": "Content Recommendation API", 
        "version": "1.0.0",
        "status": "Database auto-initialized on startup",
        "endpoints": {
            "contents": "/contents",
            "users": "/users", 
            "recommendations": "/recommendations",
            "docs": "/docs",
            "contents_todo": "/example/contents",
            "recommendations_todo": "/example/recommendations"
        }
    }