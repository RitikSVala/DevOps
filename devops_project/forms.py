from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Set boundries around what the user is able to input in each field to get rid of anomalies
##Registration Form Fields
class RegistrationForm(FlaskForm):
     user_name = StringField("Username", validators=[DataRequired(),Length(min=2, max=20)])
     user_email = StringField("Email", validators=[DataRequired(),Email()])
     user_password = PasswordField("Password", validators=[DataRequired()])
     confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo("user_password")])
     submit = SubmitField("Sign Up")

#Log In Form For Existing Users
class LoginForm(FlaskForm):
     user_email = StringField("Email", validators=[DataRequired(),Email()])
     user_password = PasswordField("Password", validators=[DataRequired()])
     remember = BooleanField("Remember Password")
     submit = SubmitField("Log In")



