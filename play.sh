#!/bin/bash
# Simple launcher script for the Brain Training Game

echo "🚀 Starting Brain Training Game..."
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 brain_training_game.py
elif command -v python &> /dev/null; then
    python brain_training_game.py
else
    echo "❌ Error: Python 3 is not installed!"
    echo "Please install Python 3.6 or higher to play this game."
    exit 1
fi
