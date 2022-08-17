from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()


class ContactsForm(FlaskForm):
    relationsip = StringField('Relationship', validators = [DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    phone_number = PasswordField('Phone Number', validators = [DataRequired()])
    home_address = PasswordField('Home Address', validators = [DataRequired()])
    submit = SubmitField()