package com.example.rcmd.models.dto;

import com.example.rcmd.models.entity.Content;

import java.util.List;

public class RcmdResponse {

    private String type;
    private List<Content> contents;

    public RcmdResponse() {
    }

    public RcmdResponse(String type, List<Content> contents) {
        this.type = type;
        this.contents = contents;
    }

    public String getType() {
        return type;
    }

    public List<Content> getContents() {
        return contents;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setContents(List<Content> contents) {
        this.contents = contents;
    }
}
