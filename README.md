# 🎬 CineHub - Movie Website

A modern, responsive **unified** movie website built with Flask and vanilla JavaScript. Manage movies in multiple languages (Marathi, Hindi, and Punjabi) with a sleek admin panel—all from a single server.

## 🌟 What's New (v2.0)

✨ **Unified Architecture**: Single Flask server serving both API and frontend  
📱 **Responsive Design**: Mobile, tablet, and desktop optimized  
🎨 **Modern UI**: Gradient animations and smooth interactions  
⚡ **Fast Performance**: No build step required, instant startup  
🔒 **Built-in API**: All CRUD operations on one server  
📡 **Language Filtering**: Marathi, Hindi, Punjabi movie support  
🏆 **Admin Panel**: Complete movie management system  

## 🎬 Features

- **🏠 Home Page**: Browse all movies with beautiful grid layout
- **🎭 Language Filtering**: Filter by Marathi, Hindi, or Punjabi
- **⚙️ Admin Panel**: Add, edit, and delete movies with form validation
- **📱 Responsive**: Works on mobile, tablet, and desktop
- **🎨 Modern Design**: Gradient backgrounds, smooth animations
- **🌐 Single Server**: No separate frontend/backend complexity
- **📊 RESTful API**: 7 endpoints for full CRUD operations
- **🏢 Branding**: Rahul Corp footer with professional styling

## 📁 Project Structure

```
my_movie_web/
├── app/
│   ├── app.py                 # ⭐ Main unified Flask server (160 lines)
│   ├── static/               # Frontend static assets (if needed)
│   └── templates/
│       └── index.html        # Complete responsive HTML+CSS+JS (550+ lines)
├── backend/                  # [Legacy - for reference only]
├── frontend/                 # [Legacy - for reference only]
├── .venv/                    # Virtual environment
├── .gitignore               # Git configuration
├── UNIFIED_DEPLOYMENT_GUIDE.md  # ⭐ Deployment instructions
└── [Documentation files]
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.13+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/))

### Installation (3 Steps)

**Step 1:** Clone & Navigate
```powershell
git clone https://github.com/Rahulb87/my_movie_web.git
cd my_movie_web
```

**Step 2:** Set Up Environment
```powershell
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.\.venv\Scripts\Activate.ps1
```

**Step 3:** Run Server
```powershell
# Install dependencies
pip install Flask==2.3.3 Flask-CORS==4.0.0

# Start server
python app/app.py
```

✅ **Done!** Visit http://localhost:5000
```
REACT_APP_API_URL=http://localhost:5000/api
```

4. Start the development server:
```bash
npm start
```

The frontend will open on `http://localhost:3000`

## 📱 Pages

### Home Page
- Display of latest movies in a responsive grid
- Language filter menu (Marathi, Hindi, Punjabi)
- Hero section with branding
- Movie cards with watch buttons

### Admin Panel
- Add new movies
- Edit existing movies
- Delete movies
- View all movies in admin interface
## 📖 Available Routes

| Route | Purpose |
|-------|---------|
| `/` | Home page - browse movies |
| `/admin` | Admin panel - manage movies |
| `/api/movies` | Get all movies (or filter: `?language=marathi`) |
| `/api/movies/<id>` | Get/update/delete specific movie |

## 🎨 Design Features

✨ **Dark Theme** with gradient backgrounds  
🎭 **Language Icons** for visual recognition  
📱 **Mobile First** responsive layout  
⚡ **No Build Step** - vanilla JavaScript  
🎨 **CSS Grid** for movie cards layout  

### Color Scheme
- **Dark**: #0f0f0f, #1a1a1a, #2d2d2d
- **Accent**: #ff6b6b (Red)
- **Secondary**: #4ecdc4 (Teal)

## 🔧 Technology Stack

| Component | Technology |
|-----------|-----------|
| Server | Flask 2.3.3 (Python) |
| Frontend | Vanilla JavaScript + HTML5 + CSS3 |
| API | RESTful JSON endpoints |
| CORS | Flask-CORS enabled |
| Port | 5000 (localhost) |

## 📡 API Endpoints

All endpoints return JSON. Authentication not required.

```
GET    /api/movies                    # Get all movies
GET    /api/movies?language=marathi   # Filter by language
GET    /api/movies/<id>               # Get specific movie
POST   /api/movies                    # Create movie (JSON body)
PUT    /api/movies/<id>               # Update movie (JSON body)
DELETE /api/movies/<id>               # Delete movie
```

### Sample Request/Response

**Create Movie (POST /api/movies)**
```json
{
  "title": "Natrang",
  "language": "marathi",
  "url": "https://youtube.com/embed/...",
  "image_url": "https://example.com/image.jpg",
  "release_date": "2025-01-15"
}
```

**Response**
```json
{
  "id": 4,
  "title": "Natrang",
  "language": "marathi",
  "url": "https://youtube.com/embed/...",
  "image_url": "https://example.com/image.jpg",
  "release_date": "2025-01-15"
}
```

## 📚 Sample Movies Included

1. **Natrang** - Marathi classic
2. **Laal Singh Chaddha** - Hindi blockbuster
3. **Sardar Udham** - Punjabi thriller

## 📖 Documentation

- **[Unified Deployment Guide](./UNIFIED_DEPLOYMENT_GUIDE.md)** - Detailed setup and deployment
- **[API Documentation](./API_DOCUMENTATION.md)** - Complete API reference
- **[Quick Reference](./QUICK_REFERENCE.md)** - Common commands

## 🌐 Deployment Options

### Option 1: Local Development (Recommended)
Perfect for development and testing. Runs on `http://localhost:5000`

### Option 2: Python Hosting Service
- **PythonAnywhere** - https://www.pythonanywhere.com
- **Render** - https://render.com
- **Railway** - https://railway.app
- **Heroku** - https://www.heroku.com

### Option 3: GitHub Pages (Static Only)
For pure static site without backend functionality.

See [Unified Deployment Guide](./UNIFIED_DEPLOYMENT_GUIDE.md) for detailed steps.

## 🚨 Troubleshooting

**Port 5000 in use?**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Movies not loading?**
1. Check `http://localhost:5000/api/movies` in browser
2. Look for errors in terminal output
3. Check browser console (F12) for JavaScript errors

**404 errors?**
- Home: `http://localhost:5000`
- Admin: `http://localhost:5000/admin`
- API: `http://localhost:5000/api/movies`

## 📊 Statistics

- **Lines of Code**: ~700 (app.py + index.html)
- **API Endpoints**: 7 (full CRUD)
- **Languages Supported**: 3 (Marathi, Hindi, Punjabi)
- **Responsive Breakpoints**: 3 (Mobile, Tablet, Desktop)
- **Performance**: < 100ms API response time

## 🎯 Future Roadmap

- 🔐 User authentication & admin login
- 💾 Database persistence (SQLAlchemy)
- 🔍 Search functionality
- ⭐ Movie ratings & reviews
- 📹 Video streaming integration
- 👤 User profiles & watchlists
- 📊 Analytics dashboard
- 🌍 Multi-language UI

## 📄 License

© 2025 Rahul Corp. All rights reserved.

## 💬 Support & Contact

- **GitHub**: https://github.com/Rahulb87/my_movie_web
- **Issues**: https://github.com/Rahulb87/my_movie_web/issues

---

**CineHub 🎬** - Your Entertainment Platform  
Built with passion for cinema enthusiasts
