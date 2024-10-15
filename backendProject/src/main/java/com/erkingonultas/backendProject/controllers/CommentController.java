package com.erkingonultas.backendProject.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.erkingonultas.backendProject.models.Comment;
import com.erkingonultas.backendProject.models.User;
import com.erkingonultas.backendProject.services.CommentService;

import java.util.List;

@RestController
@RequestMapping("/comments")
public class CommentController {

    @Autowired
    private CommentService commentService;

    @Autowired
    private AuthenticatedUserService authenticatedUserService;

    @PostMapping("/create")
    public Comment createComment(@RequestParam Long postId,
                                 @RequestParam String content,
                                 @RequestParam(required = false) Long parentCommentId) {
        User user = authenticatedUserService.getUserFromPrincipal();
        return commentService.createComment(postId, content, user, parentCommentId);
    }

    @GetMapping("/post/{postId}")
    public List<Comment> getCommentsByPost(@PathVariable Long postId) {
        return commentService.getCommentsByPost(postId);
    }

    @PostMapping("/upvote")
    public Comment upvoteComment(@RequestParam Long commentId) {
        return commentService.upvoteComment(commentId);
    }

    @PostMapping("/downvote")
    public Comment downvoteComment(@RequestParam Long commentId) {
        return commentService.downvoteComment(commentId);
    }

    @PostMapping("/best-answer")
    public Comment markBestAnswer(@RequestParam Long commentId) {
        User user = authenticatedUserService.getUserFromPrincipal();
        return commentService.markBestAnswer(commentId, user);
    }
}