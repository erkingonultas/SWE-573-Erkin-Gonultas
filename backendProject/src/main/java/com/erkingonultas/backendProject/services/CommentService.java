package com.erkingonultas.backendProject.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.erkingonultas.backendProject.models.Comment;
import com.erkingonultas.backendProject.models.Post;
import com.erkingonultas.backendProject.models.User;
import com.erkingonultas.backendProject.repositories.CommentRepository;
import com.erkingonultas.backendProject.repositories.PostRepository;

import java.util.List;

@Service
public class CommentService {

    @Autowired
    private CommentRepository commentRepository;

    @Autowired
    private PostRepository postRepository;

    public Comment createComment(Long postId, String content, User user, Long parentCommentId) {
        Post post = postRepository.findById(postId)
                .orElseThrow(() -> new RuntimeException("Post not found"));
        
        Comment comment = new Comment();
        comment.setPost(post);
        comment.setContent(content);
        comment.setUser(user);

        if (parentCommentId != null) {
            Comment parentComment = commentRepository.findById(parentCommentId)
                    .orElseThrow(() -> new RuntimeException("Parent comment not found"));
            comment.setParentComment(parentComment);
        }

        return commentRepository.save(comment);
    }

    public List<Comment> getCommentsByPost(Long postId) {
        return commentRepository.findByPostIdOrderByUpvotesDesc(postId);  // Sorted by upvotes
    }

    public Comment upvoteComment(Long commentId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("Comment not found"));
        comment.setUpvotes(comment.getUpvotes() + 1);
        return commentRepository.save(comment);
    }

    public Comment downvoteComment(Long commentId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("Comment not found"));
        comment.setDownvotes(comment.getDownvotes() + 1);
        return commentRepository.save(comment);
    }

    public Comment markBestAnswer(Long commentId, User postAuthor) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("Comment not found"));
        
        // Ensure the post author is marking the comment as the best answer
        if (!comment.getPost().getUser().equals(postAuthor)) {
            throw new RuntimeException("Only the post author can mark the best answer.");
        }

        comment.setBestAnswer(true);
        return commentRepository.save(comment);
    }
}
