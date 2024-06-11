from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/timer')
def timer():
    return render_template("timer.html")

@auth.route('/steps')
def steps():
    steps = [
        {"text": "Step 1: Preheat your oven to 375°F (190°C).", "underline": ["Preheat"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"},
        {"text": "Step 2: Mix the ingredients in a bowl.", "underline": ["Mix"], "gif": "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"},
        {"text": "Step 3: Place the mixture into a baking dish.", "underline": ["Place"], "gif": "https://media.giphy.com/media/3ohhwpKYFbJsNOhYyc/giphy.gif"},
        {"text": "Step 4: Bake for 25-30 minutes.", "underline": ["Bake"], "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"}
    ]
    return render_template("index.html", steps = steps)

@auth.route('/slider')
def slider():
    images = [
        '/static/assets/ed07d79937b933a1dca3918b313f0cc4.png',
        '/static/assets/ed07d79937b933a1dca3918b313f0cc4.png',
        '/static/assets/ed07d79937b933a1dca3918b313f0cc4.png'
    ]
    return render_template("index.html", images = images)


@auth.route('/test')
def test():
    return render_template("test.html")

@auth.route('/sign-up', methods=['GET', 'POST'] )
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2') 


        if len(email) <4:
            flash('Email must be greater than 4 characters.', category='error')

        elif len(firstName) <2:
            flash('First name must be greater than 2 characters.', category='error')

        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')

        elif len(password1) <7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account Created!', category='success') # add user to database
            pass
        


    return render_template("sign_up.html") 