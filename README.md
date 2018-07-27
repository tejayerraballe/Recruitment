# Recruitment
Sample Recruitment Form
# recruit
Recruitment Site

## Description:

This project allows users to submit the recruitment form and admin has access to accept/reject the form.

Project urls:

- `http://localhost:8000/recruitment/form/` This url directs user to submit the form
- `http://localhost:8000/admin/` This url redirects to admin page where we can see recruit app. Recruit app will have list of the recruitment forms. Only super user can access and will be able to accept/reject the form


## Technology Used:

- Python
- Django
- default database(sqlite3)

## Project Setup Procedure:
Create virtalenv by command

`virtualenv envi`

Activate the virtualenv by:

`source envi/bin/activate`

`pip install django`

For migrations:

In the source code I have added the migrations script so you can just run the below command to migrate the schema:

`python manage.py migrate`

Then create the superuser:

From the project directory run:

`python manage.py createsuperuser`

Then start the project by the command: 

`python manage.py runserver`
