from flask import Flask

def create_app(): #This function is going to create the app for us
    app = Flask(__name__) #This is the app object that we are going to return
    app.config['SECRET_KEY'] = 'sjhkdshkshadkja' #Encryption of cookies and session data related to website.

    return app


#This makes this project a python package meaning we can import this file and whatever is inside of this init.py file will run automatically once we import it.
