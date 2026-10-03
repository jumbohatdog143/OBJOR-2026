# OBJOR-2026 Personal Portfolio

A Django-based personal portfolio website developed for the OBJOR-2026 course requirements. The project includes a public portfolio, project and technology stack management, and an administrator dashboard.

## Features

- Public personal portfolio
- Personal information, education, skills, projects, and testimonies
- Contact/inquiry form
- Dedicated administrator sign-in page
- Administrator-only dashboard
- Project management
- Technology stack management
- Project-to-technology-stack relationship
- Project links
- Django admin interface
- Custom 404 and 500 error pages

## Requirements

- Python 3.14 or compatible Python version
- Django 6.0.8
- Pillow 12.3.0

## Installation

### 1. Clone the repository

Clone the repository and enter the project directory:

    git clone <REPOSITORY_URL>
    cd OBJOR-2026

Replace <REPOSITORY_URL> with the repository URL.

### 2. Create a virtual environment

Windows PowerShell:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Configure environment variables

Create a .env file in the project root based on .env.example.

Example:

    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost

Do not commit the .env file or real secret keys to the repository.

### 5. Apply database migrations

Run the existing migrations:

    python manage.py migrate

Do not run makemigrations when setting up a fresh clone.

### 6. Create an administrator account

Create a Django superuser:

    python manage.py createsuperuser

Follow the prompts to create the administrator credentials.

### 7. Start the development server

    python manage.py runserver

Open the development site at:

    http://127.0.0.1:8000/

## Important URLs

Public portfolio:

    http://127.0.0.1:8000/

Projects:

    http://127.0.0.1:8000/projects/

Administrator sign-in:

    http://127.0.0.1:8000/admin-login/

Administrator dashboard:

    http://127.0.0.1:8000/dashboard/

Django admin:

    http://127.0.0.1:8000/admin/

## Administrator Features

Only authenticated superusers can access the administrator dashboard.

From the dashboard, the administrator can:

- View all projects
- View all technology stacks
- Add projects
- Add technology stacks
- Associate projects with an existing technology stack

New projects and technology stacks are automatically reflected in the portfolio.

## Project Creation

When adding a project, the administrator provides:

- Project Name
- Project Description
- Technology Stack
- Project Link

The technology stack is selected using radio buttons from the available technology stacks.

## Technology Stack Creation

When adding a technology stack, the administrator provides:

- Technology Stack Name

An existing technology stack can be associated with multiple projects.

## Database

The project uses SQLite for local development.

The database file is intentionally excluded from Git. A fresh clone should create its database by running:

    python manage.py migrate

## Project Structure

    OBJOR-2026/
    +-- portfolio/
    ¦   +-- migrations/
    ¦   +-- templates/
    ¦   +-- admin.py
    ¦   +-- forms.py
    ¦   +-- models.py
    ¦   +-- urls.py
    ¦   +-- views.py
    +-- portfolio_project/
    ¦   +-- settings.py
    ¦   +-- urls.py
    ¦   +-- asgi.py
    ¦   +-- wsgi.py
    +-- manage.py
    +-- requirements.txt
    +-- .env.example
    +-- README.md

## Deployment

The project is prepared for deployment using PythonAnywhere.

Before deployment:

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies from equirements.txt.
4. Configure the environment variables.
5. Run python manage.py migrate.
6. Configure the PythonAnywhere web application to use the project's WSGI application.
7. Configure static and media files as required.
8. Test all public and administrator functions after deployment.

## Git Workflow

Development is performed on a separate feature branch. Changes are committed to the feature branch and merged into the main branch through a Pull Request.

Direct pushes to the main branch are avoided.

## Author

Khalia Dela Cruz
