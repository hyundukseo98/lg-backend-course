package com.example.rcmd.todo;

import com.example.rcmd.models.dto.ContentCreate;
import com.example.rcmd.models.dto.ContentResponse;
import com.example.rcmd.models.dto.RcmdContentResponse;
import com.example.rcmd.models.dto.RcmdResponse;
import com.example.rcmd.models.entity.Content;
import com.example.rcmd.repository.ContentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * 컨텐츠 비즈니스 로직 계층
 * - 컨텐츠 관련 모든 비즈니스 로직 처리
 * - 데이터 접근 계층과 API 계층 사이의 중간 역할
 */
@Service
public class ContentTodoService {
    
    @Autowired
    private ContentRepository contentRepository;
    
    public ContentResponse create(ContentCreate contentCreate) {
        // TODO: ContentCreate 정보로 Content 객체를 생성하세요

        // TODO: contentRepository.save() 함수를 사용하여 Content 객체를 저장(생성)하세요

        // TODO: 저장된 Content의 정보를 convertResponse() 함수를 사용해 ContentResponse 객체로 변환하여 함수를 반환하세요.

        return null; // 이 줄을 삭제하고 위 코드를 작성하세요
    }

    private ContentResponse convertResponse(Content content) {
        ContentResponse contentResponse = new ContentResponse();
        contentResponse.setContentId(content.getContentId());
        contentResponse.setCreatedAt(content.getCreatedAt());
        contentResponse.setUpdatedAt(content.getUpdatedAt());
        return contentResponse;
    }
}