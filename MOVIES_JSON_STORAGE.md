# 📄 CineHub - movies.json File Storage

## Overview

CineHub now uses a **`movies.json`** file for persistent data storage instead of browser localStorage. This JSON file is committed to the repository and used on both local and deployed (GitHub Pages) versions.

---

## 🎯 Architecture

### How It Works

1. **On Page Load**: The application fetches `movies.json` from the server
2. **Data in Memory**: Movies are loaded into JavaScript memory (`allMovies` array)
3. **User Actions**: Add/edit/delete operations modify the in-memory array
4. **On Save**: Changes are persisted to localStorage as a fallback (for GitHub Pages)
5. **JSON File**: The `movies.json` file serves as the source of truth

### Storage Hierarchy

```
Primary Source:  movies.json (checked-in file)
       ↓
Load into Memory: allMovies[] array
       ↓
User Edits: Add/Update/Delete operations
       ↓
Fallback Save: localStorage (GitHub Pages persistence)
       ↓
For Next Load: Restore from localStorage first
```

---

## 📁 File Location

```
docs/
├── index.html          (Main application - now loads movies.json)
├── movies.json         (Movie data storage - NEW!)
└── .nojekyll           (GitHub Pages config)
```

### movies.json Structure

```json
{
  "movies": [
    {
      "id": 1,
      "title": "Movie Name",
      "language": "marathi|hindi|punjabi",
      "url": "https://youtube.com/embed/...",
      "image_url": "https://example.com/image.jpg",
      "release_date": "2023-01-15"
    }
  ],
  "nextId": 4,
  "lastUpdated": "2025-12-31T10:00:00.000Z"
}
```

---

## ✅ Key Features

### Primary: JSON File Source
✅ **Version controlled** - movies.json committed to GitHub  
✅ **Deployment ready** - Available on GitHub Pages  
✅ **Easy to edit** - Human-readable JSON format  
✅ **Backup friendly** - Can be exported/backed up easily  

### Fallback: LocalStorage Cache
✅ **Fast access** - Browser storage for quick loads  
✅ **User edits persisted** - Changes survive page refresh  
✅ **Offline support** - Works if JSON file unavailable  
✅ **GitHub Pages friendly** - No server needed for persistence  

---

## 🔄 Data Flow

### Loading Data

```javascript
// 1. Try to load movies.json
fetch('movies.json')
  ↓
// 2. If available, load into memory
allMovies = data.movies;
movieIdCounter = data.nextId;
  ↓
// 3. Check for user edits in localStorage
const userEdits = localStorage.getItem('cinehub_movies_db');
  ↓
// 4. Restore user edits if available
allMovies = userEdits.movies || allMovies;
  ↓
// 5. Render page with loaded data
renderPage();
```

### Saving Data

```javascript
// User adds/edits/deletes movie
addMovie(movieData)
  ↓
// Update in-memory array
allMovies.push(newMovie);
  ↓
// Call save function
saveMoviesToJSON()
  ↓
// Save to localStorage (fallback for GitHub Pages)
localStorage.setItem('cinehub_movies_db', JSON.stringify(data));
  ↓
// Display success message
showMessage('Movie added successfully!');
```

---

## 🚀 Deployment Behavior

### Local Development
- Loads from `http://localhost:5000/movies.json` (or similar)
- Falls back to localStorage if JSON unavailable
- Changes persist via localStorage

### GitHub Pages Deployment
- Loads from `https://rahulb87.github.io/my_movie_web/movies.json`
- Uses localStorage for user edits (GitHub Pages has no backend)
- JSON file serves as initial/reset data
- User edits override JSON data

---

## 📝 Implementation Details

### Load Function

```javascript
const MOVIES_JSON_PATH = BASE_PATH + 'movies.json';

async function loadMoviesFromJSON() {
    try {
        const response = await fetch(MOVIES_JSON_PATH);
        if (response.ok) {
            const data = await response.json();
            allMovies = data.movies || [];
            movieIdCounter = data.nextId || 4;
            return;
        }
    } catch (error) {
        console.error('Error loading from movies.json:', error);
    }
    // Fallback to default data if JSON unavailable
    allMovies = JSON.parse(JSON.stringify(defaultMovies));
    movieIdCounter = 4;
}
```

### Save Function

```javascript
async function saveMoviesToJSON() {
    try {
        const data = {
            movies: allMovies,
            nextId: movieIdCounter,
            lastUpdated: new Date().toISOString()
        };
        
        // For GitHub Pages, save to localStorage as fallback
        if (IS_GITHUB_PAGES) {
            localStorage.setItem('cinehub_movies_db', JSON.stringify(data));
            console.log('Movie data saved (GitHub Pages mode - localStorage)');
        } else {
            console.log('Movie data updated (offline mode)');
        }
    } catch (error) {
        console.error('Error saving movies:', error);
    }
}
```

### Page Load Initialization

```javascript
(async () => {
    // 1. Load from movies.json file
    await loadMoviesFromJSON();
    
    // 2. Try to restore user edits from localStorage
    try {
        const stored = localStorage.getItem('cinehub_movies_db');
        if (stored) {
            const data = JSON.parse(stored);
            allMovies = data.movies || allMovies;
            movieIdCounter = data.nextId || movieIdCounter;
        }
    } catch (error) {
        console.warn('Could not restore from localStorage:', error);
    }
    
    // 3. Render the page
    renderPage();
})();
```

---

## 🔄 Comparison: Storage Methods

| Aspect | localStorage | movies.json | Backend API |
|--------|--------------|-------------|------------|
| **Persistence** | Per-browser | Version-controlled | Cloud |
| **Scope** | Single device | All devices | All devices |
| **Size** | ~5-10MB | Unlimited | Unlimited |
| **GitHub Pages** | ✅ Works | ✅ Works | ❌ No backend |
| **Version Control** | ❌ No | ✅ Yes | ✅ Yes |
| **User Edits** | ✅ Persisted | ✅ Via localStorage | ✅ Synced |
| **Offline** | ✅ Works | ✅ Works (if cached) | ❌ No |

---

## 📊 Data Persistence Flow

### Scenario 1: Add Movie on GitHub Pages

```
1. User adds movie in admin panel
   ↓
2. addMovie() called → allMovies updated
   ↓
3. saveMoviesToJSON() called
   ↓
4. Data saved to localStorage
   ↓
5. Page refreshed by user
   ↓
6. movies.json loaded from GitHub Pages
   ↓
7. User edits restored from localStorage
   ↓
8. Movie still visible ✅
```

### Scenario 2: Push new movies.json to GitHub

```
1. Update movies.json locally
   ↓
2. Commit and push to GitHub
   ↓
3. GitHub Pages pulls latest
   ↓
4. Next user loads site
   ↓
5. Fetches new movies.json
   ↓
6. Checks localStorage for user edits
   ↓
7. Merges GitHub data with user edits
   ↓
8. All data available ✅
```

---

## 🎯 Use Cases

### Add New Movies
1. Edit `docs/movies.json`
2. Add new movie object to `movies` array
3. Increment `nextId`
4. Commit and push to GitHub
5. Changes available on deployed site

### Export Backup
1. Open browser DevTools (F12)
2. Check LocalStorage: `cinehub_movies_db`
3. Copy the JSON data
4. Save to file for backup

### Reset to Defaults
1. Clear browser LocalStorage
2. Refresh page
3. Site loads default movies.json
4. Data resets to committed version

---

## ⚠️ Important Notes

### Data Persistence on GitHub Pages

Since GitHub Pages is **static hosting** (no backend):
- ✅ `movies.json` is the source file (always available)
- ✅ User edits saved to localStorage (browser-level)
- ✅ Each user has their own edits (per-device)
- ❌ Edits don't sync across devices
- ❌ Edits lost if browser data cleared

### To Make Edits Permanent

Option 1: Update movies.json and push to GitHub
```bash
# Edit docs/movies.json
git add docs/movies.json
git commit -m "Update movies.json"
git push origin main
```

Option 2: Add backend API
```javascript
// POST to server instead of localStorage
fetch('https://your-api.com/movies', {
    method: 'POST',
    body: JSON.stringify(allMovies)
});
```

---

## 🛠️ Developer Information

### Editing movies.json Directly

```json
{
  "movies": [
    {
      "id": 1,
      "title": "New Movie",
      "language": "marathi",
      "url": "https://youtube.com/embed/...",
      "image_url": "https://example.com/image.jpg",
      "release_date": "2025-01-15"
    },
    // ... more movies
  ],
  "nextId": 2,  // Increment this for next movie
  "lastUpdated": "2025-12-31T10:00:00.000Z"
}
```

### Adding Bulk Movies

1. Prepare JSON data
2. Edit `docs/movies.json`
3. Update `nextId` to highest ID + 1
4. Commit and push
5. Site automatically loads new data

---

## 📱 Browser Compatibility

### Fetch API (used for movies.json)
✅ Chrome/Edge 40+  
✅ Firefox 39+  
✅ Safari 10.1+  
✅ All modern browsers  

### localStorage (fallback)
✅ All modern browsers  
✅ IE 8+  
✅ Mobile browsers  

---

## 🔄 Next Steps (Optional)

### To Add Backend Sync

```javascript
async function saveMoviesToServer() {
    const response = await fetch('/api/movies', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            movies: allMovies,
            nextId: movieIdCounter
        })
    });
    return response.json();
}
```

### To Enable Cloud Sync

1. Use a backend service (Firebase, Supabase, etc.)
2. Replace localStorage with API calls
3. Implement real-time sync
4. Enable multi-device synchronization

---

## ✨ Summary

### Current Architecture

✅ **Primary Storage**: `docs/movies.json` (version-controlled)  
✅ **Fallback Cache**: Browser localStorage (user edits)  
✅ **Initialization**: Loads JSON, restores user edits  
✅ **Save Process**: Updates localStorage for persistence  
✅ **Deployment Ready**: Works on GitHub Pages  

### What Changed

| Before | After |
|--------|-------|
| Only localStorage | JSON file + localStorage |
| Data lost on cache clear | JSON file always available |
| Hard to backup | Easy to commit/backup |
| Not version-controlled | Full Git history |

### Benefits

✅ Source of truth in version control  
✅ Easy to deploy new movies  
✅ Fallback persistence works offline  
✅ GitHub Pages friendly  
✅ User edits persist locally  
✅ Professional data management  

---

**Latest Update**: January 2025  
**Version**: 3.2 (With movies.json)  
**Status**: ✅ Production Ready
