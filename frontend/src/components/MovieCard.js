import React from 'react';
import '../styles/moviecard.css';

const MovieCard = ({ movie, onEdit, onDelete }) => {
  return (
    <div className="movie-card">
      <div className="movie-image-container">
        <img src={movie.image_url} alt={movie.title} className="movie-image" />
        <div className="movie-overlay">
          <a href={movie.url} target="_blank" rel="noopener noreferrer" className="play-btn">
            ▶ Watch Now
          </a>
        </div>
      </div>
      
      <div className="movie-info">
        <h3 className="movie-title">{movie.title}</h3>
        <p className="movie-language">
          {movie.language === 'marathi' && '🎭 Marathi'}
          {movie.language === 'hindi' && '🎬 Hindi'}
          {movie.language === 'punjabi' && '🎪 Punjabi'}
        </p>
        <p className="movie-date">
          {new Date(movie.release_date).toLocaleDateString()}
        </p>
        
        {onEdit && onDelete && (
          <div className="movie-actions">
            <button className="edit-btn" onClick={() => onEdit(movie)}>Edit</button>
            <button className="delete-btn" onClick={() => onDelete(movie.id)}>Delete</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default MovieCard;
