package com.example.rcmd.service;

import com.example.rcmd.models.entity.User;
import com.example.rcmd.repository.UserRepository;
import com.example.rcmd.models.dto.UserResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;


@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public Optional<UserResponse> getById(Integer userId) {
        return userRepository.findById(userId).map(this::convertToResponse);
    }

    private UserResponse convertToResponse(User user) {
        return new UserResponse(
                user.getUserId(),
                user.getName(),
                user.getCreatedAt(),
                user.getUpdatedAt()
        );
    }
}