package com.example.rcmd.service;

import com.example.rcmd.models.dto.RcmdResponse;
import com.example.rcmd.models.entity.Content;
import com.example.rcmd.repository.ContentRepository;
import com.example.rcmd.repository.RecommendationRepository;
import com.example.rcmd.models.dto.RcmdContentResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class RecommendationService {

    @Autowired
    private RecommendationRepository recommendationRepository;

    @Autowired
    private ContentRepository contentRepository;

    public RcmdContentResponse getUserRecommendations(Integer userId) {

        if(userId == null){
            return getLatestContents(10);
        }

        List<Content> contents = recommendationRepository.findUserRecommendations(userId);

        if (contents.isEmpty()) {
            return getLatestContents(10);
        }

        return convertToResponse(contents);
    }

    private RcmdContentResponse getLatestContents(Integer limit) {
        List<Content> contents = contentRepository.findLatestMovies().stream()
                .limit(limit)
                .collect(Collectors.toList());
        return convertToResponse(contents);
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