package com.example.rcmd.models.entity;

import java.io.Serializable;
import java.util.Objects;

/**
 * 사용자-컨텐츠 추천 복합키 엔터티
 * - 추천 복합키 정보를 저장
 */
public class RcmdUserContentId implements Serializable {
    
    private Integer userId;
    private Integer contentId;
    
    // Constructors
    public RcmdUserContentId() {}
    
    public RcmdUserContentId(Integer userId, Integer contentId) {
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
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        RcmdUserContentId that = (RcmdUserContentId) o;
        return Objects.equals(userId, that.userId) && Objects.equals(contentId, that.contentId);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(userId, contentId);
    }
}