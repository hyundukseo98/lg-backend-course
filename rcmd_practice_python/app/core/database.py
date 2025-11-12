from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def execute_sql_file(filename: str):
    """SQL 파일을 실행하는 헬퍼 함수"""
    from app.core.sql_loader import sql_loader
    
    try:
        sql_content = sql_loader.load_sql(filename)
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        with engine.connect() as conn:
            for statement in statements:
                if statement:
                    logger.info(f"Executing: {statement[:50]}...")
                    conn.execute(text(statement))
            conn.commit()
            logger.info(f"Successfully executed {filename}")
    except Exception as e:
        logger.error(f"Error executing {filename}: {e}")
        raise

def init_db():
    """데이터베이스 완전 초기화 (스키마부터 재생성)"""
    logger.info("Starting database initialization...")
    
    try:
        # 1. 스키마 삭제
        execute_sql_file('drop_schema.sql')
        
        # 2. 스키마 생성
        execute_sql_file('create_schema.sql')
        
        # 3. 테이블 생성
        execute_sql_file('create_tables.sql')
        
        # 4. 샘플 데이터 삽입
        execute_sql_file('sample_data.sql')
        
        logger.info("Database initialization completed successfully!")
        
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise

def reset_data_only():
    """데이터만 초기화 (테이블 구조 유지)"""
    logger.info("Resetting data only...")
    
    try:
        with engine.connect() as conn:
            # 외래키 제약조건 때문에 순서 중요
            conn.execute(text("DELETE FROM rcmd_user_movie"))
            conn.execute(text("DELETE FROM user"))
            conn.execute(text("DELETE FROM movies"))
            
            # AUTO_INCREMENT 초기화
            conn.execute(text("ALTER TABLE movies AUTO_INCREMENT = 1"))
            conn.execute(text("ALTER TABLE user AUTO_INCREMENT = 1"))
            
            conn.commit()
        
        # 샘플 데이터 재삽입
        execute_sql_file('sample_data.sql')
        
        logger.info("Data reset completed successfully!")
        
    except Exception as e:
        logger.error(f"Data reset failed: {e}")
        raise

def get_root_engine():
    """데이터베이스 지정 없이 MySQL 서버에 연결"""
    from urllib.parse import urlparse, urlunparse
    parsed = urlparse(settings.database_url)
    # 데이터베이스 부분을 제거하고 루트로 연결
    root_url = urlunparse((parsed.scheme, parsed.netloc, '', '', '', ''))
    return create_engine(root_url)

def schema_exists() -> bool:
    """rcmd_practice 스키마가 존재하는지 확인"""
    try:
        root_engine = get_root_engine()
        with root_engine.connect() as conn:
            result = conn.execute(text("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'rcmd_practice'"))
            return result.fetchone() is not None
    except Exception as e:
        logger.error(f"Error checking schema existence: {e}")
        return False

def tables_exist() -> bool:
    """필요한 테이블들이 존재하는지 확인"""
    if not schema_exists():
        return False
        
    required_tables = ['contents', 'users', 'rcmd_user_content']
    try:
        root_engine = get_root_engine()
        with root_engine.connect() as conn:
            for table in required_tables:
                result = conn.execute(text(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'rcmd_practice' AND TABLE_NAME = '{table}'"))
                if not result.fetchone():
                    return False
            return True
    except Exception as e:
        logger.error(f"Error checking tables existence: {e}")
        return False

def execute_sql_file_with_root(filename: str):
    """루트 연결로 SQL 파일 실행"""
    from app.core.sql_loader import sql_loader
    
    try:
        sql_content = sql_loader.load_sql(filename)
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        root_engine = get_root_engine()
        with root_engine.connect() as conn:
            for statement in statements:
                if statement:
                    logger.info(f"Executing: {statement[:50]}...")
                    conn.execute(text(statement))
            conn.commit()
            logger.info(f"Successfully executed {filename}")
    except Exception as e:
        logger.error(f"Error executing {filename}: {e}")
        raise

def init_db_if_needed():
    """스키마가 없을 때만 DB 초기화"""
    if schema_exists() and tables_exist():
        logger.info("Database already exists. Skipping initialization.")
        return
    
    logger.info("Database not found. Starting initialization...")
    
    # 스키마가 없으면 루트 연결로 스키마부터 생성
    if not schema_exists():
        execute_sql_file_with_root('create_schema.sql')
    
    # 이후 작업은 기존 방식으로
    execute_sql_file('create_tables.sql')
    execute_sql_file('sample_data.sql')
    
    logger.info("Database initialization completed successfully!")