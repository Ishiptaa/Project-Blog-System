import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('/api/posts/')  // Using the proxy setup
      .then(res => setPosts(res.data))
      .catch(err => console.error('Error fetching posts:', err));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>My Blog</h1>
      {posts.length > 0 ? (
        posts.map(post => (
          <div key={post.id} style={{ marginBottom: 20, border: '1px solid #ddd', padding: 15 }}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
            <small>By {post.author_details?.username}</small>
          </div>
        ))
      ) : (
        <p>No posts found. Create some in Django admin!</p>
      )}
    </div>
  );
}

export default App;