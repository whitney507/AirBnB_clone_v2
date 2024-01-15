#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import unittest
import os
import pycodestyle
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    Test case for the City class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the test.
        """
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDown(cls):
        """
        Tear down after the test.
        """
        del cls.city

    def tearDown(self):
        """
        Additional teardown steps.
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """
        Test PEP8 style for the City module.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 style issues")

    def test_checking_for_docstring_City(self):
        """
        Check if there is a docstring for the City class.
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """
        Check if City has the expected attributes.
        """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """
        Check if City is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """
        Check if attribute types for City are as expected.
        """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """
        Test if the save method works for City.
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """
        Test if the to_dict method works for City.
        """
        self.assertEqual('to_dict' in dir(self.city), True)


class TestCityAttributes(unittest.TestCase):
    """
    Additional test case for City class attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test if state_id attribute is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test if name attribute is of type str.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """
    PEP8 style test case for the City module.
    """

    def test_pep8_user(self):
        """
        Test PEP8 style for the City module.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()

