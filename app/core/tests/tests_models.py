from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='1234test'):
    '''Create a sample user'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@test.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email for the new user is normalised'''
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(
            email,
            'somepw'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_superuser_created_correctly(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        '''Test the tag string representation matches'''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
