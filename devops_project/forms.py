## form structures for login pages and registration pages
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from devops_project.models import User

#Set boundries around what the user is able to input in each field to get rid of anomalies
##Registration Form Fields
class RegistrationForm(FlaskForm):
     user_name = StringField("Username", validators=[DataRequired(),Length(min=2, max=20)])
     user_email = StringField("Email", validators=[DataRequired(),Email()])
     user_password = PasswordField("Password", validators=[DataRequired()])
     confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo("user_password")])
     submit = SubmitField("Sign Up")

     ##Check if there is already pre existing records of user & display a message for them
     def validate_user_email(self, user_email):

          user = User.query.filter_by(user_email=user_email.data).first()
          if user:
               raise ValidationError("This user email has already been used!")

     def validate_user_name(self, user_name):

          user = User.query.filter_by(user_name=user_name.data).first()
          if user:
               raise ValidationError("This user name has already been used!")
#Log In Form For Existing Users
class LoginForm(FlaskForm):
     user_email = StringField("Email", validators=[DataRequired(),Email()])
     user_password = PasswordField("Password", validators=[DataRequired()])
     submit = SubmitField("Log In")



