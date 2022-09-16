from flask import Flask, render_template, redirect, url_for, request
from application import app
from application.forms.forms import UserRegistration, UserLogin
from application.models.models import Users
from application.service.service import Userservice, Loginservice
from flask_login import current_user


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Loginservice.is_logged_in()  #### this is not yet working
    message = ""
    form = UserRegistration()
    logform = UserLogin()
    if form.validate_on_submit():
        if request.method == 'POST':
            try:
                Userservice.Adduser(form=form)
                message = "User added to database"
            except:
                message = "User Name or Email Already in use"
        
    elif logform.validate_on_submit():
        if request.method == 'GET':
            try:
                Loginservice.log_in(logform=logform)
                if current_user.is_authenticated:
                    message = "Your IN!!!!!!"
                else:
                    message = "User Name or Password Incorrect"
            except:
                message = "Fatel Error: The Admin Gods do not smile upon you"  

    return render_template('signup.html', form=form, logform=logform, message=message)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # Loginservice.is_logged_in()  #### this is not yet working

#     ########################################
#     ## need to work out the logic on this
#     ########################################
#     ## Sign Up section ##
#     message = ""
#     form = UserRegistration()
#     if form.validate_on_submit():
#         try:
#             Userservice.Adduser(form=form)
#             message = "User added to database"
#         except:
#             message = "User Name or Email Already in use"
    
#     # login section on signup
#     logform = UserLogin()
#     if logform.validate_on_submit():
#         try:
#             Loginservice.log_in(logform=logform)
#             if current_user.is_authenticated:
#                 message = "Your IN!!!!!!"
#             else:
#                 message = "User Name or Password Incorrect"
#         except:
#             message = "Fatel Error: The Admin Gods do not smile upon you"  

#     return render_template('signup.html', form=form, logform=logform, message=message)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     print("Login page hit")
#     message = ""
#     Loginservice.is_logged_in()
#     form = UserLogin()
#     if form.validate_on_submit():
#         try:
#             Loginservice.log_in(form=form)
#             if current_user.is_authenticated:
#                 return redirect(url_for('index'))
#             else:
#                 message = "User Name or Password Incorrect"
#         except:
#             message = "Fatel Error: The Admin Gods do not smile upon you"  
#     return render_template('login.html', form=form, message=message)





####################################################################
##                        chopping block                          ##
####################################################################


## attempt 1. if and elif to check 
## idea behind this was that the checks were npt hitting the rigt places
## thought wrpping them in an if elif statement would solve it
## tried it without checking for POST first then with Checking for post

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # Loginservice.is_logged_in()  #### this is not yet working

#     # forms and message #
#     message = ""
#     form = UserRegistration()
#     logform = UserLogin()
#     #########################
#     if request.method == 'POST' and form.validate_on_submit():
#         try:
#             Userservice.Adduser(form=form)
#             message = "User added to database"
#         except:
#             message = "User Name or Email Already in use"
    
#     # login section on signup
#     elif request.method == 'POST' and logform.validate_on_submit():
#     # if logform.validate_on_submit():
#         try:
#             Loginservice.log_in(logform=logform)
#             if current_user.is_authenticated:
#                 message = "Your IN!!!!!!"
#             else:
#                 message = "User Name or Password Incorrect"
#         except:
#             message = "Fatel Error: The Admin Gods do not smile upon you"  

#     return render_template('signup.html', form=form, logform=logform, message=message)

###############################################
# attempt 2. this idea was to wrap the login and signup in 2 seperate functions 
# and call them in an iff statemnet

# no success

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # Loginservice.is_logged_in()  #### this is not yet working
#     form = UserRegistration()
#     logform = UserLogin()


#     def SignUp(form):
#         # message = ""
#         form = UserRegistration()

#         try:
#             Userservice.Adduser(form=form)
#             message = "User added to database"
#         except:
#             message = "User Name or Email Already in use"

#     # login section
#     def LogIn(logform):
#         logform = UserLogin()

#         print("login elif hit")
#         try:
#             Loginservice.log_in(logform=logform)
#             print("login hit")

#             if current_user.is_authenticated:
#                 message = "Your IN!!!!!!"
#             else:
#                 message = "User Name or Password Incorrect"
#         except:
#             message = "Fatel Error: The Admin Gods do not smile upon you"  

#     if form.validate_on_submit():
#         SignUp(form)
#     elif logform.validate_on_submit():
#         LogIn(logform)
        


#     return render_template('signup.html', form=form, logform=logform)


# ## attempt 3

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # Loginservice.is_logged_in()  #### this is not yet working

#     ########################################
#     ## need to work out the logic on this
#     ########################################
#     ## Sign Up section ##
#     message = ""
#     form = UserRegistration()
#     if form.validate_on_submit():
#         try:
#             Userservice.Adduser(form=form)
#             message = "User added to database"
#         except:
#             message = "User Name or Email Already in use"
    

#     return render_template('signup.html', form=form, message=message)
    

# # @app.route('/register', methods=['GET', 'POST'])
# def login():    
#     # login section on signup
#     message = ""
#     logform = UserLogin()
#     if logform.validate_on_submit():
#         try:
#             Loginservice.log_in(logform=logform)
#             if current_user.is_authenticated:
#                 message = "Your IN!!!!!!"
#             else:
#                 message = "User Name or Password Incorrect"
#         except:
#             message = "Fatel Error: The Admin Gods do not smile upon you"  

#     return render_template('signup.html', logform=logform, message=message)