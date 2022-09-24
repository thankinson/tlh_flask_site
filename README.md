# QA Flask Final Project

This project started as a way for me to practice flask while on the QA Cloud course and since starting i have deceded to use it as part of my final project.

## The Project
### Flask app
This Flask app is designed to :

    - Allow user to access the user dashboard and update password or delete account.
    - Allow Admin to access an admin dashboard so they can give users diferent access rights to content or remove a user. 

The user should not be able to access the admin dashboard. 

### The Database
The database uses 3 tables to manage user information and what contente they can see and use in this app.

The Tables
- Users --- Holds user information.
- UserAdmin --- This is the bridge between the Users and UserRoles table.
- UserRoles --- This table says what admin and users cann access using booleans.

## Python Modules
- Flask==2.2.2
- Flask-Bcrypt==1.0.1
- Flask-Login==0.6.2
- Flask-SQLAlchemy==2.5.1
- Flask-Testing==0.8.1
- Flask-WTF==1.0.1

## File Structure

    root/
    |----application/
    |           |---forms/
    |           |       |--forms.py   
    |           |
    |           |---models/
    |           |       |--models.py
    |           |
    |           |---modules/
    |           |       |--csrf.py
    |           |
    |           |---routes/
    |           |       |--routes.py
    |           |
    |           |---service/
    |           |       |--service.py
    |           |
    |           |---static/
    |           |       |--javascript/
    |           |       |--styles/
    |           |               |--adminpage.css
    |           |               |--dashboard.css
    |           |               |--index.css
    |           |               |--main.css
    |           |               |--signup.css
    |           |
    |           |---templates/
    |                   |--adminpage.html
    |                   |--dashboard.html
    |                   |--index.html
    |                   |--layout.html
    |                   |--main.html
    |                   |--signup.html
    |---.gitignore
    |
    |---app.py
    |
    |---Jenkinsfile
    |
    |---README.md