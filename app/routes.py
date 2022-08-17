from app import app

from flask import render_template

from app.forms import SignUpForm

from app.models import User

from app.forms import ContactsForm

from app.models import Contacts


@app.route('/')
def index():
    author_info = {
        'my_name': 'Jeremy'
    }
    return render_template('index.html', author = author_info)


@app.route('/signup')
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Form has been successfully validated! ')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        new_user = User(email = email, username = username, password = password)
        print(f'{new_user.username} has been created. ')
    return render_template('signup.html', form = form)


@app.route('/contacts')
def contacts():
    form = ContactsForm()
    if form.validate_on_submit():
        print('Contact has been successfully validated! ')
        relationship = form.relationsip.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        home_address = form.home_address.data
        new_contact = Contacts(relationship = relationship, first_name = first_name, last_name = last_name, phone_number = phone_number, home_address = home_address)
        print(f'{new_contact.first_name} has been created. ')
    return render_template('contacts.html', form = form)