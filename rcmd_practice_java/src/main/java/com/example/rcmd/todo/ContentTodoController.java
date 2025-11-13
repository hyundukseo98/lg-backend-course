package com.example.rcmd.todo;

import com.example.rcmd.models.dto.ContentCreate;
import com.example.rcmd.models.dto.ContentResponse;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/contents")
public class ContentTodoController {
    
    @Autowired
    private ContentTodoService contentService;
    
    /**
     * 새 컨텐츠 생성
     * CRUD 계층을 통한 데이터 생성 예시
     * 
     * TODO: 다음 단계를 구현하세요
     * 1. contentService.create() 메서드를 사용하여 컨텐츠를 생성하세요
     * 2. 생성된 컨텐츠 정보를 반환하세요
     * 3. 예외 발생 시 적절한 HTTP 상태 코드를 반환하세요
     */
    @PostMapping
    public ResponseEntity<ContentResponse> createContent(@Valid @RequestBody ContentCreate contentData) {
        try {
            // TODO: contentService.create() 메서드를 사용하여 컨텐츠를 생성하세요

            // TODO: 생성된 컨텐츠 정보를 반환하세요

            return null; // 이 줄을 삭제하고 위 코드를 작성하세요
        } catch (Exception e) {
            // TODO: 적절한 HTTP 예외를 발생시키세요

            return null; // 이 줄을 삭제하고 위 코드를 작성하세요
        }
    }
}