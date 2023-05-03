from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class UserManagerTests(TestCase):
    def test_create_user_without_email(self):
        user_create = get_user_model().objects.create_user
        self.assertRaises(ValueError, 
                          user_create,
                          email='',
                          password='12test12')

    def test_create_user(self):
        user = get_user_model().objects.create_user(email='test@example.com',
                                                    password='12test12')
        self.assertTrue(isinstance(user, get_user_model()))

    def test_create_staffuser(self):
        user = get_user_model().objects.create_staffuser(email='test@example.com',
                                                    password='12test12')
        self.assertTrue(isinstance(user, get_user_model()))
        self.assertEqual(user.staff, True)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(email='test@example.com',
                                                    password='12test12')
        self.assertTrue(isinstance(user, get_user_model()))
        self.assertEqual(user.staff, True)
        self.assertEqual(user.admin, True)



class UserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(email='test@example.com',
                                                        password='12test12')
        
    def test_str(self):
        self.assertEqual(str(self.user), self.user.email)
        
    def test_staff(self):
        self.assertEqual(self.user.is_staff, self.user.staff)
        
    def test_admin(self):
        self.assertEqual(self.user.is_admin, self.user.admin)

class SigninTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com',
                                                         password='12test12')
        
    def tearDown(self):
        self.user.delete()
        
    def test_correct(self):
        user = authenticate(email='test@example.com', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)
        
    def test_wrong_username(self):
        user = authenticate(email='wrong@wrong.com', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)
        
    def test_wrong_pssword(self):
        user = authenticate(email='test@example.com', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)