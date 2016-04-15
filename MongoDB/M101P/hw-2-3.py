#####  Homework: Homework 2.3
##### Blog User Sign-up and Login
##### 
##### Download the handout and unpack it.
##### 
##### You should see three files at the highest level: blog.py, userDAO.py and sessionDAO.py. There is also a views directory which contains the templates for the project.
##### 
##### The project roughly follows the model/view/controller paradigm. userDAO and sessionDAO.py comprise the model. blog.py is the controller. The templates comprise the view.
##### 
##### If everything is working properly, you should be able to start the blog by typing:
##### 
##### python blog.py
##### 
##### Note that this project requires the following python modules be installed on your computer: cgi, hmac, datetime, json, sys, string, hashlib, urllib, urllib2, random, re, pymongo, and bottle. If you have python installed at all, you probably already have most of these installed except pymongo and bottle.
##### 
##### If you have python-setuptools installed, the command "pip" makes this simple. Any other missing packages will show up when validate.py is run, and can be installed in a similar fashion. As of this recording, we are still using the beta version of PyMongo so we will install directly from GitHub. Note that this directions are identical to what we taught you within the lessons and you should already have PyMongo 3.x and bottle installed. If not, use the following commands.
##### 
##### $ pip install https://github.com/mongodb/mongo-python-driver/archive/3.0b1.tar.gz
##### $ pip install bottle
##### 
##### If you go to http://localhost:8082 you should see a message, "this is a placeholder for the blog"
##### 
##### Here are some URLs that must work when you are done.
##### 
##### http://localhost:8082/signup
##### http://localhost:8082/login
##### http://localhost:8082/logout
##### 
##### When you login or sign-up, the blog will redirect to http://localhost:8082/welcome and that must work properly, welcoming the user by username
##### 
##### We have removed two pymongo statements from userDAO.py and marked the area where you need to work with XXX. You should not need to touch any other code. The pymongo statements that you are going to add will add a new user to the database upon sign-up, and validate a login by retrieving the right user document.
##### 
##### The blog stores its data in the blog database in two collections, users and sessions. Here are two example docs for a username 'erlichson' with password 'fubar'. You can insert these if you like, but you don't need to.
##### 
##### > db.users.find()
##### { "_id" : "erlichson", "password" : "d3caddd3699ef6f990d4d53337ed645a3804fac56207d1b0fa44544db1d6c5de,YCRvW" }
##### > 
##### > db.sessions.find()
##### { "_id" : "wwBfyRDgywSqeFKeQMPqVHPizaWqdlQJ", "username" : "erlichson" }> 
##### 
##### Once you have the the project working, the following steps should work:
##### 
#####     go to http://localhost:8082/signup
#####     create a user
##### 
##### It should redirect you to the welcome page and say: welcome username, where username is the user you signed up with. Now
##### 
#####     Go to http://localhost:8082/logout
#####     Now login http://localhost:8082/login.
##### 
##### 
##### Ok, now it's time to validate you got it all working.
##### 
##### There was one additional program that should have been downloaded in the project called validate.py.
##### 
##### python validate.py
##### 
##### For those who are using MongoHQ, MongoLab or want to run the webserver on a different host or port, there are some options to the validation script that can be exposed by running
##### 
##### python validate.py -help
##### 
##### If you got it right, it will provide a validation code for you to enter into the box below. Enter just the code, no spaces. Note that your blog must be running when you run the validator. 
##### 




########################################################################
#
# Copyright (c) 2008 - 2013 10gen, Inc. <http://10gen.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#



import pymongo
import sessionDAO
import userDAO
import bottle
import cgi
import re



__author__ = 'aje'


# General Discussion on structure. This program implements a blog. This file is the best place to start to get
# to know the code. In this file, which is the controller, we define a bunch of HTTP routes that are handled
# by functions. The basic way that this magic occurs is through the decorator design pattern. Decorators
# allow you to modify a function, adding code to be executed before and after the function. As a side effect
# the bottle.py decorators also put each callback into a route table.

# These are the routes that the blog must handle. They are decorated using bottle.py

# This route is the main page of the blog
@bottle.route('/')
def blog_index():

    cookie = bottle.request.get_cookie("session")

    username = sessions.get_username(cookie)

    # todo: this is not yet implemented at this point in the course

    return bottle.template('blog_template', dict(username=username))



# displays the initial blog signup form
@bottle.get('/signup')
def present_signup():
    return bottle.template("signup",
                           dict(username="", password="",
                                password_error="",
                                email="", username_error="", email_error="",
                                verify_error =""))

# displays the initial blog login form
@bottle.get('/login')
def present_login():
    return bottle.template("login",
                           dict(username="", password="",
                                login_error=""))

# handles a login request
@bottle.post('/login')
def process_login():

    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print "user submitted ", username, "pass ", password

    user_record = users.validate_login(username, password)
    if user_record:
        # username is stored in the user collection in the _id key
        session_id = sessions.start_session(user_record['_id'])

        if session_id is None:
            bottle.redirect("/internal_error")

        cookie = session_id

        # Warning, if you are running into a problem whereby the cookie being set here is
        # not getting set on the redirect, you are probably using the experimental version of bottle (.12).
        # revert to .11 to solve the problem.
        bottle.response.set_cookie("session", cookie)

        bottle.redirect("/welcome")

    else:
        return bottle.template("login",
                               dict(username=cgi.escape(username), password="",
                                    login_error="Invalid Login"))


@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return {'error':"System has encountered a DB error"}


@bottle.get('/logout')
def process_logout():

    cookie = bottle.request.get_cookie("session")

    sessions.end_session(cookie)

    bottle.response.set_cookie("session", "")


    bottle.redirect("/signup")


@bottle.post('/signup')
def process_signup():

    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # set these up in case we have an error case
    errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
    if validate_signup(username, password, verify, email, errors):

        if not users.add_user(username, password, email):
            # this was a duplicate
            errors['username_error'] = "Username already in use. Please choose another"
            return bottle.template("signup", errors)

        session_id = sessions.start_session(username)
        print session_id
        bottle.response.set_cookie("session", session_id)
        bottle.redirect("/welcome")
    else:
        print "user did not validate"
        return bottle.template("signup", errors)



@bottle.get("/welcome")
def present_welcome():
    # check for a cookie, if present, then extract value

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)  # see if user is logged in
    if username is None:
        print "welcome: can't identify user...redirecting to signup"
        bottle.redirect("/signup")

    return bottle.template("welcome", {'username': username})



# Helper Functions

# validates that the user information is valid for new signup, return True of False
# and fills in the error string if there is an issue
def validate_signup(username, password, verify, email, errors):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASS_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    errors['username_error'] = ""
    errors['password_error'] = ""
    errors['verify_error'] = ""
    errors['email_error'] = ""

    if not USER_RE.match(username):
        errors['username_error'] = "invalid username. try just letters and numbers"
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = "invalid password."
        return False
    if password != verify:
        errors['verify_error'] = "password must match"
        return False
    if email != "":
        if not EMAIL_RE.match(email):
            errors['email_error'] = "invalid email address"
            return False
    return True

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.blog

users = userDAO.UserDAO(database)
sessions = sessionDAO.SessionDAO(database)


bottle.debug(True)
bottle.run(host='localhost', port=8082)         # Start the webserver running and wait for requests

