# How to install Django in python virtual environment
- Create a virtual environment
```bash:
python -m venv .venv
```
- Activate the virtual environment
```bash:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
- Install Django
```bash:
pip install django
```
# using Faster package manager like uv:
- Install uv:
```bash:
pip install uv
```
- Create a virtual environment with uv:
```bash:
uv venv
```
- Activate the virtual environment
```bash:
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
- Install Django using uv:
```bash:
uv pip install django
```
# How to create project in Django:
# - Create a new Django project
```bash
django-admin startproject myproject
```

