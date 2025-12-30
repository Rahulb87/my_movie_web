# Quick Reference Card

## 🚀 Quick Start Commands

### Windows PowerShell
```powershell
# Terminal 1 - Backend
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py

# Terminal 2 - Frontend
cd frontend
npm install
npm start
```

### Mac/Linux Terminal
```bash
# Terminal 1 - Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

# Terminal 2 - Frontend
cd frontend
npm install
npm start
```

---

## 🔗 Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | `http://localhost:3000` | User Interface |
| Backend | `http://localhost:5000` | API Server |
| API | `http://localhost:5000/api` | API Endpoint |
| Home Page | `http://localhost:3000/` | Movie Display |
| Admin Panel | `http://localhost:3000/admin` | Movie Management |

---

## 📡 API Quick Reference

```bash
# Get all movies
curl http://localhost:5000/api/movies

# Get by language
curl "http://localhost:5000/api/movies?language=marathi"

# Create movie
curl -X POST http://localhost:5000/api/movies \
  -H "Content-Type: application/json" \
  -d '{"title":"Movie","language":"hindi","url":"link","image_url":"img"}'

# Update movie
curl -X PUT http://localhost:5000/api/movies/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"New Title"}'

# Delete movie
curl -X DELETE http://localhost:5000/api/movies/1
```

---

## 🎨 Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Reload Page | `F5` or `Ctrl+R` |
| Dev Tools | `F12` |
| Search | `Ctrl+F` |
| Home | `Ctrl+Alt+H` |

---

## 📁 Important Files

| File | What to Edit |
|------|-------------|
| `frontend/src/components/Navbar.js` | Menu items |
| `frontend/src/components/Footer.js` | Footer content |
| `frontend/src/styles/global.css` | Overall styling |
| `backend/app.py` | API logic |
| `frontend/.env.local` | API URL |

---

## 🎬 Movie Data Format

```json
{
  "title": "Movie Name",
  "language": "marathi|hindi|punjabi",
  "url": "https://example.com/movie",
  "image_url": "https://example.com/poster.jpg",
  "release_date": "2024-01-15"
}
```

---

## 🛠️ Common Fixes

| Issue | Solution |
|-------|----------|
| Port in use | Change port in `.env` |
| CORS error | Start backend first |
| Module error | Run `pip install -r requirements.txt` |
| npm error | Run `npm cache clean --force` |
| Can't connect | Check both servers running |

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 35+ |
| Backend Routes | 7 |
| Frontend Components | 6 |
| CSS Files | 7 |
| Configuration Files | 8 |
| Documentation Files | 5 |

---

## 🎯 Feature Checklist

### Frontend
- [x] Home page with hero
- [x] Movie grid display
- [x] Language filtering
- [x] Admin panel
- [x] Movie form
- [x] Responsive design
- [x] Navigation
- [x] Footer

### Backend
- [x] GET all movies
- [x] GET by language
- [x] GET by ID
- [x] POST create
- [x] PUT update
- [x] DELETE remove
- [x] Health check
- [x] CORS enabled

### Design
- [x] Modern UI
- [x] Dark theme
- [x] Gradient effects
- [x] Animations
- [x] Mobile responsive
- [x] Professional logo
- [x] Branding

---

## 📈 Next Steps

1. Start both servers
2. Test home page
3. Add sample movies
4. Test admin panel
5. Check responsive design
6. Deploy (optional)

---

## 🎓 Learning Resources

- **React**: https://react.dev
- **Flask**: https://flask.palletsprojects.com
- **REST API**: https://restfulapi.net
- **CSS**: https://developer.mozilla.org/en-US/docs/Web/CSS

---

## 💡 Tips & Tricks

- Use React DevTools browser extension for debugging
- Use Flask debugger for backend issues
- Check Network tab in DevTools for API calls
- Use `console.log()` for debugging JavaScript
- Use `print()` for debugging Python

---

## 🔐 Environment Variables

### Backend (.env)
```
FLASK_ENV=development
FLASK_APP=app.py
FLASK_DEBUG=True
```

### Frontend (.env.local)
```
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_NAME=CineHub
```

---

## 📱 Responsive Sizes

- Desktop: 1920px+
- Tablet: 768px - 1199px
- Mobile: Below 768px

---

## 🎨 Color Guide

- **Primary Action**: #ff6b6b (Red)
- **Secondary Action**: #4ecdc4 (Teal)
- **Background**: #0f0f0f (Very Dark)
- **Text**: #ffffff (White)

---

## ⏱️ Estimated Time to Complete

- Initial Setup: 5-10 minutes
- Full Testing: 10-15 minutes
- Customization: 20-30 minutes
- Deployment: 30-60 minutes

---

## 📞 Support Resources

- README.md - Main documentation
- SETUP_GUIDE.md - Installation help
- API_DOCUMENTATION.md - API reference
- STRUCTURE_GUIDE.md - Architecture details
- PROJECT_SUMMARY.md - Complete overview

---

## ✅ Pre-Launch Checklist

- [ ] Python installed
- [ ] Node.js installed
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Both servers running
- [ ] Frontend loads (localhost:3000)
- [ ] API responds (localhost:5000/api/movies)
- [ ] Movies display on home page
- [ ] Admin panel accessible
- [ ] Can add movie
- [ ] Can edit movie
- [ ] Can delete movie
- [ ] Mobile looks good
- [ ] Tablet looks good

---

**Version:** 1.0.0 | **Date:** December 30, 2024 | **Status:** ✅ Ready
