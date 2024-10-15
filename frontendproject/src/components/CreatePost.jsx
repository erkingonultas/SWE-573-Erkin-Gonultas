import React, { useState } from 'react';
import axios from 'axios';

function CreatePost() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [tags, setTags] = useState('');
  const [image, setImage] = useState(null);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onloadend = () => {
      setImage(reader.result);  // Base64 encoded string
    };
    reader.readAsDataURL(file);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const postData = {
      title,
      description,
      tags: tags.split(','),  // Split tags into an array
      image,
    };

    try {
      await axios.post('/posts/create', postData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`  // Assuming you are using JWT for auth
        }
      });
      alert('Post created successfully!');
    } catch (err) {
      console.error('Error creating post', err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        placeholder="Title" 
        value={title} 
        onChange={(e) => setTitle(e.target.value)} 
        required 
      />
      <textarea 
        placeholder="Description" 
        value={description} 
        onChange={(e) => setDescription(e.target.value)} 
        required 
      />
      <input 
        type="text" 
        placeholder="Tags (comma-separated)" 
        value={tags} 
        onChange={(e) => setTags(e.target.value)} 
      />
      <input 
        type="file" 
        onChange={handleImageUpload} 
        required 
      />
      <button type="submit">Create Post</button>
    </form>
  );
}

export default CreatePost;
