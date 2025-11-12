package com.example.rcmd.models.dto;

import java.util.List;

public class RcmdContentResponse {

    private List<RcmdResponse> recommendations;

    public RcmdContentResponse() {
    }

    public RcmdContentResponse(List<RcmdResponse> recommendations) {
        this.recommendations = recommendations;
    }

    public List<RcmdResponse> getRecommendations() {
        return recommendations;
    }

    public void setRecommendations(List<RcmdResponse> recommendations) {
        this.recommendations = recommendations;
    }
}