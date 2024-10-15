package com.erkingonultas.backendProject.util;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class JwtUtils {

    @Value("${jwt.secret}")
    private String jwtSecret;

    // Extract username/email from the JWT token
    public String extractUsername(String token) {
        return getClaimsFromToken(token).getSubject();  // Assuming the 'subject' is the username or email
    }

    private Claims getClaimsFromToken(String token) {
        return Jwts.parser()
                .setSigningKey(jwtSecret)
                .parseClaimsJws(token)
                .getBody();
    }
}