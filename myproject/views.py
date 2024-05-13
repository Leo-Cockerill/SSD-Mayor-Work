#this file is for navigation and routing
#https://flask.palletsprojects.com/en/3.0.x/tutorial/views/#create-a-blueprint


from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') #this is the route
def home(): #this is the function that will be executed when the route is accessed
    return "<h1>Hello World<h1>"