from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__) ##Module Name = __name__ = __main__
##Secret Key to protect against modifying cookies etc. (Set secret key for the appication)
app.config["SECRET_KEY"] = "d7545bde35264afcc836e153c2deabce"
##SQLALCHEMY - Set path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devops.db"

db = SQLAlchemy(app)

class User(db.Model):
    ##Unique number to define different users also the primary key ("primary_key=True")
    id = db.Column(db.Integer, primary_key=True)
    ##String with a max char value of "20", user_names need to be unique so pass in "unique=true"
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    ##String with a max char value of "20", user_names need to be unique so pass in "unique=true"
    user_email = db.Column(db.String(100), unique=True, nullable=False)
    ##String with a max char value of "50"
    uesr_password = db.Column(db.String(50), nullable=False)
    ##uploads attribute is related to the upload model
    uploads= db.relationship("Upload", backref="creator", lazy=True)

    ##Defines how the object is printed
    def __repr__(self):
        return f"User: ('{self.user_name}', '{self.user_email}')"

##Upload class that will hold the posts made onto webpage
class Upload(db.Model):
    ##Unique number to define different users also the primary key ("primary_key=True")
    id = db.Column(db.Integer, primary_key=True)
    ##Header for each post can only be 120 char long and must have data inputed.
    header = db.Column(db.String(120), nullable = False)
    ##Date and time of when the post was made, saves whatever the current time on system is as the date and time
    date_uploaded = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    caption = db.Column(db.Text, nullable = False)
    ##This will be the ID of the user (creator) of the post
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable = False)

    ##Defines how the object is printed
    def __repr__(self):
        return f"Upload: ('{self.header}', '{self.date_uploaded}')"


##Temporary Data Set
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
    form = RegistrationForm()
    if form.validate_on_submit():
        ##Validation Message
        flash(f'Account has now successfully been created for {form.user_name.data}!', 'success')
        ##Redirect to home page once successful instead of staying static on registration page
        return redirect(url_for('home'))
    return render_template("register_form.html", form=form)

##Assigned URL for Login Page.
##GET used to retrieve the data & POST to insert/update record.
@app.route("/loginform", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.user_email.data =="admin@blog.com" and form.user_password.data == "password":
            #Validate Message shows log in was succeessful (parameteres met)
            flash("Log In Successful!", "success")
            ##Redirect user to home page
            return redirect(url_for("home"))
        ##If parameters not met (unsuccessful login) Display message to let user know
        else:
            flash("Login has been unsuccessful. Try Again!","danger")

    return render_template("login_form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
