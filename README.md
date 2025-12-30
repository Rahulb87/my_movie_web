# Movie Website - Full Stack Application

A modern, responsive movie website built with React.js and Python Flask. Manage movies in multiple languages (Marathi, Hindi, and Punjabi) with an intuitive admin panel.

## 🎬 Features

- **Home Page**: Display latest movies with language filtering (Marathi, Hindi, Punjabi)
- **Responsive Design**: Mobile-friendly UI that works on all devices
- **Admin Panel**: Manage movies (Add, Edit, Delete) with ease
- **Language Support**: Filter movies by language
- **Modern UI**: Beautiful gradient designs with smooth animations
- **Branding**: Rahul Corp logo in footer with professional styling

## 📋 Project Structure

```
my_movie_web/
├── backend/
│   ├── app.py              # Flask application with API routes
│   ├── models/
│   │   └── movie.py        # Movie data model
│   ├── routes/             # API route handlers
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/
│   │   └── index.html      # Main HTML file
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── Navbar.js
│   │   │   ├── Footer.js
│   │   │   ├── MovieCard.js
│   │   │   └── MovieForm.js
│   │   ├── pages/          # Page components
│   │   │   ├── Home.js
│   │   │   └── Admin.js
│   │   ├── styles/         # CSS files
│   │   │   ├── global.css
│   │   │   ├── navbar.css
│   │   │   ├── footer.css
│   │   │   ├── moviecard.css
│   │   │   ├── movieform.css
│   │   │   ├── home.css
│   │   │   └── admin.css
│   │   ├── utils/
│   │   │   └── api.js      # API service
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── .env
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the frontend directory:
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
- Form validation

## 🎨 Design Features

### Responsive Design
- Mobile-first approach
- Breakpoints for tablets (768px) and mobile (480px)
- Flexible grid layouts
- Touch-friendly buttons

### Color Scheme
- Primary: Dark (#0f0f0f, #1a1a1a)
- Accent: Red (#ff6b6b)
- Secondary: Teal (#4ecdc4)

### Typography
- Modern sans-serif fonts
- Gradient text effects
- Clear hierarchy

## 📡 API Endpoints

### Movies

- `GET /api/movies` - Get all movies
- `GET /api/movies?language=marathi` - Get movies by language
- `GET /api/movies/<id>` - Get specific movie
- `POST /api/movies` - Create new movie
- `PUT /api/movies/<id>` - Update movie
- `DELETE /api/movies/<id>` - Delete movie

## 🔧 Technologies Used

### Frontend
- React 18.2.0
- React Router v6
- Axios for API calls
- CSS3 with Grid and Flexbox

### Backend
- Flask 2.3.3
- Flask-CORS
- Python 3.8+

## 📝 Movie Data Model

```javascript
{
  id: number,
  title: string,
  language: 'marathi' | 'hindi' | 'punjabi',
  url: string,
  image_url: string,
  release_date: ISO string
}
```

## 🎯 Future Enhancements

- User authentication
- Movie ratings and reviews
- Search functionality
- Favorites/Watchlist
- Video streaming integration
- User profiles
- Social sharing
- Analytics dashboard

## 📄 License

© 2024 Rahul Corp. All rights reserved.

## 👨‍💻 Author

Built with ❤️ for movie enthusiasts
