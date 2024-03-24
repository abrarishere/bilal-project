from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')
@auth.route('/logout')
def logout():
    return 'logout'

@auth.route('/forgot')
def forgot():
    return render_template('forgot.html')


@auth.route('/projects')
def projects():
    return render_template('projects.html')