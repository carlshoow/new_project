from sqlite3 import IntegrityError
from flask import render_template, redirect, url_for, flash
from signin_login_flask import app, db, bcrypt
from signin_login_flask.forms import RegistrationForm, LoginForm
from signin_login_flask.db_class import User
#from flask_login import current_user


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            flash('Account already exists!', 'danger')
            return render_template('register.html', form=form)
            
        flash('Account created successfully', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been Log in', 'success')
        return redirect(url_for('account'))
    return render_template("login.html", form=form)


@app.route('/account')
def account():
    return render_template("account.html")