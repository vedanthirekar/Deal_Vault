from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FloatField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL, Optional, NumberRange
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    dob = DateField('Date of Birth', validators=[DataRequired()], format='%Y-%m-%d')
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# from flask_wtf import FlaskForm
# from wtforms import StringField, FloatField, SubmitField, IntegerField, TextAreaField, DateField
# from wtforms.validators import DataRequired, Optional, NumberRange

class DealForm(FlaskForm):
    store_name = StringField('Store Name', validators=[DataRequired(), Length(min=2, max=100)])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    deal_desc = TextAreaField('Deal Description', validators=[DataRequired()])
    deal_amount = FloatField('Deal Amount', validators=[Optional(), NumberRange(min=0)])
    deal_validity = DateField('Deal Validity', validators=[Optional()], format='%Y-%m-%d')
    submit = SubmitField('Post Deal')