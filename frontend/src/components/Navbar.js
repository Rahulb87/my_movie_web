import React from 'react';
import '../styles/navbar.css';

const Navbar = ({ onLanguageFilter }) => {
  return (
    <nav className="navbar">
      <div className="container">
        <div className="navbar-content">
          <div className="logo">
            <span className="logo-icon">🎬</span>
            <span className="logo-text">CineHub</span>
          </div>
          
          <ul className="nav-menu">
            <li><a href="/">Home</a></li>
            <li className="dropdown">
              <button className="dropdown-btn">Movies</button>
              <div className="dropdown-content">
                <a onClick={() => onLanguageFilter('marathi')} href="#marathi">
                  🎭 Marathi
                </a>
                <a onClick={() => onLanguageFilter('hindi')} href="#hindi">
                  🎬 Hindi
                </a>
                <a onClick={() => onLanguageFilter('punjabi')} href="#punjabi">
                  🎪 Punjabi
                </a>
                <a onClick={() => onLanguageFilter(null)} href="#all">
                  📽️ All Movies
                </a>
              </div>
            </li>
            <li><a href="/admin">Admin</a></li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
