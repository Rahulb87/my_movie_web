# CineHub Unified Deployment Guide

## Overview

CineHub is now a **unified single-server application** that combines both the Flask API backend and HTML frontend into one seamless experience. This guide covers deployment on localhost and GitHub Pages.

---

## 🚀 Local Development Setup

### Prerequisites
- Python 3.13+ ([Download](https://www.python.org/downloads/))
- Git ([Download](https://git-scm.com/))

### Step 1: Clone the Repository

```powershell
git clone https://github.com/Rahulb87/my_movie_web.git
cd my_movie_web
```

### Step 2: Set Up Python Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3: Install Dependencies

```powershell
pip install Flask==2.3.3 Flask-CORS==4.0.0
```

### Step 4: Run the Unified Server

```powershell
# From project root directory
python app/app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Step 5: Access the Application

Open your browser and visit:
- **Home Page:** http://localhost:5000
- **Admin Panel:** http://localhost:5000/admin
- **API Base:** http://localhost:5000/api

---

## 📁 Project Structure

### Current Architecture (Unified)

```
my_movie_web/
├── app/
│   ├── app.py                 # Main unified Flask server
│   ├── static/               # Frontend static assets (future)
│   └── templates/
│       └── index.html        # Main HTML template with embedded UI
├── .venv/                    # Virtual environment
├── .gitignore               # Git ignore rules
└── [documentation files]
```

### Key Files

- **`app/app.py`** (160 lines)
  - Flask application entry point
  - All 7 REST API endpoints (GET, POST, PUT, DELETE)
  - Frontend HTML serving with SPA routing
  - Includes sample movie data (Natrang, Laal Singh Chaddha, Sardar Udham)

- **`app/templates/index.html`** (550+ lines)
  - Complete responsive UI with embedded JavaScript
  - Navigation bar with language filtering
  - Home page with movie grid
  - Admin panel for CRUD operations
  - Footer with Rahul Corp branding

---

## 🎬 Features

### Home Page
- Display all movies or filter by language (Marathi, Hindi, Punjabi)
- Responsive grid layout
- Movie cards with images, titles, and release dates
- Language indicators with emojis

### Admin Panel
- Add new movies with validation
- Edit existing movies
- Delete movies with confirmation
- Form with fields:
  - Movie Title
  - Language (dropdown)
  - Movie URL
  - Image URL
  - Release Date

### API Endpoints

All endpoints return JSON responses:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/movies` | Get all movies (optional `?language=` filter) |
| GET | `/api/movies/<id>` | Get specific movie |
| POST | `/api/movies` | Create new movie |
| PUT | `/api/movies/<id>` | Update movie |
| DELETE | `/api/movies/<id>` | Delete movie |
| GET | `/` | Serve home page |
| GET | `/admin` | Serve admin panel |

### Sample Movie Data
- **Natrang** (Marathi)
- **Laal Singh Chaddha** (Hindi)
- **Sardar Udham** (Punjabi)

---

## 🌐 GitHub Pages Deployment (Static Site)

### Important Note
GitHub Pages traditionally hosts **static sites** only. The current Flask app requires a Python runtime. For full GitHub Pages deployment, you have options:

#### Option 1: Deploy Flask App to a Python Hosting Service
Services like **PythonAnywhere**, **Render**, **Heroku**, or **Railway** support Flask:

**For PythonAnywhere:**
1. Create account at https://www.pythonanywhere.com
2. Upload project files
3. Create Flask web app with your app.py
4. Set working directory and source code
5. Reload the web app

**Example URL:** `https://yourusername.pythonanywhere.com`

#### Option 2: Deploy Static HTML Version
If you want pure static site hosting on GitHub Pages:

1. Ensure `index.html` is in repository root or `docs/` folder
2. Go to GitHub repo Settings → Pages
3. Set source to "main" branch / "root" or "docs" folder
4. Site will be available at: `https://Rahulb87.github.io/my_movie_web/`

**Note:** Static version won't have backend API functionality. Data persistence requires a backend server.

---

## 🔧 Development Tips

### Hot Reload
The Flask app runs with debug mode enabled, so changes to `app.py` automatically reload the server.

### Debugging
Enable detailed error messages by checking the browser console (F12) for JavaScript errors and the terminal for Python errors.

### Data Persistence
Currently, movies are stored in memory. On server restart, only sample movies remain. To add persistence:

1. Install SQLAlchemy: `pip install Flask-SQLAlchemy`
2. Modify `app.py` to use database models
3. Initialize database on startup

### Adding Real Movie Data
Edit the `sample_movies` list in `app/app.py`:

```python
sample_movies = [
    {
        'id': 1,
        'title': 'Movie Name',
        'language': 'marathi',  # or 'hindi', 'punjabi'
        'url': 'https://youtube.com/embed/...',
        'image_url': 'https://example.com/image.jpg',
        'release_date': '2025-01-15'
    },
    # ... more movies
]
```

---

## 🐛 Troubleshooting

### Port 5000 Already in Use
```powershell
# Find and kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or modify app.py to use different port:
if __name__ == '__main__':
    app.run(debug=True, port=3000)
```

### CORS Errors
The app has CORS enabled by default. If you see CORS errors:
1. Check browser console (F12)
2. Verify API endpoint URLs in `index.html` JavaScript

### Movies Not Loading
1. Check terminal for Python errors
2. Verify `/api/movies` endpoint returns data:
   - Visit http://localhost:5000/api/movies in browser
   - Should display JSON array of movies

### 404 Errors
- Home page: http://localhost:5000
- Admin: http://localhost:5000/admin
- API: http://localhost:5000/api/movies

---

## 📊 Performance Considerations

- **In-memory Database:** Fine for < 1000 movies
- **Concurrent Users:** Supports 50+ simultaneous connections with Flask dev server
- **Image Loading:** Uses placeholder URLs; replace with real image URLs for production

---

## 📝 Next Steps

1. **Add Database:** Implement SQLAlchemy for data persistence
2. **User Authentication:** Add login system for admin panel
3. **Real Images:** Replace placeholder image URLs
4. **Deployment:** Deploy to PythonAnywhere or similar service
5. **Domain:** Connect custom domain (if using external hosting)

---

## 📞 Support

For issues or questions:
1. Check the [API Documentation](./API_DOCUMENTATION.md)
2. Review [Project Summary](./PROJECT_SUMMARY.md)
3. Check GitHub Issues: https://github.com/Rahulb87/my_movie_web/issues

---

## 🏢 Branding

- **Logo:** 🎬 CineHub
- **Copyright:** © 2025 Rahul Corp. All rights reserved.
- **Footer Brand:** Rahul Corp ™

---

**Last Updated:** January 2025  
**Version:** 2.0 (Unified Server)
