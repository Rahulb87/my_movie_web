import React from 'react';
import '../styles/footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>About</h3>
            <p>Your ultimate movie destination for Marathi, Hindi, and Punjabi films.</p>
          </div>
          
          <div className="footer-section">
            <h3>Quick Links</h3>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/admin">Admin Panel</a></li>
              <li><a href="/">Browse Movies</a></li>
            </ul>
          </div>

          <div className="footer-section">
            <h3>Follow Us</h3>
            <div className="social-links">
              <a href="#facebook">Facebook</a>
              <a href="#twitter">Twitter</a>
              <a href="#instagram">Instagram</a>
            </div>
          </div>
        </div>
        
        <div className="footer-bottom">
          <div className="logo-section">
            <span className="footer-logo">🏢</span>
            <p>&copy; 2024 Rahul Corp. All rights reserved.</p>
          </div>
          <p>CineHub &trade; - Your Entertainment Platform</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
