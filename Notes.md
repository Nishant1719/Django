# General Notes

- # Notes on creating a app.
    - Step 1 : Command for creating app.
        ```bash
        python .\manage.py startapp AppName
        ```
    - Step 2 :
        - Make main project aware about the app folder
            - Go to settings files:
            - INSTALLED_APPS =  [
                ...,
                'DjangoApp',
            ]
    
- # Notes on Integrating tailwind : Terminal Commands
    - Step 1: pip install django-tailwind
        - pip install 'django-tailwind[reload]' (Optional)
    
    - Step 2: 
        (Django) PS C:\Users\Nishant\Desktop\Study\Django\Djangopractice> python .\manage.py tailwind init

    - Step 3:
