from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Members, Cars

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()

        member1 = Members(name="new member", email= "newmember@test.app")
        db.session.add(member1)
        db.session.commit()

        car1 = Cars(plate="GB123", make= "Tesla X") #member_id
        db.session.add(car1)
        db.session.commit()


    def tearDown(self):
        # Will be called after every test
        db.drop_all()

class TestMembersCRUD(TestBase):

    def test_read_members(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('new member', str(response.data))
        self.assertIn('newmember@test.app', str(response.data))
    
    def test_create_members(self):
        response = self.client.post(url_for('create'),
            data=dict(name="created member", email="createmember@test.app"),
            follow_redirects=True
        )
        created_member = Members.query.get(2)
        self.assertEqual(created_member.name, "created member")
        self.assertIn('created member', str(response.data))
        self.assertIn('createmember@test.app', str(response.data))

    def test_update_members(self):
        response = self.client.post(
            url_for('update', name="new member"),
            data=dict(name="updated member", email="updatedmember@test.app", active=True),
            follow_redirects=True
        )
        self.assertIn("updated member", str(response.data))
        self.assertIn("updatedmember@test.app", str(response.data))

    def test_delete_members(self):
        response = self.client.post(
            url_for('delete', name="new member"),
            follow_redirects=True
        )
        self.assertNotIn("new member", str(response.data))

class TestcarsCRUD(TestBase):

    def test_read_cars(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('GB123', str(response.data))
        self.assertIn('Tesla X', str(response.data))
    
  