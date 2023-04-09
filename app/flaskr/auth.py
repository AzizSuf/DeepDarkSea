from main import app  # __main__
from flask import Flask, render_template, request, redirect, url_for, flash
import db

@app.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/signup')
def signup():
    return render_template('auth/signup.html')


@app.route('/login/handler', methods=['POST'])
def login_handler():
    name = request.form['email'].split('@')[0]

    user_email = request.form['email']
    user_password = request.form['password']

    # user_rememberme = request.form['remember']
    # print(user_rememberme, flush=True)

    # Check user in DB
    if db.check_user(user_email, user_password):
        flash(f'Приветствуем вас, {name}')
        return redirect(url_for('index'))
    else:
        flash(f'Неверный email или пароль')
        return redirect(url_for('login'))


@app.route('/signup/handler', methods=['POST'])
def signup_handler():
    print(request.form, flush=True)  # TODO: удалить

    # Simple validation.
    # TODO:
    if request.form['password'] == request.form['repeated_password']:
        user_email = request.form['email']
        user_password = request.form['password']

        # Add new user to DB
        db.add_user(user_email, user_password)

        return redirect(url_for('index'))
    else:
        flash('Пароли не совпадают')
        return redirect(url_for('signup'))


@app.route('/logout/handler')
def logout_handler():
    return redirect(url_for('index'))
