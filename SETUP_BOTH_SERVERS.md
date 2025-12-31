# 🚀 Setup Guide: Running Both Servers for Development

## Overview

For local development with persistent `movies.json` file updates, you need **BOTH** servers running:

| Server | Port | Purpose |
|--------|------|---------|
| **Flask** | 5000 | Backend API - Saves to movies.json |
| **Node.js** | 3000 | Frontend UI - User interface |

---

## 🔧 Setup Instructions

### 1. Start Flask Backend Server (Port 5000)

**Terminal 1:**
```bash
cd c:\Users\Rahul_win10\Documents\My_projects\my_movie_web
.venv\Scripts\python.exe app/app.py
```

**Expected Output:**
```
✅ Loaded 3 movies from C:\...\docs\movies.json
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### 2. Start Node.js Frontend Server (Port 3000)

**Terminal 2:**
```bash
cd c:\Users\Rahul_win10\Documents\My_projects\my_movie_web\frontend
npm start
```

**Expected Output:**
```
npm start v8.x.x
Compiled successfully!
You can now view the app in the browser.
  http://localhost:3000
```

---

## ✅ Testing the Integration

### Step 1: Open Browser

Visit: **http://localhost:3000**

### Step 2: Go to Admin Panel

Click **Admin** in navbar

### Step 3: Add a Movie

1. Click **+ Add New Movie**
2. Fill in form:
   - Title: "Test Movie"
   - Language: Hindi
   - URL: (optional)
   - Image URL: (optional)
   - Release Date: Today
3. Click **Add Movie**

### Step 4: Verify

**In Browser Console (F12):**
- Should show network request to: `http://localhost:5000/api/movies`
- Status should be: 201 (Created)

**Check movies.json File:**
```bash
# Open the file
code docs/movies.json

# Or check with git
git diff docs/movies.json
```

**Expected:** New movie should appear in movies.json! ✅

---

## 🔄 Data Flow

```
User on localhost:3000
    ↓
Clicks "Add Movie"
    ↓
Frontend sends POST to http://localhost:5000/api/movies
    ↓
Flask Backend receives request
    ↓
Updates in-memory database
    ↓
Calls save_movies_to_file()
    ↓
Writes to docs/movies.json
    ↓
Returns 201 Created response
    ↓
Frontend shows success message ✅
```

---

## 🐛 Troubleshooting

### Issue: "Failed to add movie" or Network Error

**Problem:** Flask backend not running or CORS issue

**Solution:**
1. Check Flask is running on port 5000:
   ```bash
   # Terminal should show: Running on http://127.0.0.1:5000
   ```

2. Check CORS is enabled in Flask (it should be):
   ```python
   # In app/app.py
   from flask_cors import CORS
   CORS(app)  # ← Should be present
   ```

3. Check frontend API URL is correct:
   ```javascript
   // In app/templates/index.html
   const API_URL = 'http://localhost:5000/api';  // ← Should be this
   ```

### Issue: "movies.json not updating"

**Check:**
1. Flask server logs show save message:
   ```
   ✅ Saved X movies to C:\...\docs\movies.json
   ```

2. Check file permissions (docs folder should be writable)

3. Close and reopen file in editor to see changes

### Issue: Port Already in Use

**Flask already running:**
```bash
# Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Node.js already running:**
```bash
# Find and kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

---

## 📁 Important Paths

```
Project Root: c:\Users\Rahul_win10\Documents\My_projects\my_movie_web

Flask Backend:
  app/
  ├── app.py                 ← Flask server (run this)
  ├── templates/
  │   └── index.html         ← Frontend template (using localhost:5000 API)
  
Frontend (Node.js):
  frontend/
  ├── package.json
  ├── src/
  ├── public/
  
Data File:
  docs/
  └── movies.json            ← Gets updated by Flask backend ✅
```

---

## 🔗 Key Configuration

### Flask Backend (app/app.py)
```python
MOVIES_JSON_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs', 'movies.json')
# Points to: docs/movies.json

CORS(app)  # Allows requests from localhost:3000
```

### Frontend (app/templates/index.html)
```javascript
const API_URL = 'http://localhost:5000/api';
// Points to Flask API on port 5000

async function addMovie(movieData) {
    const response = await fetch(`${API_URL}/movies`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(movieData)
    });
    // This calls: http://localhost:5000/api/movies
}
```

---

## ✨ Features

✅ **Add Movie** - Saved to docs/movies.json  
✅ **Edit Movie** - Updated in movies.json  
✅ **Delete Movie** - Removed from movies.json  
✅ **Page Refresh** - Data persists (loads from movies.json)  
✅ **Version Control** - Can commit changes to Git  
✅ **CORS Enabled** - Frontend on 3000 can call API on 5000  

---

## 📝 Summary

**To see actual file updates in docs/movies.json:**

1. ✅ Start Flask: `.venv\Scripts\python.exe app/app.py`
2. ✅ Start Node.js: `npm start` (in frontend folder)
3. ✅ Open: `http://localhost:3000`
4. ✅ Add/Edit/Delete movies
5. ✅ Check: `docs/movies.json` - File is updated! ✅

---

**Latest Commit:** cea2918 - fix: Update API URL to point to Flask backend  
**Status:** ✅ Ready for development
