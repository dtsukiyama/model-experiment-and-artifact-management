#!/bin/bash

# Exit script on any error
set -e

echo "Setting up Lefthook..."

# Check if Homebrew is installed
if ! command -v brew >/dev/null 2>&1; then
    echo "Error: Homebrew is not installed. Please install Homebrew first."
    exit 1
fi

# Step 1: Install Lefthook using Homebrew
echo "Installing Lefthook using Homebrew..."
brew install lefthook

# Step 2: Initialize Lefthook in the current Git repository
echo "Initializing Lefthook in the Git repository..."
lefthook install

echo "Lefthook setup is complete!"
