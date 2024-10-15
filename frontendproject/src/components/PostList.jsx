import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    async function fetchPosts() {
      const response = await axios.get('/posts/all');
      setPosts(response.data);
    }
    fetchPosts();
  }, []);

  return (
    <div>
      <h1>All Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <h2>{post.title}</h2>
            <img src={post.image} alt={post.title} style={{ width: '200px' }} />
            <p>{post.description}</p>
            <p>Tags: {post.tags.join(', ')}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostList;
