package com.example.rcmd.todo;

import com.example.rcmd.models.dto.RcmdContentResponse;
import com.example.rcmd.models.dto.RcmdResponse;
import com.example.rcmd.models.entity.Content;
import com.example.rcmd.repository.ContentRepository;
import com.example.rcmd.repository.RecommendationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class RecommendationTodoService {

    @Autowired
    private RecommendationRepository recommendationRepository;

    @Autowired
    private ContentRepository contentRepository;

    public RcmdContentResponse getUserRecommendations(Integer userId) {

        // TODO: userId가 없을 때에는 최신 컨텐츠 10개 반환

        // TODO: recommendRepository.findUserRecommendation() 함수를 사용해 개인 추천 컨텐츠 조회

        // TODO: 개인 추천 컨텐츠가 없을 떄에는 최신 컨텐츠 10개 반환

        // TODO:  RcmdContentResponse 객체로 변환하여 함수를 반환 (convertToResponse 함수 사용)
        return null; // 이 줄을 삭제하고 위 코드를 작성하세요
    }

    private RcmdContentResponse getLatestContents(Integer limit) {

        // TODO: contentRepository.findLatestMovies() 함수를 사용해 최신 컨텐츠 limit개 조회

        // TODO:  RcmdContentResponse 객체로 변환하여 함수를 반환
        return null; // 이 줄을 삭제하고 위 코드를 작성하세요
    }

    private RcmdContentResponse convertToResponse(List<Content> contents) {
        RcmdContentResponse result = new RcmdContentResponse();
        List<RcmdResponse> recommendations = new ArrayList<>();

        Map<String, List<Content>> contentByType = new HashMap<>();
        for (Content content : contents) {
            // 해당하는 키가 없다면 해당 키를 기반으로 new ArrayList<>() 를 만들어주고 put한다
            contentByType.computeIfAbsent(content.getType(), k -> new ArrayList<>()).add(content);
        }

        for(Map.Entry<String, List<Content>> entry : contentByType.entrySet()) {
            recommendations.add(new RcmdResponse(entry.getKey(), entry.getValue()));
        }

        result.setRecommendations(recommendations);

        return result;
    }
}