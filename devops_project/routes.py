##Redirect routes to webpages
import bcrypt
from flask import render_template, url_for, flash, redirect
from flask_login.utils import login_required
from devops_project import app, db, bcrypt
from devops_project.forms import RegistrationForm, LoginForm
from devops_project.models import User, Upload
from flask_login import login_user, current_user, logout_user

##Temporary Data Set (HARDCODED)
uploads = [
        {
            "user": "RITIK VALA",
            "header": "Post No.1",
            "caption": "First Post Caption",
            "date_uploaded": "24 February, 2021"
        },
        {
            "user": "JAMES BOND",
            "header": "Post No.2",
            "caption": "Second Post Caption",
            "date_uploaded": "15 March, 2021"
        }

]


##Assigned URL for Home Page.
@app.route("/")
def home():
    return render_template("home_page.html", uploads=uploads)

##Assigned URL for About Page.
@app.route("/about")
def about():
    return render_template("about_page.html")

##Assigned URL for Registration Page.
##Get used to retrieve the data & post to insert/update record.
@app.route("/registerform", methods=['GET','POST'])
def register():
    ##Check iff user is logged in and then redirect to home webpage
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        ##user_password gets hashsed & .decode to change from bites to string
        hashed_password = bcrypt.generate_password_hash(form.user_password.data).decode('utf-8')
        ##Create new instance for the user & add user to make changes to the devops database
        user = User(user_name=form.user_name.data, user_email=form.user_email.data, user_password=hashed_password)
        db.session.add(user)
        db.session.commit()
        ##Validation Message
        flash(f'Account has now successfully been created for {form.user_name.data}!', 'success')
        ##Redirect to home page once successful instead of staying static on registration page
        return redirect(url_for('login'))
    return render_template("register_form.html", form=form)

##Assigned URL for Login Page.
##GET used to retrieve the data & POST to insert/update record.
@app.route("/loginform", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        ##Check if user exists in current database
        user= User.query.filter_by(user_email=form.user_email.data).first()
        ##check if user exists as well as if the password and user email match
        if user and bcrypt.check_password_hash(user.user_password, form.user_password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash("Login has been unsuccessful. Try Again!","danger")
    return render_template("login_form.html", form=form)

##Route to log user out back to main homepage
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

#create posts and upload to page
@app.route("/upload")
@login_required
def new_upload():
    return render_template("Create_upload.html")