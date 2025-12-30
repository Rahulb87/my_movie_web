#!/bin/bash

# Movie Website - Quick Start Script

echo "==========================================="
echo "     Movie Website - Quick Start"
echo "==========================================="
echo ""

# Check if running from correct directory
if [ ! -d "backend" ]; then
    echo "Error: Please run this script from the project root directory"
    exit 1
fi

echo "[1/4] Setting up Backend..."
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing backend dependencies..."
pip install -q -r requirements.txt

echo "Backend setup complete!"
echo ""

echo "[2/4] Setting up Frontend..."
cd ../frontend

echo "Installing frontend dependencies..."
npm install

echo "Frontend setup complete!"
echo ""

echo "==========================================="
echo "     Setup Complete!"
echo "==========================================="
echo ""
echo "To start the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  1. cd backend"
echo "  2. source venv/bin/activate"
echo "  3. python app.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  1. cd frontend"
echo "  2. npm start"
echo ""
echo "The application will open at: http://localhost:3000"
echo ""
