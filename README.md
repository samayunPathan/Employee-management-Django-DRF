
# Employee Management System
## Overview
This project is a backend REST API for an Employee Management System built with Django and Django Rest Framework. It provides functionality for user authentication and employee management, including departments and achievements.

## Features
- User authentication (register, login, logout) using JWT tokens
- CRUD operations for Employees
- CRUD operations for Departments
- CRUD operations for Achievements
- Associating Achievements with Employees

## Tech Stack
```
Python 3.x+
Django 
Django Rest Framework 
djangorestframework-simplejwt 
```
## Project Structure
```
employee_management/
│
├── employee_management/    # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py
│
├── user/                  # User authentication app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Custom User model
│   ├── serializers.py      # User serializers
│   ├── urls.py             # Authentication URLs
│   └── views.py            # Authentication views
│
├── employee/              # Employee management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Employee, Department, Achievement models
│   ├── serializers.py      # Serializers for employee-related models
│   ├── urls.py             # Employee management URLs
│   └── views.py            # Employee management views
│
├── manage.py
└── README.md
```
## Installation

#### Clone the repository:
```bash
https://github.com/samayunPathan/Employee-management-Django-DRF
cd Employee-management-Django-DRF
```

#### Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
#### Install the required packages:
```bash
pip install -r requirements.txt
```
#### Apply the migrations:
```bash
python manage.py migrate
```
#### Create a superuser:
```bash
python manage.py createsuperuser
```
#### Run the development server:
```bash
python manage.py runserver
```


## API Endpoints
### Authentication
```
Register: POST /api/users/register/
Login: POST /api/users/login/
Logout: POST /api/users/logout/
Refresh Token: POST /api/users/login/refresh/
```
### Employee Management
```
Employees: api/employees/
Departments: api/departments/
Achievements: api/achievements/
Employee Achievements: api/employee-achievements/
```
### All employee management endpoints support CRUD operations (GET, POST, PUT, DELETE).
Usage

#### Register a new user:

- POST /api/user/register/
```bash
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

#### Login to get the access token:
- POST /api/user/login/
```bash
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

Use the access token in the Authorization header for subsequent requests:
``Authorization: Bearer <your_access_token>``

Create, retrieve, update, or delete resources using the appropriate endpoints and HTTP methods.

## Testing
To run the test suite:
```bash
python manage.py test
```


