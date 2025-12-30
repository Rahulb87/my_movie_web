import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './styles/global.css';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Admin from './pages/Admin';

function App() {
  const [selectedLanguage, setSelectedLanguage] = useState(null);

  const handleLanguageFilter = (language) => {
    setSelectedLanguage(language);
  };

  return (
    <Router>
      <div className="app">
        <Navbar onLanguageFilter={handleLanguageFilter} />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/admin" element={<Admin />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
