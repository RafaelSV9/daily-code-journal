package com.rafaelsv.taskmanager.service;

import com.rafaelsv.taskmanager.dto.TaskRequest;
import com.rafaelsv.taskmanager.dto.TaskResponse;
import com.rafaelsv.taskmanager.model.Task;
import com.rafaelsv.taskmanager.repository.TaskRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class TaskService {

    private final TaskRepository taskRepository;

    public TaskService(TaskRepository taskRepository) {
        this.taskRepository = taskRepository;
    }

    public List<TaskResponse> findAll() {
        return taskRepository.findAll().stream()
                .map(this::toResponse)
                .collect(Collectors.toList());
    }

    public TaskResponse findById(Long id) {
        Task task = taskRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Task not found with id: " + id));
        return toResponse(task);
    }

    public TaskResponse create(TaskRequest request) {
        Task task = new Task();
        task.setTitle(request.getTitle());
        task.setDescription(request.getDescription());
        if (request.getStatus() != null && !request.getStatus().isBlank()) {
            task.setStatus(request.getStatus());
        }
        Task saved = taskRepository.save(task);
        return toResponse(saved);
    }

    public TaskResponse update(Long id, TaskRequest request) {
        Task task = taskRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Task not found with id: " + id));

        task.setTitle(request.getTitle());
        task.setDescription(request.getDescription());
        if (request.getStatus() != null && !request.getStatus().isBlank()) {
            task.setStatus(request.getStatus());
        }

        Task saved = taskRepository.save(task);
        return toResponse(saved);
    }

    public void delete(Long id) {
        if (!taskRepository.existsById(id)) {
            throw new RuntimeException("Task not found with id: " + id);
        }
        taskRepository.deleteById(id);
    }

    public TaskResponse updateStatus(Long id, String status) {
        Task task = taskRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Task not found with id: " + id));

        task.setStatus(status);
        Task saved = taskRepository.save(task);
        return toResponse(saved);
    }

    private TaskResponse toResponse(Task task) {
        return new TaskResponse(
                task.getId(),
                task.getTitle(),
                task.getDescription(),
                task.getStatus(),
                task.getCreatedAt(),
                task.getUpdatedAt()
        );
    }
}
