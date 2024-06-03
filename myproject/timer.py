from flask import Blueprint, render_template, request, flash

timer = Blueprint('timer', __name__)

from flask import Flask, render_template, Response
import time

@timer.route('/content') # render the content a url differnt from index. This will be streamed into the iframe
def content():
    def timer(t):
        for i in range(t):
            time.sleep(5) #put 60 here if you want to have seconds
            yield str(i)
    return Response(timer(10), mimetype='text/html') #at the moment the time value is hardcoded in the function just for simplicity

@timer.route('/')
def index():
    return render_template('timer2.html') # render a template at the index. The content will be embedded in this template




