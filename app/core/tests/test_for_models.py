from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def dummy_user(email='test@gmail.com', password='12345'):
    """a  dummy user for test"""
    return get_user_model().objects.create_user(email, password)


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
        '''check created user is staff with superuser permissions'''
        email = 'ashok@example.com'
        password = '123Ashok'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=dummy_user(),
            name='Curry'
            )

        self.assertEqual(str(tag), tag.name)