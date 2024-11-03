import React, { useState } from 'react';

const CreatePost = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [tags, setTags] = useState('');
  const [image, setImage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('tags', tags);
    if (image) formData.append('image', image);

    // Call the API to create the post
    await fetch('/api/posts', {
      method: 'POST',
      body: formData,
    });
    // Redirect or update the UI after submission
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Create a New Post</h1>
      <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required placeholder="Title" />
      <textarea value={description} onChange={(e) => setDescription(e.target.value)} required placeholder="Description"></textarea>
      <input type="text" value={tags} onChange={(e) => setTags(e.target.value)} placeholder="Tags (comma separated)" />
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreatePost;
