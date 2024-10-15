package com.erkingonultas.backendProject.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.erkingonultas.backendProject.models.Post;
import com.erkingonultas.backendProject.models.User;
import com.erkingonultas.backendProject.services.PostService;
import com.erkingonultas.backendProject.util.PostRequest;

import java.security.Principal;
import java.util.List;

@RestController
@RequestMapping("/posts")
public class PostController {

    @Autowired
    private PostService postService;

    @Autowired
    private AuthenticatedUserService authenticatedUserService;

    @PostMapping("/create")
    public Post createPost(@RequestBody PostRequest postRequest, Principal principal) {
        User user = authenticatedUserService.getUserFromPrincipal();  // Fetch the logged-in user
        return postService.createPost(postRequest.getTitle(), postRequest.getDescription(), postRequest.getTags(), postRequest.getImage(), user);
    }

    @GetMapping("/all")
    public List<Post> getAllPosts() {
        return postService.getAllPosts();
    }
}
