#!/usr/bin/python3
"""
Module for testing the Amenity class.
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import unittest

storage_t = getenv("HBNB_TYPE_STORAGE")

class TestAmenityModel(test_basemodel):
    """Test case for the Amenity model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test case."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_attribute_type(self):
        """Test the type of the 'name' attribute."""
        new_amenity = self.value()
        self.assertEqual(type(new_amenity.name), str)

class TestPEP8(unittest.TestCase):
    """Test case for PEP8 compliance."""
    
    def test_pep8_compliance(self):
        """Check PEP8 style for the Amenity module."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

class TestInheritFromBaseModel(unittest.TestCase):
    """Test case to check if Amenity inherits from BaseModel."""

    def test_instance(self):
        """Check if Amenity is an instance of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")

class TestAmenityBaseModel(unittest.TestCase):
    """Test case for the Amenity class in relation to BaseModel."""

    def test_attributes_types(self):
        """Test the types of attributes in Amenity."""
        with patch('models.amenity'):
            amenity_instance = Amenity()
            expected_attrs_types = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
            }
            instance_dict = amenity_instance.to_dict()
            expected_dict_attrs = ["id", "created_at", "updated_at", "name", "__class__"]
            self.assertCountEqual(instance_dict.keys(), expected_dict_attrs)
            self.assertEqual(instance_dict['name'], 'Barbie')
            self.assertEqual(instance_dict['__class__'], 'Amenity')

            for attr, types in expected_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, amenity_instance.__dict__)
                    self.assertIs(type(amenity_instance.__dict__[attr]), types)
            self.assertEqual(amenity_instance.name, "Barbie")

    # Additional tests...

class TestAmenityModel(unittest.TestCase):
    """Test case for the Amenity class."""

    def test_subclass_of_base_model(self):
        """Test that Amenity is a subclass of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attribute(self):
        """Test that Amenity has a 'name' attribute initialized as an empty string."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_t == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    # Additional tests...

