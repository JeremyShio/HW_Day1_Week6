from app import app


from flask import render_template


from colorama import Fore


@app.route('/')


@app.route('/index')
def index():
    user_info = {
        'my_name': 'Jeremy'
    }
    return render_template('index.html', user = user_info)


@app.route('/favnums')
def favnums():
    user_info = {
        'my_name': 'Jeremy'
    }
    
    numbers = ['21', '47', '2', '30', '74']

    return render_template('favnums.html', user = user_info, numbers = numbers)


@app.route('/base')
def base():
    return render_template('base.html')