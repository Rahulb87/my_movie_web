from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

# Simple in-memory database (for demo purposes)
movies_db = []
next_id = 1

# Sample data
sample_movies = [
    {
        'id': 1,
        'title': 'Natrang',
        'language': 'marathi',
        'url': 'https://www.youtube.com/embed/sample1',
        'image_url': 'https://via.placeholder.com/300x400?text=Natrang',
        'release_date': '2023-01-15'
    },
    {
        'id': 2,
        'title': 'Laal Singh Chaddha',
        'language': 'hindi',
        'url': 'https://www.youtube.com/embed/sample2',
        'image_url': 'https://via.placeholder.com/300x400?text=Laal+Singh',
        'release_date': '2023-02-20'
    },
    {
        'id': 3,
        'title': 'Sardar Udham',
        'language': 'punjabi',
        'url': 'https://www.youtube.com/embed/sample3',
        'image_url': 'https://via.placeholder.com/300x400?text=Sardar+Udham',
        'release_date': '2023-03-10'
    }
]

movies_db.extend(sample_movies)
next_id = 4

# Routes

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Get all movies, optionally filtered by language"""
    language = request.args.get('language')
    
    if language:
        filtered_movies = [m for m in movies_db if m['language'].lower() == language.lower()]
        return jsonify(filtered_movies)
    
    return jsonify(movies_db)

@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """Get a specific movie by ID"""
    movie = next((m for m in movies_db if m['id'] == movie_id), None)
    
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    return jsonify(movie)

@app.route('/api/movies', methods=['POST'])
def create_movie():
    """Create a new movie"""
    global next_id
    
    data = request.get_json()
    
    # Validation
    if not data or not data.get('title') or not data.get('language'):
        return jsonify({'error': 'Title and language are required'}), 400
    
    new_movie = {
        'id': next_id,
        'title': data.get('title'),
        'language': data.get('language'),
        'url': data.get('url', ''),
        'image_url': data.get('image_url', ''),
        'release_date': data.get('release_date', datetime.now().isoformat())
    }
    
    movies_db.append(new_movie)
    next_id += 1
    
    return jsonify(new_movie), 201

@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """Update an existing movie"""
    movie = next((m for m in movies_db if m['id'] == movie_id), None)
    
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    data = request.get_json()
    
    # Update fields
    if 'title' in data:
        movie['title'] = data['title']
    if 'language' in data:
        movie['language'] = data['language']
    if 'url' in data:
        movie['url'] = data['url']
    if 'image_url' in data:
        movie['image_url'] = data['image_url']
    if 'release_date' in data:
        movie['release_date'] = data['release_date']
    
    return jsonify(movie)

@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Delete a movie"""
    global movies_db
    
    movie = next((m for m in movies_db if m['id'] == movie_id), None)
    
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    movies_db = [m for m in movies_db if m['id'] != movie_id]
    
    return jsonify({'message': 'Movie deleted successfully'})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
