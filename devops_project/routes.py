##Redirect routes to webpages
from flask import render_template, url_for, flash, redirect, request
from flask_login.utils import login_required
from devops_project import app, db, bcrypt
from devops_project.forms import RegistrationForm, LoginForm, UploadForm
from devops_project.models import User, Upload
from flask_login import login_user, current_user, logout_user


##Assigned URL for Home Page.
@app.route("/")
def home():
    uploads = Upload.query.all()
    return render_template("home_page.html", uploads=uploads)

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
@app.route("/upload/new", methods = ["GET","POST"])
@login_required
def new_upload():
    form = UploadForm()
    ##Validation to see if user has successfully uploaded the post
    if form.validate_on_submit():
        #create post onto the database
        upload = Upload(header=form.header.data, caption=form.caption.data, creator=current_user)
        db.session.add(upload)
        db.session.commit()
        flash("Your post has been successfully uploaded!", "success")
        return redirect(url_for("home"))
    ##Redirect user to the webpage to create a post and uplaod it
    return render_template("Create_upload.html", form=form, legend="New Post")


##Make upload ID a part of the route and pass the variable as an integer
@app.route("/upload/<int:upload_id>")
def upload(upload_id):
    upload = Upload.query.get(upload_id)
    return render_template("upload.html", upload=upload)

##Edit an existing post, user must be logged in. Display existing data in fields. methods to accept the logic from legend
@app.route("/upload/<int:upload_id>/update", methods = ["GET","POST"])
@login_required
def update_upload(upload_id):
    upload = Upload.query.get(upload_id)
    ##Decline access is the current user is not the creator fo the post
    if upload.creator != current_user:
        flash("You Do Not Access To This Post!","danger")
    form = UploadForm()
    if form.validate_on_submit():
        upload.header = form.header.data
        upload.caption = form.caption.data
        ##Doesn't need db.add because it already exists
        db.session.commit()
        flash("Your Post Has Now Been Updated, Thank You!", "success")
        return redirect(url_for("upload", upload_id=upload.id))
    elif request.method == "GET":
        ##Handle the changes made for the legend below
        form.header.data = upload.header
        form.caption.data = upload.caption
    return render_template("Create_upload.html", form =form, legend="Update Post")

##Edit an existing post, user must be logged in. Display existing data in fields. methods to accept the logic from legend
@app.route("/upload/<int:upload_id>/delete", methods = ["POST"])
@login_required
def delete_upload(upload_id):
    upload = Upload.query.get(upload_id)
    ##Decline access is the current user is not the creator fo the post
    if upload.creator != current_user:
        flash("You Do Not Access To This Post!","danger")
    db.session.delete(upload)
    db.session.commit()
    flash("Your post has been successfully deleted!", "success")
    return redirect(url_for("home"))