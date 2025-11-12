package com.example.rcmd.models.dto;

import jakarta.validation.constraints.NotNull;

public class RcmdCreate {
    
    @NotNull(message = "User ID is required")
    private Integer userId;
    
    @NotNull(message = "Content ID is required")
    private Integer contentId;
    
    // Constructors
    public RcmdCreate() {}
    
    public RcmdCreate(Integer userId, Integer contentId) {
        this.userId = userId;
        this.contentId = contentId;
    }
    
    // Getters and Setters
    public Integer getUserId() {
        return userId;
    }
    
    public void setUserId(Integer userId) {
        this.userId = userId;
    }
    
    public Integer getContentId() {
        return contentId;
    }
    
    public void setContentId(Integer contentId) {
        this.contentId = contentId;
    }
}