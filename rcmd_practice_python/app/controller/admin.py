# app/api/admin.py (새 파일 생성)
from fastapi import APIRouter, HTTPException
from app.core.database import init_db
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/init-db")
def initialize_database():
    """
    데이터베이스 초기화 API
    - 스키마 생성
    - 테이블 생성  
    - 샘플 데이터 삽입
    """
    try:
        logger.info("🔄 Starting database initialization...")
        init_db()
        logger.info("✅ Database initialization completed!")
        
        return {
            "message": "Database initialized successfully",
            "status": "success",
            "details": {
                "schema": "created",
                "tables": "created", 
                "sample_data": "inserted"
            }
        }
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise HTTPException(status_code=500, detail=f"Database initialization failed: {str(e)}")

@router.get("/status")
def get_database_status():
    """데이터베이스 상태 확인"""
    try:
        from app.core.database import engine
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        
        return {
            "database": "connected",
            "status": "healthy"
        }
    except Exception as e:
        return {
            "database": "disconnected", 
            "status": "unhealthy",
            "error": str(e)
        }