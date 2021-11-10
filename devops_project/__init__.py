from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) ##Module Name = __name__ = __main__
##Secret Key to protect against modifying cookies etc. (Set secret key for the appication)
app.config["SECRET_KEY"] = "d7545bde35264afcc836e153c2deabce"
##SQLALCHEMY - Set path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devops.db"
db = SQLAlchemy(app)

##import down here to avoid circular import confliction
from devops_project import routes