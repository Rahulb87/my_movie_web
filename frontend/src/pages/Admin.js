import React, { useState, useEffect } from 'react';
import MovieForm from '../components/MovieForm';
import MovieCard from '../components/MovieCard';
import '../styles/admin.css';
import { movieAPI } from '../utils/api';

const Admin = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingMovie, setEditingMovie] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');

  useEffect(() => {
    fetchMovies();
  }, []);

  const fetchMovies = async () => {
    try {
      setLoading(true);
      const response = await movieAPI.getAll();
      setMovies(response.data);
    } catch (err) {
      setError('Failed to fetch movies');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddMovie = () => {
    setEditingMovie(null);
    setShowForm(true);
  };

  const handleEditMovie = (movie) => {
    setEditingMovie(movie);
    setShowForm(true);
  };

  const handleDeleteMovie = async (movieId) => {
    if (window.confirm('Are you sure you want to delete this movie?')) {
      try {
        await movieAPI.delete(movieId);
        setMovies(movies.filter(m => m.id !== movieId));
        setSuccessMessage('Movie deleted successfully!');
        setTimeout(() => setSuccessMessage(''), 3000);
      } catch (err) {
        setError('Failed to delete movie');
      }
    }
  };

  const handleFormSubmit = async (formData) => {
    try {
      if (editingMovie) {
        // Update existing movie
        const response = await movieAPI.update(editingMovie.id, formData);
        setMovies(movies.map(m => (m.id === editingMovie.id ? response.data : m)));
        setSuccessMessage('Movie updated successfully!');
      } else {
        // Create new movie
        const response = await movieAPI.create(formData);
        setMovies([...movies, response.data]);
        setSuccessMessage('Movie added successfully!');
      }
      setShowForm(false);
      setEditingMovie(null);
      setTimeout(() => setSuccessMessage(''), 3000);
    } catch (err) {
      setError('Failed to save movie');
      console.error('Error:', err);
    }
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setEditingMovie(null);
  };

  return (
    <div className="admin">
      <div className="admin-header">
        <h1>Admin Panel</h1>
        <p>Manage your movie collection</p>
      </div>

      <div className="container">
        {successMessage && (
          <div className="success-message">
            {successMessage}
          </div>
        )}

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {!showForm && (
          <button className="add-movie-btn" onClick={handleAddMovie}>
            + Add New Movie
          </button>
        )}

        {showForm && (
          <MovieForm
            movie={editingMovie}
            onSubmit={handleFormSubmit}
            onCancel={handleFormCancel}
          />
        )}

        {loading && <p className="text-center">Loading movies...</p>}

        {!loading && movies.length === 0 && (
          <p className="text-center">No movies yet. Add your first movie!</p>
        )}

        {!loading && movies.length > 0 && (
          <>
            <h2 className="section-title">All Movies ({movies.length})</h2>
            <div className="admin-movies-grid">
              {movies.map(movie => (
                <MovieCard
                  key={movie.id}
                  movie={movie}
                  onEdit={handleEditMovie}
                  onDelete={handleDeleteMovie}
                />
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default Admin;
