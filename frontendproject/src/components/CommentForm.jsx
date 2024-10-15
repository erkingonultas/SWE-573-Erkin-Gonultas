import React, { useState } from 'react';
import axios from 'axios';

const CommentForm = ({ postId, parentCommentId, onCommentCreated }) => {
    const [content, setContent] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/comments/create', {
                postId,
                content,
                parentCommentId
            });
            onCommentCreated(response.data);
            setContent('');
        } catch (error) {
            console.error('Error creating comment:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea
                value={content}
                onChange={(e) => setContent(e.target.value)}
                placeholder="Write a comment..."
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default CommentForm;
