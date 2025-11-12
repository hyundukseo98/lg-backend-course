from typing import Any, Dict
from sqlalchemy.orm import Session

class CRUDBase:
    def __init__(self, model):
        """CRUD 기본 클래스"""
        self.model = model

    def get(self, db: Session, id: Any):
        """ID로 단일 레코드 조회"""
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100):
        """여러 레코드 조회 (페이징)"""
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in):
        """새 레코드 생성"""
        try:
            obj_data = self._extract_data(obj_in)
            db_obj = self.model(**obj_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except Exception as e:
            db.rollback()
            raise e

    def update(self, db: Session, *, db_obj, obj_in):
        """기존 레코드 업데이트"""
        try:
            obj_data = self._extract_data(obj_in)
            for field, value in obj_data.items():
                setattr(db_obj, field, value)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except Exception as e:
            db.rollback()
            raise e

    def remove(self, db: Session, *, id: int):
        """레코드 삭제"""
        try:
            obj = db.query(self.model).get(id)
            if obj is None:
                raise ValueError(f"Object with id {id} not found")
            db.delete(obj)
            db.commit()
            return obj
        except Exception as e:
            db.rollback()
            raise e

    def _extract_data(self, obj_in) -> Dict[str, Any]:
        """Pydantic 모델에서 데이터 추출"""
        if hasattr(obj_in, 'model_dump'):
            return obj_in.model_dump()
        elif hasattr(obj_in, 'dict'):
            return obj_in.dict()
        elif isinstance(obj_in, dict):
            return obj_in
        else:
            raise ValueError("Invalid input type for data extraction")