import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CommentForm from './CommentForm';

const CommentsList = ({ postId }) => {
    const [comments, setComments] = useState([]);

    useEffect(() => {
        fetchComments();
    }, []);

    const fetchComments = async () => {
        try {
            const response = await axios.get(`/comments/post/${postId}`);
            setComments(response.data);
        } catch (error) {
            console.error('Error fetching comments:', error);
        }
    };

    const handleUpvote = async (commentId) => {
        try {
            await axios.post('/comments/upvote', { commentId });
            fetchComments();  // Refresh comments
        } catch (error) {
            console.error('Error upvoting comment:', error);
        }
    };

    const handleDownvote = async (commentId) => {
        try {
            await axios.post('/comments/downvote', { commentId });
            fetchComments();
        } catch (error) {
            console.error('Error downvoting comment:', error);
        }
    };

    const handleMarkBestAnswer = async (commentId) => {
        try {
            await axios.post('/comments/best-answer', { commentId });
            fetchComments();
        } catch (error) {
            console.error('Error marking best answer:', error);
        }
    };

    return (
        <div>
            {comments.map((comment) => (
                <div key={comment.id}>
                    <p>{comment.content}</p>
                    <p>Upvotes: {comment.upvotes} | Downvotes: {comment.downvotes}</p>
                    <button onClick={() => handleUpvote(comment.id)}>Upvote</button>
                    <button onClick={() => handleDownvote(comment.id)}>Downvote</button>
                    <button onClick={() => handleMarkBestAnswer(comment.id)}>Mark as Best Answer</button>
                    <CommentForm postId={postId} parentCommentId={comment.id} onCommentCreated={fetchComments} />
                </div>
            ))}
        </div>
    );
};

export default CommentsList;
