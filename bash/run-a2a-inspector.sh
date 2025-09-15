#!/bin/bash

# A2A Inspector Setup and Run Script
# This script handles both initial setup and running the a2a-inspector tool

set -e  # Exit on any error

echo "🚀 A2A Inspector Setup and Run..."

# Check if a2a-inspector directory already exists
if [ -d "a2a-inspector" ]; then
    echo "📁 a2a-inspector directory already exists, updating..."
    cd a2a-inspector
    git pull
else
    echo "📥 Cloning a2a-inspector repository..."
    git clone https://github.com/a2aproject/a2a-inspector.git
    cd a2a-inspector
    
    echo "🔧 Setting up Python dependencies with uv..."
    # Run from the root of the project
    uv sync

    echo "📦 Installing frontend dependencies..."
    # Navigate to the frontend directory
    cd frontend

    # Install npm packages
    npm install

    echo "🔙 Going back to root directory..."
    # Go back to the root directory
    cd ..
fi

echo "🔧 Making run script executable..."
# Make the script executable (first time only)
chmod +x scripts/run.sh

echo "🎯 Starting A2A Inspector (frontend and backend)..."
# Run both frontend and backend with a single command
bash scripts/run.sh
