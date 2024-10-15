package com.erkingonultas.backendProject.controllers;

import com.erkingonultas.backendProject.models.User;
import com.erkingonultas.backendProject.repositories.UserRepository;
import com.erkingonultas.backendProject.util.JwtUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

@Service
public class AuthenticatedUserService {

    @Autowired
    private JwtUtils jwtUtils;

    @Autowired
    private UserRepository userRepository;

    public User getUserFromPrincipal() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication == null || !authentication.isAuthenticated()) {
            return null;  // No authenticated user
        }

        // Extract JWT token from Authentication object
        String token = (String) authentication.getCredentials();
        String username = jwtUtils.extractUsername(token);

        // Find the user in the database by username or email
        return userRepository.findByEmail(username)
                .orElseThrow(() -> new RuntimeException("User not found: " + username));
    }
}
