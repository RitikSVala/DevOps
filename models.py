from datetime import datetime
from devops_project import db


class User(db.Model):
    ##Unique number to define different users also the primary key ("primary_key=True")
    id = db.Column(db.Integer, primary_key=True)
    ##String with a max char value of "20", user_names need to be unique so pass in "unique=true"
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    ##String with a max char value of "20", user_names need to be unique so pass in "unique=true"
    user_email = db.Column(db.String(100), unique=True, nullable=False)
    ##String with a max char value of "60"
    user_password = db.Column(db.String(60), nullable=False)
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