# FileNest – Smart File Management System

## Overview

**FileNest** is a beginner-level Django web application for managing files and folders. Users can upload, organize, edit, share, download, preview, and delete files.

## Features

* User registration and login
* Upload multiple files
* Create and manage folders
* Create nested subfolders
* Rename, move, and delete folders
* Edit file name and description
* View file details
* Download and preview files
* Move files between folders
* Share files with other users
* View shared files
* Move deleted files to Trash
* Restore or permanently delete files
* Filter files by file type
* Sort files by name and upload time
* Display storage usage
* Generate AI-based summaries for PDF files
* Save the summary using the browser's **Print → Save as PDF**
* Responsive user interface

## Technologies Used

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Django
* **Database:** SQLite
* **Authentication:** Django Authentication
* **File Storage:** Django FileField
* **AI:** Google Gemini API

## Django Apps

account      → User registration and login
files        → File upload and management
folders      → Folder and subfolder management
filesharing  → File sharing
trash        → Deleted file management


## Project Structure

FileNest/
│
├── account/
├── files/
├── folders/
├── filesharing/
├── trash/
├── templates/
├── media/
├── manage.py
└── db.sqlite3

## Installation

Install Django: pip install django 
                pip install django google-genai

Run migrations: python manage.py migrate

Start the server: python manage.py runserver

Open: http://127.0.0.1:8000/


## Gemini API

The AI summary feature requires a Gemini API key in Django settings:

GEMINI_API_KEY = "your-api-key"

## Main Workflow

Login
  ↓
FileNest Dashboard
  ↓
Upload Files
  ↓
Create Folders
  ↓
Organize Files
  ↓
Edit / Move / Share / Preview
  ↓
Trash
  ↓
Restore or Permanently Delete

## Purpose

FileNest was developed as a **beginner-level Django project** to demonstrate Django models, forms, views, templates, authentication, CRUD operations, file handling, folder management, file sharing, and basic API/AI integration.
