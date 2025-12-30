# Installation & Setup Guide

## Quick Start (Windows)

### Step 1: Install Python & Node.js

**Python:**
- Download from https://www.python.org/downloads/
- Ensure "Add Python to PATH" is checked during installation
- Verify: Open PowerShell and run `python --version`

**Node.js:**
- Download from https://nodejs.org/ (LTS version recommended)
- Verify: Open PowerShell and run `node --version` and `npm --version`

### Step 2: Backend Setup

1. Open PowerShell and navigate to the project:
```powershell
cd "c:\Users\Rahul_win10\Documents\My_projects\my_movie_web\backend"
```

2. Create a virtual environment:
```powershell
python -m venv venv
```

3. Activate the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

4. Install dependencies:
```powershell
pip install -r requirements.txt
```

5. Run the Flask server:
```powershell
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

**Keep this terminal open!**

### Step 3: Frontend Setup

1. Open a new PowerShell window and navigate to frontend:
```powershell
cd "c:\Users\Rahul_win10\Documents\My_projects\my_movie_web\frontend"
```

2. Install dependencies:
```powershell
npm install
```

3. Start the React development server:
```powershell
npm start
```

The browser should automatically open to `http://localhost:3000`

## 🎯 Testing the Application

### Home Page
1. Visit `http://localhost:3000`
2. You should see the hero section with "Welcome to CineHub"
3. Sample movies should be displayed in a grid
4. Click on the "Movies" dropdown to filter by language

### Admin Panel
1. Navigate to `http://localhost:3000/admin`
2. Click "+ Add New Movie" button
3. Fill in the form and click "Add Movie"
4. The new movie should appear in the grid
5. Click "Edit" to modify or "Delete" to remove movies

## 📝 Sample Movie Data

The backend comes pre-loaded with sample movies:

**Marathi:**
- Natrang

**Hindi:**
- Laal Singh Chaddha

**Punjabi:**
- Sardar Udham

## 🔧 Troubleshooting

### Issue: "Module not found" in Python
**Solution:** Ensure virtual environment is activated and requirements are installed
```powershell
pip install -r requirements.txt
```

### Issue: CORS error in browser console
**Solution:** Ensure backend is running on port 5000 and frontend API URL is correct

### Issue: Port already in use
**Solution:** Change port in `app.py` (Backend) or `.env` file (Frontend)

### Issue: npm install fails
**Solution:** Clear npm cache and retry
```powershell
npm cache clean --force
npm install
```

## 📦 Adding More Movies

### Via Admin Panel (GUI)
1. Go to `/admin`
2. Click "Add New Movie"
3. Fill all fields
4. Submit

### Via API (Using Postman or curl)
```bash
POST http://localhost:5000/api/movies
Content-Type: application/json

{
  "title": "Movie Title",
  "language": "marathi",
  "url": "https://link-to-movie.com",
  "image_url": "https://link-to-poster.jpg",
  "release_date": "2024-01-15"
}
```

## 🚀 Deployment (Future)

For production deployment:

**Backend (Python):**
- Use Gunicorn instead of Flask dev server
- Deploy to Heroku, AWS, or DigitalOcean
- Use PostgreSQL instead of in-memory storage

**Frontend (React):**
- Build for production: `npm run build`
- Deploy to Vercel, Netlify, or AWS S3
- Update API URL in .env for production

## 📱 Responsive Testing

Test on different screen sizes:
- Desktop: 1920x1080+
- Tablet: 768px width
- Mobile: 480px width

Use Chrome DevTools (F12) to test responsiveness.

## ✅ Features Checklist

- [x] Home page with latest movies
- [x] Responsive design (mobile, tablet, desktop)
- [x] Language filtering (Marathi, Hindi, Punjabi)
- [x] Admin panel for CRUD operations
- [x] Professional logo and branding
- [x] Rahul Corp footer branding
- [x] Modern UI with gradient designs
- [x] API integration
- [x] Form validation
- [x] Smooth animations and transitions

## 📞 Support

For issues or questions, refer to the main README.md in the project root.
