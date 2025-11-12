package com.example.rcmd.models.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class ContentCreate {

    @NotBlank(message = "Title is required")
    private String title;

    @NotBlank(message = "Type is required")
    private String type;

    @NotNull(message = "Year is required")
    private Integer year;
    
    @NotBlank(message = "Genre is required")
    private String genre;
    
    // Constructors
    public ContentCreate() {}
    
    public ContentCreate(String title, String type, Integer year, String genre) {
        this.title = title;
        this.type = type;
        this.year = year;
        this.genre = genre;
    }
    
    // Getters and Setters
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
}