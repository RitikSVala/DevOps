##Initialize .py file 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import getenv
from flask_bcrypt import Bcrypt

##Flask instance!
app = Flask(__name__) ##Module Name = __name__ = __main__
##Secret Key to protect against modifying cookies etc. (Set secret key for the appication)
app.config["SECRET_KEY"] = "d7545bde35264afcc836e153c2deabce"
##SQLALCHEMY - Set path
app.config["SQLALCHEMY_DATABASE_URI"] = getenv('db_uri')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

##import down here to avoid circular import confliction
from devops_project import routes