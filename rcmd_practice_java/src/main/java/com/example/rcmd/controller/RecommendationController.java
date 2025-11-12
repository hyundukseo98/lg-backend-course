package com.example.rcmd.controller;

import com.example.rcmd.service.ContentService;
import com.example.rcmd.service.RecommendationService;
import com.example.rcmd.service.UserService;
import com.example.rcmd.models.dto.RcmdContentResponse;
import com.example.rcmd.models.dto.UserResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/example/recommendations")
public class RecommendationController {
    
    @Autowired
    private RecommendationService recommendationService;
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public ResponseEntity<RcmdContentResponse> getRecommendations(@RequestParam(required = false) Integer userId) {
        try {
            if (userId != null) {
                Optional<UserResponse> user = userService.getById(userId);
                if (user.isEmpty()) {
                    return ResponseEntity.notFound().build();
                }
            }
            RcmdContentResponse response = recommendationService.getUserRecommendations(userId);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
}