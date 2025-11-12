package com.example.rcmd.controller;

import com.example.rcmd.models.dto.ContentResponse;
import com.example.rcmd.service.ContentService;
import com.example.rcmd.models.dto.ContentCreate;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/example/contents")
public class ContentController {
    
    @Autowired
    private ContentService contentService;
    
    /**
     * 새 영화 생성
     * CRUD 계층을 통한 데이터 생성 예시
     */
    @PostMapping
    public ResponseEntity<ContentResponse> createContent(@Valid @RequestBody ContentCreate contentData) {
        try {
            ContentResponse content = contentService.create(contentData);
            return ResponseEntity.status(HttpStatus.CREATED).body(content);
        } catch (Exception e) {
            return ResponseEntity.badRequest().build();
        }
    }
}