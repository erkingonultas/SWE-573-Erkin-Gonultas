package com.erkingonultas.backendProject.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.erkingonultas.backendProject.models.Post;

public interface PostRepository extends JpaRepository<Post, Long> {
}
