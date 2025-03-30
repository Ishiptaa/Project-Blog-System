import axios from 'axios';

const api = axios.create({
  baseURL: '/api', // This will be proxied to Django
});

export const getPosts = () => api.get('/posts/');
export const getPost = (id) => api.get(`/posts/${id}/`);
export const createPost = (postData) => api.post('/posts/', postData);
