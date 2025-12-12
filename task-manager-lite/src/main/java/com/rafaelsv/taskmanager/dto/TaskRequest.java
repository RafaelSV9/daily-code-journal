package com.rafaelsv.taskmanager.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class TaskRequest {

    @NotBlank(message = "Title is mandatory")
    @Size(max = 100, message = "Title must have at most 100 characters")
    private String title;

    @Size(max = 1000, message = "Description must have at most 1000 characters")
    private String description;

    @Size(max = 30, message = "Status must have at most 30 characters")
    private String status;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
