# basic-cred
CRED operation using HTML+mySQL+FASTAPI

FastAPI + MySQL + HTML - CRED App
Features

- Create a new user (Name and ID)
- View all users
- Edit existing user details
- Delete user records
- Backend built with FastAPI
- MySQL for database storage
- HTML + JavaScript (AJAX) for the frontend

Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Backend     | FastAPI        |
| Frontend    | HTML + JavaScript (AJAX) |
| Database    | MySQL          |
| ORM         | SQLAlchemy     |
| Server      | Uvicorn        |


1. Create Virtual Environment - python -m venv .project1
2. Install Requirements - pip install -r requirements.txt
3. MySQL Database Setup - CREATE DATABASE tablename;
4. Update database.py
5. Run the App using command - uvicorn main:app --reload
6. Open browser at: http://127.0.0.1:8000

====================================================================================================================
cred-js: project with javascript ajax call

This project is a simple web-based CRUD (Create, Read, Update, Delete) application developed using:

FastAPI as the backend web framework, MySQL as the relational database, and HTML + JavaScript (AJAX) for the user interface.
The goal of this application is to demonstrate how you can build a fully functional, interactive web app that allows users to manage data records — specifically, storing and updating ID and usernames (or any two fields you choose).
It serves as a beginner-friendly project that connects a Python backend to a MySQL database with real-time interaction from the frontend using AJAX.

=======================================================================================================================
netflixfav: 

NetflixFav is a simple, user-friendly web application built to perform CRUD operations (Create, Read, Update, Delete) on a list of users and their favorite movies or shows. This project is designed for learning and practicing full-stack development using:
FastAPI (Backend API Framework), MySQL (Relational Database), HTML + CSS + JavaScript (AJAX) (Frontend)

Users can add their favorite content, view existing entries, update any changes, or delete records — all through a clean HTML interface powered by FastAPI endpoints.

This app can serve as a mini project or learning module for anyone exploring:
FastAPI, SQL-based data handling with MySQL

Requirements for netflixfav:
fastapi==0.116.1
uvicorn
sqlalchemy
pymysql
Jinja2==3.1.6
python-multipart

========================================================================================================================
sturegform:

The sturegform project is a web application built to perform basic CRED (Create, Read, Edit, Delete) operations for managing student records. It is designed to be a lightweight and beginner-friendly full-stack project that helps you understand how FastAPI interacts with a MySQL database using HTML forms as the frontend interface.

The application allows users to:
- Register a student by submitting a form with details such as ID and username.
- Retrieve student records using ID-based lookup.
- Update existing student information.
- Delete a student entry from the database.

The app is built using:
FastAPI — web framework for building APIs with Python.
MySQL — relational database to store and manage student records.
HTML + Jinja2 — used for rendering the frontend forms and displaying results.

Requirements for sturegform:
fastapi==0.116.1
uvicorn
sqlalchemy
pymysql
Jinja2==3.1.6
python-multipart
