from typing import List
from collections import defaultdict
from app.dto.content import Content, ContentsByType, ContentTypeList

def group_contents_by_type(contents: List[Content]) -> ContentTypeList:
    """컨텐츠를 타입별로 그룹화"""
    grouped = defaultdict(list)
    for content in contents:
        grouped[content.type].append(content)
    
    contents_by_type = []
    for content_type, type_contents in grouped.items():
        contents_by_type.append(ContentsByType(
            type=content_type,
            contents=type_contents
        ))
    
    return ContentTypeList(
        recommendations=contents_by_type
    )