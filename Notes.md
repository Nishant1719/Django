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
    