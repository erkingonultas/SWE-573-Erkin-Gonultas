package com.erkingonultas.backendProject.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.erkingonultas.backendProject.services.AuthService;
import com.erkingonultas.backendProject.util.AuthRequest;
import com.erkingonultas.backendProject.util.AuthResponse;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private AuthService authService;

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody AuthRequest authRequest) {
        String token = authService.registerUser(authRequest.getEmail(), authRequest.getUsername(), authRequest.getPassword());
        return ResponseEntity.ok(new AuthResponse(token));
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody AuthRequest authRequest) {
        String token = authService.loginUser(authRequest.getEmail(), authRequest.getPassword());
        return ResponseEntity.ok(new AuthResponse(token));
    }
}
