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

        car1 = Cars(plate="new123", make= "new make", member_id=1)
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
    
    def test_update_members_get(self):
        response = self.client.get(
            url_for('update', name="new member"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

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



class TestCarsCRUD(TestBase):

    def test_read_cars(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('new123', str(response.data))
        self.assertIn('new make', str(response.data))

    def test_update_cars(self):
        member2 = Members(name="member2", email= "newmember@test2.app")
        db.session.add(member2)
        db.session.commit()
        response = self.client.post(
            url_for('update_car', plate="new123"),
            data=dict(plate="updated123", make="updated make", car_owner=2),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('updated123', str(response.data))
        self.assertIn('updated make', str(response.data))
        self.assertIn('member2', str(response.data))
    
    def test_create_cars(self):
        member2 = Members(name="member2", email= "newmember@test2.app")
        db.session.add(member2)
        db.session.commit()
        response = self.client.post(url_for('create_car'),
            data=dict(plate="created123", make="created make", car_owner=2),
            follow_redirects=True
        )
        self.assertIn('created123', str(response.data))
        self.assertIn('created make', str(response.data))
        self.assertIn('member2', str(response.data))

    def test_delete_cars(self):
        response = self.client.post(
            url_for('delete_car', plate="new123"),
            follow_redirects=True
        )
        self.assertNotIn("new123", str(response.data))

    def test_update_cars_get(self):
        response = self.client.get(
            url_for('update_car', plate="new123"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)




