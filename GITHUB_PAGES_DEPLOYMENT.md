# 🚀 GitHub Pages Deployment Guide - CineHub

## Overview

This guide explains how to deploy CineHub to GitHub Pages as a **static website** with proper routing and base path handling.

---

## 📋 Key Concepts for GitHub Pages Deployment

### The Problem
When you deploy to GitHub Pages, your site is served from a **subdirectory**, not the root:
- **Local**: `http://localhost:5000/`
- **GitHub Pages**: `https://Rahulb87.github.io/my_movie_web/`

This means all asset paths and API calls need to account for the `/my_movie_web/` base path.

### The Solution
The `docs/index.html` file includes:
1. **Dynamic base path detection** - Automatically determines if running locally or on GitHub Pages
2. **URL history management** - Proper routing without server-side rewrites
3. **Relative API paths** - Adjusts API endpoint paths based on base path

---

## 🔧 How It Works

### Base Path Detection
```javascript
function getBasePath() {
    const pathname = window.location.pathname;
    if (pathname.includes('my_movie_web')) {
        return '/my_movie_web/';
    }
    return '/';
}
```

- **Local** (`http://localhost:5000/`): Returns `/`
- **GitHub Pages** (`https://Rahulb87.github.io/my_movie_web/`): Returns `/my_movie_web/`

### URL Routing
Navigation is handled entirely on the client-side:
```javascript
function navigateTo(page) {
    if (page === 'home') {
        window.history.pushState({page: 'home'}, 'Home', BASE_PATH);
    } else if (page === 'admin') {
        window.history.pushState({page: 'admin'}, 'Admin', BASE_PATH + 'admin');
    }
    renderPage();
}
```

---

## 📁 File Structure for GitHub Pages

```
my_movie_web/
├── docs/                          ← GitHub Pages source folder
│   ├── index.html                 ← Single page app (handles all routes)
│   └── .nojekyll                  ← Tells GitHub not to use Jekyll
├── app/
│   ├── app.py                     ← Flask server (local development)
│   └── templates/index.html       ← Flask template (local development)
└── [other files...]
```

---

## 🚀 Deployment Steps

### Step 1: GitHub Repository Setup

1. Go to your repository: https://github.com/Rahulb87/my_movie_web
2. Go to **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Set to "Deploy from a branch"
   - **Branch**: Select `main` and `/docs` folder
   - Click **Save**

### Step 2: Verify Deployment

GitHub will automatically build and deploy. You should see:
- ✅ Environment: "github-pages" 
- ✅ Status: "Active"
- ✅ URL: `https://Rahulb87.github.io/my_movie_web/`

### Step 3: Test the Site

Visit: **https://Rahulb87.github.io/my_movie_web/**

Expected behavior:
- ✅ Home page loads with movie grid
- ✅ Language filtering works
- ✅ Admin panel is accessible
- ✅ Navigation between pages works
- ✅ All styling and animations display correctly

---

## 🔌 API Considerations

### Important Note
The current `docs/index.html` is a **static-only version** with hardcoded sample data. It does NOT connect to a backend API.

To enable API functionality with a backend server:

### Option 1: Flask Backend + GitHub Pages Frontend

1. **Deploy Flask separately** to:
   - PythonAnywhere
   - Render.com
   - Railway.app
   - Heroku

2. **Update API_URL** in `docs/index.html`:
   ```javascript
   const API_URL = 'https://your-deployed-flask-server.com/api';
   ```

3. **Enable CORS** on your backend (already enabled in `app/app.py`)

### Option 2: Pure Static Site (Current)

The `docs/index.html` works as a **demo site** with built-in sample movies:
- **Natrang** (Marathi)
- **Laal Singh Chaddha** (Hindi)
- **Sardar Udham** (Punjabi)

Users can add/edit/delete in the admin panel, but data resets on page reload (no persistence).

---

## 🌐 Accessing Your Site

### URLs

| Page | GitHub Pages URL |
|------|------------------|
| **Home** | `https://Rahulb87.github.io/my_movie_web/` |
| **Admin** | `https://Rahulb87.github.io/my_movie_web/admin` |

### Local Development

Still works the same way:
```powershell
cd c:\Users\Rahul_win10\Documents\My_projects\my_movie_web
python app/app.py
# Visit: http://localhost:5000
```

---

## ✅ Verification Checklist

- [ ] GitHub Pages enabled in repository settings
- [ ] Source set to "main" branch / "/docs" folder
- [ ] `.nojekyll` file exists in docs folder
- [ ] `docs/index.html` is the main file
- [ ] Site is live at `https://Rahulb87.github.io/my_movie_web/`
- [ ] Home page loads on first visit
- [ ] Navigation works (home ↔ admin)
- [ ] Language filtering works
- [ ] Admin CRUD operations work (demo data)
- [ ] Responsive design looks good on mobile

---

## 🐛 Troubleshooting

### Issue: 404 Error on GitHub Pages

**Solution:**
1. Check that `/docs` folder is set in GitHub Pages settings
2. Verify `index.html` exists in `/docs` folder
3. Wait 5 minutes for GitHub to redeploy after changes

### Issue: Static Assets Not Loading

**Solution:**
1. All CSS is inline in `index.html` (no external files)
2. No external dependencies needed
3. Everything is self-contained

### Issue: Navigation Not Working

**Solution:**
1. Check browser console for JavaScript errors (F12)
2. Verify you're using the correct GitHub Pages URL
3. Clear browser cache and refresh

### Issue: Admin Form Not Saving

**Solution:**
This is expected behavior for the static demo:
- Admin form works and shows success messages
- But data doesn't persist (no backend connection)
- To enable persistence, deploy Flask backend separately

---

## 🔄 Updating Deployed Site

### To update `docs/index.html`:

```powershell
# Edit the file
# Then push to GitHub
git add docs/
git commit -m "Update CineHub deployment"
git push origin main
```

GitHub Pages will redeploy automatically (usually within 30 seconds).

---

## 🎯 Production Deployment with Backend

For a **production-grade** deployment with data persistence:

### Architecture
```
GitHub Pages (Frontend)
     ↓ (API calls)
Flask Backend (Your choice of host)
     ↓ (Data)
Database
```

### Step-by-Step:

1. **Deploy Flask to PythonAnywhere** (or Render/Railway):
   ```bash
   # Create account at pythonanywhere.com
   # Upload app.py and requirements.txt
   # Configure Flask web app
   # Get endpoint: https://yourname.pythonanywhere.com
   ```

2. **Update `docs/index.html`** API endpoint:
   ```javascript
   // Replace this line:
   const API_URL = BASE_PATH + 'api';
   
   // With this:
   const API_URL = 'https://yourname.pythonanywhere.com/api';
   ```

3. **Push to GitHub**:
   ```powershell
   git add docs/index.html
   git commit -m "Connect to backend API"
   git push origin main
   ```

4. **Test**:
   - Visit your GitHub Pages site
   - Admin panel should now save to backend
   - Data persists across page reloads

---

## 📊 Features Comparison

| Feature | Local Dev | GitHub Pages (Current) | GitHub Pages + Backend |
|---------|-----------|----------------------|----------------------|
| Home page | ✅ | ✅ | ✅ |
| Admin panel | ✅ | ✅ | ✅ |
| Language filtering | ✅ | ✅ | ✅ |
| CRUD operations | ✅ (REST API) | ✅ (demo only) | ✅ (persisted) |
| Data persistence | ✅ (memory) | ❌ (demo data) | ✅ (database) |
| Responsive design | ✅ | ✅ | ✅ |

---

## 🔐 Security Notes

- **Static site**: No server-side execution, very safe
- **API deployment**: Implement authentication on your backend
- **CORS**: Already configured in Flask (`app.py`)
- **Data**: In demo mode, no personal data is stored

---

## 📞 Support

### If site isn't loading:
1. Check GitHub Pages settings in repository
2. Verify URL is correct: `https://Rahulb87.github.io/my_movie_web/`
3. Check browser console for errors (F12)
4. Try clearing cache: `Ctrl+Shift+Delete`

### If you need backend API:
1. Deploy Flask separately (see production deployment above)
2. Update API_URL in docs/index.html
3. Push changes to GitHub

---

## 🎉 Success Indicators

✅ Site loads at `https://Rahulb87.github.io/my_movie_web/`  
✅ All pages are accessible  
✅ Navigation works without page reloads  
✅ Mobile view is responsive  
✅ Dark theme displays correctly  
✅ Admin panel is functional  

---

**Your CineHub is now deployed on GitHub Pages! 🚀**

**Local development**: Still use `python app/app.py`  
**GitHub Pages**: Visit your GitHub Pages URL  
**Both** use the same code structure for maximum compatibility!
