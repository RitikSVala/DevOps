from flask import url_for
from flask_testing import TestCase
from devops_project import app, db
import devops_project.routes
from devops_project.forms import RegistrationForm, LoginForm
from devops_project.models import User, Upload

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
    
    def setUp(self):
        db.create_all()
        Sample1 = User(user_name='RitikVala', user_email='RitikV@hotmail.com', user_password='Python', confirm_password='Python')
        db.session.add(Sample1)
        db.session.commit()
        Sample2 = Upload(header='This is a post', caption= 'this is a caption')
        db.session.add(Sample2)
        db.session.commit()   

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def registerform(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'RitikVala', response.data)
    
    def loginform(self):
        response = self.client.post(
            url_for('loginform'),
            data = dict(user_name='RitikVala', user_email='Hi@admin.com', user_password='php'),
            follow_redirects = True
        )
        self.assertIn(b'RitikVala', response.data)
  