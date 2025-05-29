# Start the python virtual environment
- In the main directory of your Django project, you can create a virtual environment to manage your dependencies. This is a good practice to keep your project isolated from other Python projects on your system.
- # Create a virtual environment
```bash
.venv/Scripts/activate
```
# Create a Django project
```bash
django-admin startproject Djangopractice
```
- After creating a Django project, you can follow these steps to run the development server.

- # Navigate to the project directory
```bash
cd Djangopractice
```
- # Run the Django development server
```bash
python manage.py runserver
# python manage.py runserver 8000 (port) for specifying a port
```