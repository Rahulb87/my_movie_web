from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

# Path to movies.json file
MOVIES_JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'movies.json')

# In-memory database
movies_db = []
next_id = 1

# Load movies from movies.json on startup
def load_movies_from_file():
    global movies_db, next_id
    try:
        if os.path.exists(MOVIES_JSON_PATH):
            with open(MOVIES_JSON_PATH, 'r') as f:
                data = json.load(f)
                # Handle both array format and object format
                if isinstance(data, list):
                    movies_db = data
                elif isinstance(data, dict) and 'movies' in data:
                    movies_db = data['movies']
                else:
                    movies_db = []
                
                # Set next_id to max ID + 1
                if movies_db:
                    max_id = max(movie['id'] for movie in movies_db)
                    next_id = max_id + 1
                else:
                    next_id = 1
                
                print(f'✅ Loaded {len(movies_db)} movies from {MOVIES_JSON_PATH}')
        else:
            print(f'⚠️ movies.json file not found at {MOVIES_JSON_PATH}')
            movies_db = []
            next_id = 1
    except Exception as e:
        print(f'❌ Error loading movies.json: {e}')
        movies_db = []
        next_id = 1

# Save movies to movies.json file
def save_movies_to_file():
    try:
        os.makedirs(os.path.dirname(MOVIES_JSON_PATH), exist_ok=True)
        with open(MOVIES_JSON_PATH, 'w') as f:
            json.dump(movies_db, f, indent=2)
        print(f'✅ Saved {len(movies_db)} movies to {MOVIES_JSON_PATH}')
    except Exception as e:
        print(f'❌ Error saving movies.json: {e}')

# Load movies on startup
load_movies_from_file()

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
    save_movies_to_file()  # Persist to movies.json
    
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
    
    save_movies_to_file()  # Persist to movies.json
    return jsonify(movie)

@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Delete a movie"""
    global movies_db
    
    movie = next((m for m in movies_db if m['id'] == movie_id), None)
    
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    movies_db = [m for m in movies_db if m['id'] != movie_id]
    save_movies_to_file()  # Persist to movies.json
    
    return jsonify({'message': 'Movie deleted successfully'})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
