### Password Manager

`python3 -m venv virtualenv`
`source virtualvenv/bin/activate`
`git clone PROJECT_NAME`
`pip3 install -r password_manager/requirements.txt `
`python3 manage.py makemigrations`
`python3 manage.py migrate`
`python3 manage.py createsuperuser`
`python3 manage.py runserver`

Now, you can access your password manager at http://localhost:8000/passwords/ or http://localhost:8000/passwords/add or http://localhost:8000/admin. It will display a list of passwords fetched from the database.

![Passwords](passwords.png)

![Add a new password](add_password.png)

![Admin Console](admin_console.png)