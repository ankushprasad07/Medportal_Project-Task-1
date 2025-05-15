# Medportal Project - User Signup and Login Application

## Overview
This is a Django-based web application that enables signup and login for different types of users: **Patients** and **Doctors**.  
After login, users are redirected to their respective dashboards showing their profile information entered during registration.

---

## Features
- User registration with fields:
  - First Name
  - Last Name
  - Profile Picture
  - Username
  - Email
  - Password + Confirm Password (validation included)
  - Address (Line1, City, State, Pincode)
  - User type (Patient or Doctor)

- Login functionality with validation
- Redirect to user-specific dashboards after login
- Logout functionality
- Responsive and modern UI styled with Tailwind CSS

---

## Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning the repo)
- Virtualenv (recommended)

---

## Setup Instructions

1. **Clone the repository (if applicable):**

   git clone https://github.com/ankushprasad07/Medportal_Project-Task-1
   cd Medportal_Project-Task-1

Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Run the development server:

python manage.py runserver

Open the application:

Open your browser and navigate to http://127.0.0.1:8000/
You will see the homepage with options to Register or Login.

Usage
Click Register to create a new user account.
After successful registration, you can login with your credentials.
Depending on the user type, you will be redirected to either the Patient or Doctor dashboard, displaying your profile details.
Use the logout icon to securely log out.
