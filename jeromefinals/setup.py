#!/usr/bin/env python
"""
Setup script for JeromeFinals Portfolio Project
Run: python setup.py
"""

import os
import sys

def create_directories():
    """Create necessary directories"""
    directories = [
        'static/css',
        'myapp/templates/myapp',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def create_requirements():
    """Create requirements.txt"""
    with open('requirements.txt', 'w') as f:
        f.write("Django==4.2.0\n")
    print("✓ Created requirements.txt")

def create_readme():
    """Create README.md"""
    with open('README.md', 'w') as f:
        f.write("""# JeromeFinals Portfolio

A monochrome Django portfolio project with no database.

## Installation

1. Install requirements:
```bash
pip install -r requirements.txt