package com.example.rcmd.models.dto;

import java.time.LocalDateTime;

public class UserResponse {
    
    private Integer userId;
    private String name;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    
    // Constructors
    public UserResponse() {}
    
    public UserResponse(Integer userId, String name, LocalDateTime createdAt, LocalDateTime updatedAt) {
        this.userId = userId;
        this.name = name;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }
    
    // Getters and Setters
    public Integer getUserId() {
        return userId;
    }
    
    public void setUserId(Integer userId) {
        this.userId = userId;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
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