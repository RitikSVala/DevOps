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
    
    def test_update_emp(self):
        response = self.client.post(
            url_for('editRecordForm', empno=1),
            data = dict(emp_name='Bob Smith', department='IT', subject='php', salary=18000, marks=305),
            follow_redirects = True
        )
        self.assertIn(b'Bob Smith', response.data)
    
    def test_del_emp(self):
        response = self.client.get(url_for('deleteEmployee', empno=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee Information System', response.data)
    
    def test_emp_info(self):
        response = self.client.get(url_for('personalInformation', empno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
    
    def test_view_edit(self):
        response = self.client.get(url_for('editRecordForm', empno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)
    
    def test_view_add(self):
        response = self.client.get(url_for('saveRecord'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)
    
    def test_filter_recs(self):
        response = self.client.post(url_for('filterrecords'),
        data = dict(dept='IT'))
        self.assertIn(b'John Smith', response.data)
    
    def test_filter_recs_all(self):
        response = self.client.post(url_for('filterrecords'),
        data = dict(dept='all'),
        follow_redirects = True)
        self.assertIn(b'John Smith', response.data)