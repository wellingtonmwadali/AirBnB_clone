#!/usr/bin/python3
"""file storage class unit tests
"""
import unittest
import json
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestConsoleClass(unittest.TestCase):
    """TestConsoleClass
    Args:
        unittest (): Property for unit testing
    """

    maxDiff = None

    def setUp(self):
        """ condition that tests file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """this  destroys the created file """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """ check whether theres is module documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """ check whether theres is  documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check whether there is  method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test whether base and test_base follows for pep8 style """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")

    def test_executable_file(self):
        """ Check whether file has permissions to execute"""
        # Check read access
        is_read_true = os.access('console.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check write access
        is_write_true = os.access('console.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('console.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_check_help(self):
        """ checks whether each command has a help output """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_good(self):
        """ Test whether there is create function """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_empty(self):
        """ Tests create function """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create")
            self.assertEqual(help_val.getvalue(), "** class name missing **\n")

    def test_create_unknown(self):
        """ Tests create_class whether it doesn't """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Holberton")
            self.assertEqual(val.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """ test checks for normal parameters """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_show_notfound(self):
        """ Test with class that does not exists """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show helloo ')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_show_empty(self):
        """ Test function with class missing is"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_show_id(self):
        """ Test function with id missing """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        """ tests whether class is missing """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_destroy_wrong(self):
        """ tests whether class name is missing """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy fakeclass')
            self.assertTrue(val.getvalue() == "** class is missing **\n")

    def test_destroy_id(self):
        """ tests whether the id is does not exist """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(val.getvalue() == "**instance id unavailable **\n")

    def test_destroy_notfound(self):
        """ tests whether the id belongs to an instance """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel 121212')
            self.assertTrue(val.getvalue() == "** instance missing **\n")

    def destroy_working(self):
        """ tests whether destroy methods delets an instance """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** instance is missing**\n")

    def test_all_fakeclass(self):
        """ tests whether class name is available """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(val.getvalue() == "** class is missing **\n")

    def test_all_working(self):
        """ tests whether all methods work correclty """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_trueclass(self):
        """tests whether all methods work efficiently with a class input """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update_missingclass(self):
        """ tests whether the class is doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_update_wrongclass(self):
        """ tests whether the class is available """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update FakeClass')
            self.assertTrue(val.getvalue() == "** class not available **\n")

    def test_update_noinstance(self):
        """ tests whether the instance id is not available """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(val.getvalue() == "**instance id unavailable **\n")

    def test_update_notfound(self):
        """ tests whether instance id exists """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel 121212')
            self.assertTrue(val.getvalue() == "**instance is missing **\n")

    def test_update_missing_name(self):
        """ tests whether  attribute name is missing """
        with patch('sys.stdout', new=StringIO()) as my_id:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = my_id.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() == "** attribute name missing **\n")

    def test_update_missing_value(self):
        """ tests whether attribute value is missing """
        with patch('sys.stdout', new=StringIO()) as my_id:
            HBNBCommand().onecmd('create BaseModel')
            base_id = my_id.getvalue()
            self.assertTrue(len(base_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel ' + base_id + "first_name")
            self.assertTrue(val.getvalue() == "** value is not available **\n")

    def test_update_ok(self):
        """tests whether update test is working """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + user_id + " name alice")
            HBNBCommand().onecmd("show BaseModel " + user_id)
            self.assertTrue("alice" in val.getvalue())

    def test_update_okextra(self):
        """tests whether  update test is working """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            uid = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + uid + " name alice ho")
            HBNBCommand().onecmd("show BaseModel " + uid)
            self.assertTrue("alice" in val.getvalue())

    def test_user_console(self):
        """ Tests the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class ia not available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue(val.getvalue() != "** instance is missing **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all User")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update User " + user_id + " name alice")
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue("alice" in val.getvalue())
            HBNBCommand().onecmd("destroy User " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show User "+user_id)
            self.assertEqual(val.getvalue(), "** no instance available **\n")

    def test_place_console(self):
        """ Tests class user with the  console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Place")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class not available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertTrue(val.getvalue() != "** no instance available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Place")
            self.assertTrue(val.getvalue() != "** class not found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Place " + user_id + " name alice")
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertTrue("alice" in val.getvalue())
            HBNBCommand().onecmd("destroy Place " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place "+user_id)
            self.assertEqual(val.getvalue(), "** no instance available **\n")

    def test_state_console(self):
        """ Tests the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create State")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class not available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show State " + user_id)
            self.assertTrue(val.getvalue() != "** no instance available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all State")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update State " + user_id + " name alice")
            HBNBCommand().onecmd("show State " + user_id)
            self.assertTrue("alice" in val.getvalue())
            HBNBCommand().onecmd("destroy State " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show State "+user_id)
            self.assertEqual(val.getvalue(), "** no instance available **\n")

    def test_city_console(self):
        """ Tests user class with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create City")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class is missing**\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + user_id)
            self.assertTrue(val.getvalue() != "** no instance available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all City")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update City " + user_id + " name alice")
            HBNBCommand().onecmd("show City " + user_id)
            self.assertTrue("alice" in val.getvalue())
            HBNBCommand().onecmd("destroy City " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City "+user_id)
            self.assertEqual(val.getvalue(), "** no instance available **\n")

    def test_amenity_console(self):
        """ Test user class with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Amenity")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class is not available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertTrue(val.getvalue() != "** no instance available**\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Amenity")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Amenity " + user_id + " name alice")
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertTrue("alice" in val.getvalue())
            HBNBCommand().onecmd("destroy Amenity " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity "+user_id)
            self.assertEqual(val.getvalue(), "** no instance available **\n")

    def test_review_console(self):
        """ Tests user class with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Review")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class is missing **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertTrue(val.getvalue() != "** no instance available **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Review")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Review " + user_id + " name alice")
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertTrue("alice" in val.getvalue())
            HBNBCommand().onecmd("destroy Review " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review "+user_id)
            self.assertEqual(val.getvalue(), "** no instance available **\n")

    def test_alternative_all(self):
        """tests  the alternate all with class."""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_alternative_show(self):
        """tests the  alternate show with show class"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.show(\"" + user_id + "\")")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count(self):
        """tests alternate show with show class"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 1)

    def test_alternative_destroy(self):
        """tests alternate destroy with [class].destroy(id)"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.destroy(\"" + user_id + "\")")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 0)

    def test_alternative_update1(self):
        """test alternate update with show class"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            line = "\", \"name\", \"alice\")"
            HBNBCommand().onecmd("User.update(\"" + user_id + line)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.show(\"" + user_id + "\")")
            self.assertTrue("alice" in val.getvalue())

    def test_alternative_update2(self):
        """tests alternate update with show class"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            line = "\", {'first_name': 'James', 'age': 79})"
            HBNBCommand().onecmd("User.update(\"" + user_id + line)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.show(\"" + user_id + "\")")
            self.assertTrue("James" in val.getvalue())


if __name__ == '__main__':
    unittest.main()
