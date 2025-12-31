from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os
import json

app = Flask(__name__, 
            static_folder='static',
            static_url_path='',
            template_folder='templates')
CORS(app)

# Path to movies.json file (in docs folder for GitHub Pages)
MOVIES_JSON_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs', 'movies.json')

# Global variables
movies_db = []
next_id = 1

def load_movies_from_file():
    """Load movies from movies.json file"""
    global movies_db, next_id
    
    try:
        if os.path.exists(MOVIES_JSON_PATH):
            with open(MOVIES_JSON_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                movies_db = data.get('movies', [])
                next_id = data.get('nextId', len(movies_db) + 1)
                print(f"✅ Loaded {len(movies_db)} movies from {MOVIES_JSON_PATH}")
                return True
    except Exception as e:
        print(f"❌ Error loading movies from file: {e}")
    
    return False

def save_movies_to_file():
    """Save movies to movies.json file"""
    try:
        data = {
            'movies': movies_db,
            'nextId': next_id,
            'lastUpdated': datetime.now().isoformat()
        }
        
        os.makedirs(os.path.dirname(MOVIES_JSON_PATH), exist_ok=True)
        
        with open(MOVIES_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ Saved {len(movies_db)} movies to {MOVIES_JSON_PATH}")
        return True
    except Exception as e:
        print(f"❌ Error saving movies to file: {e}")
        return False

# Load movies from file on startup
load_movies_from_file()

# ============ API ROUTES ============

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
        'release_date': data.get('release_date', datetime.now().isoformat().split('T')[0])
    }
    
    movies_db.append(new_movie)
    next_id += 1
    
    # Save to file
    save_movies_to_file()
    
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
    
    # Save to file
    save_movies_to_file()
    
    return jsonify(movie)

@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Delete a movie"""
    global movies_db
    
    movie = next((m for m in movies_db if m['id'] == movie_id), None)
    
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    movies_db = [m for m in movies_db if m['id'] != movie_id]
    
    # Save to file
    save_movies_to_file()
    
    return jsonify({'message': 'Movie deleted successfully'})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

# ============ FRONTEND ROUTES ============

@app.route('/')
def home():
    """Serve the home page"""
    return render_template('index.html')

@app.route('/admin')
def admin():
    """Serve the admin page"""
    return render_template('index.html')

# Catch-all route for SPA (Single Page Application)
@app.route('/<path:path>')
def catch_all(path):
    """Catch all routes and serve index.html for SPA routing"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
