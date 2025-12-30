import React, { useState, useEffect } from 'react';
import MovieCard from '../components/MovieCard';
import '../styles/home.css';
import { movieAPI } from '../utils/api';

const Home = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedLanguage, setSelectedLanguage] = useState(null);

  useEffect(() => {
    fetchMovies();
  }, [selectedLanguage]);

  const fetchMovies = async () => {
    try {
      setLoading(true);
      const response = await movieAPI.getAll(selectedLanguage);
      setMovies(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch movies. Please try again later.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleLanguageFilter = (language) => {
    setSelectedLanguage(language);
  };

  return (
    <div className="home">
      <div className="hero-section">
        <div className="hero-content">
          <h1>Welcome to CineHub</h1>
          <p>Your entertainment destination for Marathi, Hindi & Punjabi Movies</p>
          {selectedLanguage && (
            <button
              className="clear-filter-btn"
              onClick={() => setSelectedLanguage(null)}
            >
              Clear Filter
            </button>
          )}
        </div>
      </div>

      <div className="container">
        {loading && (
          <div className="loading">
            <p>Loading movies...</p>
          </div>
        )}

        {error && (
          <div className="error">
            <p>{error}</p>
          </div>
        )}

        {!loading && !error && movies.length === 0 && (
          <div className="no-movies">
            <p>No movies found. Check back soon!</p>
          </div>
        )}

        {!loading && !error && movies.length > 0 && (
          <>
            <h2 className="section-title">
              {selectedLanguage
                ? selectedLanguage.charAt(0).toUpperCase() +
                  selectedLanguage.slice(1) +
                  ' Movies'
                : 'Latest Movies'}
            </h2>
            <div className="movies-grid">
              {movies.map(movie => (
                <MovieCard key={movie.id} movie={movie} />
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default Home;
