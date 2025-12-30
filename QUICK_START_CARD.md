# 🎬 CineHub - Quick Reference Card

## 🚀 Getting Started (30 seconds)

```powershell
# 1. Clone the project
git clone https://github.com/Rahulb87/my_movie_web.git
cd my_movie_web

# 2. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies (if first time)
pip install Flask==2.3.3 Flask-CORS==4.0.0

# 4. Start the server
python app/app.py

# 5. Open in browser
# Home: http://localhost:5000
# Admin: http://localhost:5000/admin
# API: http://localhost:5000/api/movies
```

---

## 🌐 Live URLs (Local)

| Page | URL |
|------|-----|
| Home Page | http://localhost:5000 |
| Admin Panel | http://localhost:5000/admin |
| API Base | http://localhost:5000/api |
| Get All Movies | http://localhost:5000/api/movies |
| Filter by Language | http://localhost:5000/api/movies?language=marathi |
| Get Movie #1 | http://localhost:5000/api/movies/1 |

---

## 📁 Key Files

| File | Purpose | Lines |
|------|---------|-------|
| `app/app.py` | Flask server + 7 API endpoints | 160 |
| `app/templates/index.html` | Complete UI (HTML/CSS/JS) | 550+ |
| `.gitignore` | Git configuration | 25 |

---

## 🔌 API Endpoints (7 Total)

```
GET    /api/movies                 ← Get all movies
GET    /api/movies?language=hindi  ← Filter by language
GET    /api/movies/1               ← Get movie by ID
POST   /api/movies                 ← Create new movie
PUT    /api/movies/1               ← Update movie
DELETE /api/movies/1               ← Delete movie
```

### Sample POST Request

```json
POST /api/movies
{
  "title": "Movie Name",
  "language": "marathi",
  "url": "https://youtube.com/embed/...",
  "image_url": "https://example.com/image.jpg",
  "release_date": "2025-01-15"
}
```

---

## 🎯 Features at a Glance

- ✅ **Home Page**: Browse all movies
- ✅ **Language Filter**: Marathi, Hindi, Punjabi
- ✅ **Admin Panel**: Add/Edit/Delete movies
- ✅ **Responsive**: Mobile, Tablet, Desktop
- ✅ **Single Server**: No backend/frontend separation
- ✅ **Full CRUD**: Create, Read, Update, Delete operations

---

## 🔧 Common Commands

```powershell
# Activate environment
.\.venv\Scripts\Activate.ps1

# Deactivate environment
deactivate

# Run server
python app/app.py

# Install packages
pip install Flask Flask-CORS

# Check what's running on port 5000
netstat -ano | findstr :5000

# Kill process on port 5000
taskkill /PID <PID> /F

# Git status
git status

# Git push
git push origin main

# Git pull latest
git pull origin main
```

---

## 📱 Responsive Breakpoints

- **Mobile**: 480px and below (1 column)
- **Tablet**: 768px (2 columns)
- **Desktop**: 1920px+ (3 columns)

---

## 🎨 Design Colors

| Purpose | Color | Hex |
|---------|-------|-----|
| Dark Background | Dark Gray | #0f0f0f |
| Card Background | Lighter Gray | #1a1a1a |
| Accent (Red) | Bright Red | #ff6b6b |
| Secondary (Teal) | Teal | #4ecdc4 |
| Text | White | #ffffff |

---

## 📊 Pre-loaded Sample Movies

1. **Natrang** (Marathi)
   - ID: 1
   - Date: 2023-01-15

2. **Laal Singh Chaddha** (Hindi)
   - ID: 2
   - Date: 2023-02-20

3. **Sardar Udham** (Punjabi)
   - ID: 3
   - Date: 2023-03-10

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 in use | `taskkill /PID <PID> /F` then restart |
| Movies not loading | Check `/api/movies` in browser |
| 404 errors | Verify URLs (root `/`, `/admin`, `/api/movies`) |
| Python not found | Check virtual environment is activated |
| CORS errors | Check browser console (F12) for details |

---

## 📚 Documentation

- **README.md** - Project overview
- **UNIFIED_DEPLOYMENT_GUIDE.md** - Detailed setup
- **API_DOCUMENTATION.md** - API reference
- **QUICK_REFERENCE.md** - Common tips
- **PROJECT_COMPLETION_REPORT.md** - Full details

---

## 🚀 Deployment Options

1. **PythonAnywhere** - Easy Python hosting
2. **Render** - Modern cloud platform
3. **Railway** - Simple deployment
4. **GitHub Pages** - Static site only (no backend)

See UNIFIED_DEPLOYMENT_GUIDE.md for details.

---

## 💡 Pro Tips

1. **Hot Reload Enabled**: Server restarts on code changes
2. **No Build Required**: Changes take effect immediately
3. **CORS Enabled**: Can call API from any origin
4. **Debug Mode On**: Detailed error messages in terminal
5. **Sample Data**: Pre-loaded on startup, resets on restart

---

## 🔗 Repository

- **GitHub**: https://github.com/Rahulb87/my_movie_web
- **Branch**: main
- **Issues**: https://github.com/Rahulb87/my_movie_web/issues

---

## 📞 Quick Contact

**Project**: CineHub 🎬  
**Brand**: Rahul Corp ™  
**Version**: 2.0 (Unified Server)  
**Status**: ✅ Complete & Deployed  

---

**Last Updated**: January 2025  
**Server Status**: ✅ Running on http://localhost:5000
