## Project Management App

A simple Django-based Project Management App built for the Django Internship Task.  
It allows you to create Projects and manage Tasks under each project with full CRUD operations.

### Project Module
- Create, view, edit, delete projects  
- Fields: name, description, start_date, end_date, status (Planned / In Progress / Completed)

### Task Module
- Create, view, edit, delete tasks  
- Assign tasks to a project  
- Fields: title, description, assigned_to, due_date, status (Pending / In Progress / Done)

### Additional Features
- View all tasks under each project  
- Simple and clean HTML templates  
- SQLite3 database (default)

## Installation Guide
Follow these steps to run this Django project.

### Install Python 3.13
1. Download Python 3.13.
2. Run the installer.  
5. Verify installation Run: python --version

### Install Django 5.2.5
-Run this command: pip install Django==5.2.5

-Check the Django version: python -m django --version

### Download This Project
- Download Zip or Clone using Git.

### Install Dependencies
-Inside the project folder run: pip install -r requirements.txt

### Apply Database Migrations
-python manage.py migrate (Optional)

### Run the Development Server
-python manage.py runserver

Open in any browser: Your project will now load successfully.

### Notes
- Python 3.10+ will work, but 3.13 is recommended.
- Django 5.x works, but 5.2.5 is recommended.
