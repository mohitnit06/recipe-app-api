from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_creation(self):
        email = 'test@gmail.com'
        password = 'pass1234'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_super_user_creation(self):

        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 'test1234'
        )

        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
