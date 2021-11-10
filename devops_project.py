from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__) ##Module Name = __name__ = __main__
##Secret Key to protect against modifying cookies etc. (Set secret key for the appication)
app.config["SECRET_KEY"] = "d7545bde35264afcc836e153c2deabce"
##SQLALCHEMY - Set path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devops.db"

db = SQLAlchemy(app)

class User(db.Profile):
    ##Unique number to define different users also the primary key ("primary_key=True")
    id = db.column(db.int, primary_key=True)
    ##String with a max char value of "20", user_names need to be unique so pass in "unique=true", 
    user_name = db.column(db.string(20), unique=True, nullable=False)
    ##String with a max char value of "20", user_names need to be unique so pass in "unique=true", 
    user_email = db.column(db.string(100), unique=True, nullable=False)
    ##String with a max char value of "50", 
    uesr_password = db.column(db.string(50), nullable=False)

    ##


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
