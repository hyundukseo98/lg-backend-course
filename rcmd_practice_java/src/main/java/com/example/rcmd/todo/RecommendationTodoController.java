package com.example.rcmd.todo;

import com.example.rcmd.service.UserService;
import com.example.rcmd.models.dto.RcmdContentResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/recommendations")
public class RecommendationTodoController {

    @Autowired
    private UserService userService;

    @Autowired
    private RecommendationTodoService recommendationService;
    
    /**
     * 컨텐츠 추천 조회
     * - userId 있으면: 개인화 추천
     * - userId 없으면: 일반 추천 (최신 컨텐츠)
     *
     * TODO: 다음 단계를 구현하세요
     * 1. user_id가 있는 경우와 없는 경우를 구분
     * 2. 사용자 존재 확인
     * 3. 추천 컨텐츠 조회
     * 4. 적절한 예외 처리
     */
    @GetMapping
    public ResponseEntity<RcmdContentResponse> getRecommendations(@RequestParam(required = false) Integer userId) {
        try {
            // TODO: userId가 있는지 확인하는 조건문 작성
            if (userId != null) {
                // TODO: 사용자 존재 확인 (userService.getById 함수 사용)
                
                // TODO: 사용자가 없으면 404 에러 발생
            }
            // TODO: 추천 컨텐츠 조회 (개인화 추천 영화 조회 또는 추천이 없으면 최신 컨텐츠 10개 반환 / recommendationService.getUserRecommendations 함수 사용)

            return null; // 이 줄을 삭제하고 위 코드를 작성하세요
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
}