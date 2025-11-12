package com.example.rcmd.models.entity;

import jakarta.persistence.*;

/**
 * 사용자-컨텐츠 추천 엔티티
 * - 사용자에게 추천된 컨텐츠 정보를 저장
 * - 복합 키를 사용하여 사용자와 컨텐츠의 다대다 관계 표현
 */
@Entity
@Table(name = "rcmd_user_content")
@IdClass(RcmdUserContentId.class)
public class RcmdUserContent {
    
    @Id
    @Column(name = "user_id")
    private Integer userId;
    
    @Id
    @Column(name = "content_id")
    private Integer contentId;
    
    // Constructors
    public RcmdUserContent() {}
    
    public RcmdUserContent(Integer userId, Integer contentId) {
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