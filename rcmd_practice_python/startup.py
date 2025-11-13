"""
실습용 FastAPI 서버 시작 스크립트
uvicorn 대신 이 스크립트를 사용하면 더 명확한 로그를 볼 수 있습니다.
"""
import uvicorn
import sys
from app.core.config import settings

def main():
    print("=" * 60)
    print("🎬 Content Recommendation API - 실습용 서버")
    print("=" * 60)
    print("📝 실습 특징:")
    print("   • 서버 시작 시 DB 상태 확인")
    print("   • 샘플 데이터 자동 생성")
    print("   • API 문서: http://localhost:8080/docs")
    print("=" * 60)
    
    try:
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=settings.port,
            reload=True,
            log_level="info",
            reload_excludes=[".venv/*", "__pycache__/*"]
        )
    except KeyboardInterrupt:
        print("\n👋 서버를 종료합니다.")
    except Exception as e:
        print(f"❌ 서버 시작 실패: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()