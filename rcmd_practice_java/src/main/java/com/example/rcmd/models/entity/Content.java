package com.example.rcmd.models.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

/**
 * 콘텐츠 엔티티
 * - 콘텐츠 정보를 저장하는 데이터베이스 테이블과 매핑
 * - 추천 시스템의 핵심 데이터 모델
 */
@Entity
@Table(name = "contents")
public class Content {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "content_id")
    private Integer contentId;
    
    @Column(name = "title", nullable = false, length = 255)
    private String title;

    @Column(name = "type", nullable = false, length = 100)
    private String type;
    
    @Column(name = "year", nullable = false)
    private Integer year;
    
    @Column(name = "genre", nullable = false, length = 100)
    private String genre;
    
    @Column(name = "created_at")
    private LocalDateTime createdAt;
    
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;
    
    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        updatedAt = LocalDateTime.now();
    }
    
    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }
    
    // Constructors
    public Content() {}
    
    public Content(String title, String type, Integer year, String genre) {
        this.title = title;
        this.type = type;
        this.year = year;
        this.genre = genre;
    }
    
    // Getters and Setters
    public Integer getContentId() {
        return contentId;
    }
    
    public void setContentId(Integer contentId) {
        this.contentId = contentId;
    }
    
    public String getTitle() {
        return title;
    }
    
    public void setTitle(String title) {
        this.title = title;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    
    public Integer getYear() {
        return year;
    }
    
    public void setYear(Integer year) {
        this.year = year;
    }
    
    public String getGenre() {
        return genre;
    }
    
    public void setGenre(String genre) {
        this.genre = genre;
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