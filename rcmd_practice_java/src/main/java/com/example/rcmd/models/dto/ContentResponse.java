package com.example.rcmd.models.dto;

import com.example.rcmd.models.entity.Content;

import java.time.LocalDateTime;

public class ContentResponse {

    private Integer contentId;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Constructors
    public ContentResponse() {}

    public ContentResponse(Integer contentId, LocalDateTime createdAt, LocalDateTime updatedAt) {
        this.contentId = contentId;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    public ContentResponse(Content content) {
        this.contentId = content.getContentId();
        this.createdAt = content.getCreatedAt();
        this.updatedAt = content.getUpdatedAt();
    }

    // Getters and Setters
    public Integer getContentId() {
        return contentId;
    }

    public void setContentId(Integer contentId) {
        this.contentId = contentId;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
