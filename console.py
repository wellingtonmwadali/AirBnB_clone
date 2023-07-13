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

    def do_create(self, arg):
        """
        method that creates a new class instance
        and print id.
        """
        arg2 = parse(arg)
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg2[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        method that isplay string representation of a
        class instance of a certain id.
        """
        arg2 = parse(arg)
        objdict = storage.all()
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg2) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg2[0], arg2[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg2[0], arg2[1])])

    def do_destroy(self, arg):
        """
        method that delete a class
        instance of a given id.
        """
        arg2 = parse(arg)
        objdict = storage.all()
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg2) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg2[0], arg2[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg2[0], arg2[1])]
            storage.save()

    def do_all(self, arg):
        """
        method that displays string representations of all
        instances of a class.
        nb:If no class is specified, then
        display all instantiated objects.
        """
        arg2 = parse(arg)
        if len(arg2) > 0 and arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj2 = []
            for obj in storage.all().values():
                if len(arg2) > 0 and arg2[0] == obj.__class__.__name__:
                    obj2.append(obj.__str__())
                elif len(arg2) == 0:
                    obj2.append(obj.__str__())
            print(obj2)

    def do_count(self, arg):
        """
        method that retrieve the number of
        instances of a given class.
        """
        arg2 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg2[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Update a class instance of a given id by adding
        ."""
        arg2 = parse(arg)
        objdict = storage.all()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
