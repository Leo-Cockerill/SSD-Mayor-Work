from flask import Flask
from os import path 



def create_app(): #This function is going to create the app for us
    app = Flask(__name__) #This is the app object that we are going to return
    app.config['SECRET_KEY'] = 'sjhkdshkshadkja' #Encryption of cookies and session data related to website.

    from .views import views #This is the views file that we created in the myproject folder
    from .auth import auth #This is the auth file that we created in the myproject folder
    

    app.register_blueprint(views, url_prefix='/') #This is the route for the views file
    app.register_blueprint(auth, url_prefix='/') #This is the route for the auth file



    # create_database(app) #This is going to create the database for us


    return app

# def create_database(app): #This function is going to create the database for us
#     if not path.exists('myproject/' + DB_NAME): #If the database does not exist
#         db.create_all(app=app) #This is going to create the database
#         print('Created Database!') #This is going to print out that the database was created



#This makes this project a python package meaning we can import this file and whatever is inside of this init.py file will run automatically once we import it.
