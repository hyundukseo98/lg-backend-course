package com.example.rcmd.models.dto;

import jakarta.validation.constraints.NotBlank;

public class UserCreate {
    
    @NotBlank(message = "Name is required")
    private String name;
    
    // Constructors
    public UserCreate() {}
    
    public UserCreate(String name) {
        this.name = name;
    }
    
    // Getters and Setters
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}