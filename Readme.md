# intro_django

This repository serves as a starting point for beginners learning how to build web applications using Django. The project walks you through the initial steps of setting up a Django project, creating applications, and managing databases.

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is used by developers to build robust, scalable, and maintainable web applications quickly.

## Getting Started

### Prerequisites

Before you can run this project, ensure you have the following installed:

- **Python 3.x**: Django is built on Python, so you'll need a compatible version.
- **pipenv**: A tool to create isolated Python environments and manage dependencies.
- **Git**: Version control system to clone the repository.

### Setting Up the Project

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/TandohAnthonyNwiAckah/intro_django.git
    cd intro_django
    ```

2. **Create and activate a virtual environment:**
    ```bash
    pipenv shell
    ```
    This command creates a virtual environment and activates it. Virtual environments help in maintaining dependencies and versions separately for different projects.

3. **Install Django:**
    ```bash
    pipenv install django
    ```
    This command installs Django in your virtual environment. You can verify the installation by running:
    ```bash
    python -m django --version
    ```

4. **Create a new Django project:**
    ```bash
    django-admin startproject myproject
    ```
    This command initializes a new Django project named `myproject`. The project directory will contain settings and configurations needed to run your application.

5. **Create a new application:**
    ```bash
    python manage.py startapp myapp
    ```
    This command creates a new Django app named `myapp`. Apps are modular components within a Django project, allowing you to manage different functionalities independently.

6. **Run the server:**
    ```bash
    python manage.py runserver
    ```
    This command starts the Django development server, which allows you to see your project in action at `http://127.0.0.1:8000/`.

7. **Make database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    These commands prepare and apply database schema changes, respectively. Django uses a model-based approach to create database tables.

8. **Open the Django shell:**
    ```bash
    python manage.py shell
    ```
    The shell allows you to interact with your Django project, manipulate data, and test functionalities in an interactive environment.

### Understanding the Basics

1. **Django Project Structure:**
    After creating a Django project, you will see the following structure:
    ```plaintext
    intro_django/
    ├── manage.py         # Command-line utility for interacting with Django
    ├── intro_django_proj/
    │   ├── __init__.py   # Indicates that this directory is a Python package
    │   ├── settings.py   # Configuration settings for the project
    │   ├── urls.py       # URL definitions for routing requests
    │   ├── wsgi.py       # WSGI configuration for deployment
    ```

2. **Creating Views and URLs:**
    - **Views** define what content is displayed on a particular page. They are typically written in `views.py` within your app directory.
    - **URLs** define the routes to different views. URL configurations are written in `urls.py` within your project or app directories.

3. **Creating Models:**
    - **Models** define the structure of your database tables. Each model maps to a table in the database. You can define models in `models.py` within your app directory.

4. **Django Admin Interface:**
    Django provides an admin interface out-of-the-box. You can access it by creating a superuser with the command:
    ```bash
    python manage.py createsuperuser
    ```
    After creating a superuser, you can log in at `http://127.0.0.1:8000/admin/` to manage your database models.

### Additional Learning Resources

- [Official Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Getting Started Guide](https://www.djangoproject.com/start/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Full Stack Python - Django Guide](https://www.fullstackpython.com/django.html)

By following these steps, beginners can get started with a simple Django project and gradually build their understanding of more complex features in the framework.
