#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Defines the Holberton command line interpreter"""

    prompt = "(hbnb) "
    my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": review
            }

    def do_nothing(self, arg):
        """function that does nothing"""
        pass

    def do_quit(self, arg):
        """function that exists the program and saves data"""
        return True

    def do_EOF(self, arg):
        """signal to close the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
