import os
import unittest

from app import app, db

TEST_DB = 'test.db'

BASE_DIR = ''

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(BASE_DIR, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    def register(self, email, password):
        return self.app.post(
            '/register',
            data=dict(email=email, password=password, username='user123', confirm_password=password, first_name='fName', last_name='lname', gender='Female', location='UK'),
            follow_redirects=True
        )

    def login(self, username, password):
        return self.app.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_authentication(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.request.path, '/login')

    def test_registration(self):
        response = self.register('shiwanikoirala0@gmail.com', 'secret')
        self.assertIn(b'Your account has been created', response.data)

    def test_login(self):
        self.register('shiwanikoirala0@gmail.com', 'secret')
        response = self.login('user123', 'secret')
        self.assertEqual(response.request.path, '/index')

    def test_new_post(self):
        self.register('shiwanikoirala0@gmail.com', 'secret')
        self.login('user123', 'secret')
        response = self.app.post(
            '/feed/new',
            data=dict(title='Test Title', content='Test content'),
            follow_redirects=True
        )
        self.assertIn(b'Test Title', response.data)

    def test_follow(self):
        test_user_1 = self.user(username="gjfksa",
                               email="hsjsj@mail.com",
                               first_name="hshs",
                               last_name="hhhwhwh",
                               gender="Male",
                               password="hhewhhwh")
        test_user_2 = self.user(username="hfjwh",
                               email="egdjsj@mail.com",
                               first_name="hdhdhd",
                               last_name="hwuqiqo",
                               gender="Female",
                               password="hjfkdbw"
                               )
        db.session.add(test_user_1)
        db.session.add(test_user_2)
        test_user_2.follow(test_user_1)
        db.session.commit()
        self.assertTrue(test_user_2.is_following(test_user_1))
        test_user_2.unfollow(test_user_1)
        db.session.commit()
        self.assertFalse(test_user_2.is_following(test_user_1))


if __name__ == "__main__":
    unittest.main()
