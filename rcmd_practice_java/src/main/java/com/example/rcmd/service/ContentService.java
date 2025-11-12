package com.example.rcmd.service;

import com.example.rcmd.models.dto.ContentResponse;
import com.example.rcmd.models.dto.RcmdContentResponse;
import com.example.rcmd.models.dto.RcmdResponse;
import com.example.rcmd.models.entity.Content;
import com.example.rcmd.repository.ContentRepository;
import com.example.rcmd.models.dto.ContentCreate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * 컨텐츠 비즈니스 로직 계층
 * - 컨텐츠 관련 모든 비즈니스 로직 처리
 * - 데이터 접근 계층과 API 계층 사이의 중간 역할
 */
@Service
public class ContentService {

    @Autowired
    private ContentRepository contentRepository;

    public ContentResponse create(ContentCreate contentCreate) {
        Content content = new Content(contentCreate.getTitle(),
                contentCreate.getType(),
                contentCreate.getYear(),
                contentCreate.getGenre());
        Content savedContent = contentRepository.save(content);
        return convertResponse(savedContent);
    }

    private ContentResponse convertResponse(Content content) {
        ContentResponse contentResponse = new ContentResponse();
        contentResponse.setContentId(content.getContentId());
        contentResponse.setCreatedAt(content.getCreatedAt());
        contentResponse.setUpdatedAt(content.getUpdatedAt());
        return contentResponse;
    }
}