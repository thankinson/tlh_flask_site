# QA Flask Final Project

This project started as a way for me to practice flask while on the QA Cloud course and since starting i have deceded to use it as part of my final project.

## The Project
### Flask app
This Flask app is designed to :

    - Allow user to access the user dashboard and update password or delete account.
    - Allow Admin to access an admin dashboard so they can give users diferent access rights to content or remove a user. 

The user should not be able to access the admin dashboard. 

### The Database
The database uses 2 tables to manage user information and what contente they can see and use in this app.

Note: the creat.py file to set up the db has all users Passwords set to password by default. this can be changed in the Dashboard page of application for local testing only you will also have to set an sql lite db to achive this and modify the __init__.py for none docker use.

The Tables
- Users --- Holds user information.
- UserAdmin --- This table is where a suers access rights are set. Either admin or not admin.

### Jenkinsfile
The jenkins file will setup and run tests of this Flask App

Jenkins Builds on push to main branch when job is Run. 

Unfortunatly i will not be able to provide a video for this as the course recomended way dose not work on windows 10 anymore as desktop and file directory access is no longer permitted with X-Brick game bar.

### Trello Board
This is the link to my trello board for this project. 

trello link: https://trello.com/b/gVIqjaOK/qa-tlh-final-project

###
###

## Python Modules
- cryptography
- email_validator
- flask
- flask_bcrypt
- flask_login
- flask_wtf
- flask_testing
- sqlalchemy
- flask_sqlalchemy
- wtforms
- wtforms[email]
- pymysql
- pytest

## File Structure
...
root/
|    flask-app/
|    |    |----application/
|    |    |           |---forms/
|    |    |           |       |--forms.py   
|    |    |           |
|    |    |           |---models/
|    |    |           |       |--models.py
|    |    |           |
|    |    |           |---modules/
|    |    |           |       |--csrf.py
|    |    |           |
|    |    |           |---routes/
|    |    |           |       |--routes.py
|    |    |           |
|    |    |           |---service/
|    |    |           |       |--create_db.py
|    |    |           |       |--service.py
|    |    |           |
|    |    |           |---static/
|    |    |           |       |--javascript/
|    |    |           |       |--styles/
|    |    |           |               |--adminpage.css
|    |    |           |               |--dashboard.css
|    |    |           |               |--index.css
|    |    |           |               |--main.css
|    |    |           |               |--signup.css
|    |    |           |
|    |    |           |---templates/
|    |    |                   |--adminpage.html
|    |    |                   |--dashboard.html
|    |    |                   |--index.html
|    |    |                   |--layout.html
|    |    |                   |--main.html
|    |    |                   |--signup.html
|    |    |---.gitignore
|    |    |
|    |    |---app.py
|    |    |
|    |    |---Jenkinsfile
|    |    |
|    |    |---README.md
|    |    |
|    |    |---Dockerfile
|    |    
|    nginx/
|       |---nginx.conf             
|
|---docker-compose.ymal
|
|---Jenkinsfile
...

### The write up
- unit Testing
I did not get around to unit testing my app. Even thouigh i started my project a few weeks ago i had that many issues getting docker to work over the first 2 days i didnt have enoughtime to write any test as it only left me a day for fixing the bugs in my app ready for hand in.

- This appication
This appication is designed to have a single none removeable admin that can give other users access rights to view the admin page. 

To access the site build this app on your local VM or on a cloud VM.

Open browser and enter your sever IP adress or local adress to navigate to the app. 

when the page loads you will see the home page with a brife descripton of what the app dose. 

Click on the Sign Up/login tab to bring up that page. 

Create your self a couple of users (users can also log in)

To log in on the Sign Up / Login page click the LOGIN Form button to bring up the login form. 

use the admin creds to access the db. 

default user: admin
default pass: password

(The default admin account CAN NOT be deleted from the app as far as i am aware.)

You should be instantly directed to the Dashboard page where you can see the basic admin account and have the ability to change your password.

To check other users click the Admin tab.

On the admin page curently you can give a non admin user admin access or delete user/admin.

Users who have Admin access can also delete other users and give user admin access.

after you are finished to logout just click teh logout link.


- The pipeline

Jenkins pipline will check to see if the app is running in docker and then build it.

- Future improvments.

I have a list of improvments i realy want to add to this. 

1. Create groups for users to be assigned to.
2. Create search feature to quickly lookup a user.
3. create multiple roles based on each gruop project. 
4. Unit testing. i realy need to look at unit testing. 
5. Better css layout and more profesinol look to the site.
6. Cleaner code.

