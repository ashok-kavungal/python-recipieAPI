from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_created(self):
        '''check the created user has required email conditions'''
        email = 'mathew@gmail.com'
        password = 'daredevil123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_super_user_created(self):
        '''check the super user created is staff and have super user permisssions'''
        email = 'ashok@example.com'
        password = '123Ashok'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
