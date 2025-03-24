# WhatBytes Healthcare Backend

This project is a backend system for a healthcare application built using Django and Django REST Framework (DRF). It manages patient and doctor records securely, handles user authentication via JWT, and allows for mapping patients to doctors. Data is stored in a PostgreSQL database, and sensitive configurations are managed with environment variables.

## Table of Contents

- [Features](#features)
- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Features

- **User Authentication:**  
  - User registration and login using JWT for secure authentication.
- **Patient Management:**  
  - Create, read, update, and delete patient records.
- **Doctor Management:**  
  - Create, read, update, and delete doctor records.
- **Patient-Doctor Mapping:**  
  - Assign doctors to patients and manage these mappings.
- **Security:**  
  - Sensitive data is handled using environment variables.
  - Endpoints are secured with proper permissions.

## Project Overview

The backend is developed using Django and Django REST Framework, with PostgreSQL as the database. It implements RESTful APIs for:

- **Authentication:**  
  - `POST /api/auth/register/` – Register a new user (requires name, email, and password).
  - `POST /api/auth/login/` – Log in a user and receive JWT tokens.
- **Patient Management:**  
  - `POST /api/patients/` – Create a new patient (authenticated users only).
  - `GET /api/patients/` – Retrieve patients associated with the authenticated user.
  - `GET /api/patients/<id>/` – Get details of a specific patient.
  - `PUT /api/patients/<id>/` – Update patient details.
  - `DELETE /api/patients/<id>/` – Delete a patient record.
- **Doctor Management:**  
  - `POST /api/doctors/` – Create a new doctor (authenticated users only).
  - `GET /api/doctors/` – Retrieve all doctors.
  - `GET /api/doctors/<id>/` – Get details of a specific doctor.
  - `PUT /api/doctors/<id>/` – Update doctor details.
  - `DELETE /api/doctors/<id>/` – Delete a doctor record.
- **Patient-Doctor Mapping:**  
  - `POST /api/mappings/` – Assign a doctor to a patient.
  - `GET /api/mappings/` – Retrieve all mappings.
  - `GET /api/mappings/<patient_id>/` – Get doctors assigned to a specific patient.
  - `DELETE /api/mappings/<id>/` – Remove a doctor from a patient.

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Mindlord-rex/whatbytes_healthcare.git
   cd whatbytes_healthcare
2.  **Create a Virtual Environment and Activate It:**
    
    bash
    
    CopyEdit
    
    `python -m venv env source env/bin/activate  # On Windows use: env\Scripts\activate`
    
3.  **Install Dependencies:**
    
    bash
    
    CopyEdit
    
    `pip install -r requirements.txt`
    
4.  **Database Setup:**
    
    Ensure PostgreSQL is installed and running. Create a new database (e.g., `healthcare_db`) and a dedicated user (e.g., `healthcare_user`).
    
5.  **Apply Migrations:**
    
    bash
    
    CopyEdit
    
    `python manage.py makemigrations python manage.py migrate`
    
6.  **Create a Superuser (Optional):**
    
    bash
    
    CopyEdit
    
    `python manage.py createsuperuser`
    
7.  **Start the Development Server:**
    
    bash
    
    CopyEdit
    
    `python manage.py runserver`
    

## Configuration

Create a `.env` file in the project root (based on the provided `.env.example`) and configure your settings:

ini

CopyEdit

`DB_NAME=healthcare_db DB_USER=healthcare_user DB_PASSWORD=your_secure_password DB_HOST=localhost DB_PORT=5432 SECRET_KEY=your_secret_key`

## API Endpoints

The backend exposes several RESTful endpoints:

*   **Authentication:**
    
    *   `POST /api/auth/register/`
        
    *   `POST /api/auth/login/`
        
*   **Patient Management:**
    
    *   `POST /api/patients/`
        
    *   `GET /api/patients/`
        
    *   `GET /api/patients/<id>/`
        
    *   `PUT /api/patients/<id>/`
        
    *   `DELETE /api/patients/<id>/`
        
*   **Doctor Management:**
    
    *   `POST /api/doctors/`
        
    *   `GET /api/doctors/`
        
    *   `GET /api/doctors/<id>/`
        
    *   `PUT /api/doctors/<id>/`
        
    *   `DELETE /api/doctors/<id>/`
        
*   **Patient-Doctor Mapping:**
    
    *   `POST /api/mappings/`
        
    *   `GET /api/mappings/`
        
    *   `GET /api/mappings/<patient_id>/`
        
    *   `DELETE /api/mappings/<id>/`
        

All endpoints (except registration and login) are secured and require JWT authentication.

## Testing

After starting the development server, you can test the API endpoints using any HTTP client (such as cURL or your preferred API testing tool):

*   **Register a User:**
    
    bash
    
    CopyEdit
    
    `curl -X POST http://127.0.0.1:8000/api/auth/register/ \      -H "Content-Type: application/json" \      -d '{            "email": "example@example.com",            "name": "John Doe",            "password": "YourPassword123!"          }'`
    
*   **Login a User:**
    
    bash
    
    CopyEdit
    
    `curl -X POST http://127.0.0.1:8000/api/auth/login/ \      -H "Content-Type: application/json" \      -d '{            "email": "example@example.com",            "password": "YourPassword123!"          }'`
    

On successful login, you will receive a JWT token which must be included in the `Authorization` header for all subsequent authenticated requests.
