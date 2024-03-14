from flask import Blueprint, render_template, redirect, url_for, flash,request,flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from auth.forms import SignupForm
from __init__ import db, login_manager
from auth.models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('main.profile'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))  
    return render_template('signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.html'))


@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html')