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