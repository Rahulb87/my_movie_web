import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Movie API calls
export const movieAPI = {
  getAll: (language = null) => {
    if (language) {
      return api.get(`/movies?language=${language}`);
    }
    return api.get('/movies');
  },

  getById: (id) => api.get(`/movies/${id}`),

  create: (movieData) => api.post('/movies', movieData),

  update: (id, movieData) => api.put(`/movies/${id}`, movieData),

  delete: (id) => api.delete(`/movies/${id}`),
};

export default api;
