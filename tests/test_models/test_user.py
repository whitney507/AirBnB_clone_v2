#!/usr/bin/python3
"""
Unit tests for the User class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUser(test_basemodel):
    """
    Test case for the User class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test if the first_name attribute is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test if the last_name attribute is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test if the email attribute is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test if the password attribute is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)

