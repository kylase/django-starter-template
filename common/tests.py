from django.test import TestCase
from .models import CustomUser


class TestCustomUserModel(TestCase):
    """
    Test class for CustomUser
    """
    def setUp(self):
        """
        Create a test user
        """
        CustomUser.objects.create_user('test_user',
                                       email='test_user@example.com',
                                       password='test_user-password')

    def test_string_repr(self):
        """
        Test if the string representation of the `test_user` returns 'test_user'
        """
        test_user = CustomUser.objects.get(username='test_user')

        assert str(test_user) == 'test_user'
