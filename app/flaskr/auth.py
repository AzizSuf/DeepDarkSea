from main import app  # __main__
from flask import Flask, render_template, request, redirect, url_for


@app.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')


@app.route('/signup')
def signup():
    return render_template('auth/signup.html')


@app.route('/login/handler', methods=['POST'])
def login_handler():
    print(request.form, flush=True)
    return redirect(url_for('index'))


@app.route('/signup/handler', methods=['POST'])
def signup_handler():
    print(request.form, flush=True)
    return redirect(url_for('index'))


@app.route('/user/guest')
def guest():
    return '<h1>THIS PAGE IN DEVELOPMENT</h1>'



@app.route('/base')
def base():
    return render_template('base.html', page_name='Login')
