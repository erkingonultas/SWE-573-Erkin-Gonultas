package com.erkingonultas.backendProject.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.erkingonultas.backendProject.models.Post;
import com.erkingonultas.backendProject.models.User;
import com.erkingonultas.backendProject.repositories.PostRepository;

import java.util.List;

@Service
public class PostService {

    @Autowired
    private PostRepository postRepository;

    public Post createPost(String title, String description, List<String> tags, String image, User user) {
        Post post = new Post();
        post.setTitle(title);
        post.setDescription(description);
        post.setTags(tags);
        post.setImage(image);  // Image can be a Base64 string or a file path if stored in cloud
        post.setUser(user);

        return postRepository.save(post);
    }

    public List<Post> getAllPosts() {
        return postRepository.findAll();
    }
}
