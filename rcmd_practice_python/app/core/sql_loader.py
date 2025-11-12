from pathlib import Path

class SQLLoader:
    def __init__(self):
        self.sql_dir = Path(__file__).parent.parent.parent / "sql"
        self._queries = {}
    
    def load_sql(self, filename: str) -> str:
        """SQL 파일을 로드하여 문자열로 반환"""
        if filename not in self._queries:
            file_path = self.sql_dir / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                self._queries[filename] = f.read()
        return self._queries[filename]
    
    def get_query(self, filename: str, query_name: str) -> str:
        """특정 쿼리를 추출 (주석으로 구분)"""
        content = self.load_sql(filename)
        queries = content.split('--')
        
        for query_block in queries:
            if query_name in query_block:
                lines = query_block.strip().split('\n')
                # 첫 번째 줄(주석) 제거하고 쿼리만 반환
                return '\n'.join(lines[1:]).strip()
        
        raise ValueError(f"Query '{query_name}' not found in {filename}")

sql_loader = SQLLoader()