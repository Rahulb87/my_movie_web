import React, { useState, useEffect } from 'react';
import '../styles/movieform.css';

const MovieForm = ({ movie = null, onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    title: '',
    language: 'marathi',
    url: '',
    image_url: '',
    release_date: new Date().toISOString().split('T')[0],
  });

  useEffect(() => {
    if (movie) {
      setFormData({
        title: movie.title,
        language: movie.language,
        url: movie.url,
        image_url: movie.image_url,
        release_date: movie.release_date.split('T')[0],
      });
    }
  }, [movie]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title || !formData.language) {
      alert('Please fill in all required fields');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="movie-form-container">
      <h2>{movie ? 'Edit Movie' : 'Add New Movie'}</h2>
      
      <form onSubmit={handleSubmit} className="movie-form">
        <div className="form-group">
          <label htmlFor="title">Movie Title *</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="Enter movie title"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="language">Language *</label>
          <select
            id="language"
            name="language"
            value={formData.language}
            onChange={handleChange}
            required
          >
            <option value="marathi">🎭 Marathi</option>
            <option value="hindi">🎬 Hindi</option>
            <option value="punjabi">🎪 Punjabi</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="url">Movie URL</label>
          <input
            type="url"
            id="url"
            name="url"
            value={formData.url}
            onChange={handleChange}
            placeholder="https://example.com/movie"
          />
        </div>

        <div className="form-group">
          <label htmlFor="image_url">Image URL</label>
          <input
            type="url"
            id="image_url"
            name="image_url"
            value={formData.image_url}
            onChange={handleChange}
            placeholder="https://example.com/image.jpg"
          />
        </div>

        <div className="form-group">
          <label htmlFor="release_date">Release Date</label>
          <input
            type="date"
            id="release_date"
            name="release_date"
            value={formData.release_date}
            onChange={handleChange}
          />
        </div>

        <div className="form-actions">
          <button type="submit" className="submit-btn">
            {movie ? 'Update Movie' : 'Add Movie'}
          </button>
          <button type="button" className="cancel-btn" onClick={onCancel}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default MovieForm;
