#!/usr/bin/python3
""" Command interpreter for the HBNB project """
import cmd
import sys

from models import storage

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
            }


class HBNBCommand(cmd.Cmd):
    """ Console class """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel"""
        args = arg.split()
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            print(args[0])
            return
        if len(args) > 1:
            class_obj = classes[args[0]]()
            for arg in args[1:]:
                key, value = arg.split('=')
                value = value.replace('\\"', '"')
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                    value = value.replace('_', ' ')
                setattr(class_obj, key, value)
        else:
            class_obj = classes[args[0]]
        class_obj.save()
        print(class_obj.id)

    def do_show(self, arg):
        """ Show command to print the string representation of an instance
            based on the class name and id """
        if not arg:
            print("** class name missing **")
            return
        """ Divides the string (arguments) into a list of strings """
        arg_list = arg.split()
        if arg_list[0] not in classes:
            """ Check if the class name is valid  """
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            """ Check if the id is valid """
            print("** instance id missing **")
            return
        """ Key to access the dictionary """
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            """ Check if the key exists """
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes a complete object class """
        if not arg:
            print("** class name missing **")
            return
        """ Divides the string (arguments) into a list of strings """
        arg_list = arg.split()
        if arg_list[0] not in classes:
            """ Check if the class name is valid  """
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            """ Check if the id is valid """
            print("** instance id missing **")
            return
        """ Key to access the dictionary """
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            """ Check if the key exists """
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []
        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if isinstance(v, classes[args]):
                    print_list.append(str(v))
        else:
            for v in storage.all().values():
                print_list.append(str(v))
        print(print_list)

    def do_update(self, arg):
        """ Updates an object based on the class name and id by adding or
            updating attribute """
        if not arg:
            print("** class name missing **")
            return
        """ Divides the string (arguments) into a list of strings """
        arg_list = arg.split()
        if arg_list[0] not in classes:
            """ Check if the class name is valid  """
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            """ Check if the id is valid """
            print("** instance id missing **")
            return
        """ Key to access the dictionary """
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            """ Check if the key exists """
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            """ Check if the attribute is valid """
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            """ Check if the value is valid  """
            print("** value missing **")
            return
        """ Updates the attribute """
        setattr(storage.all()[key], arg_list[2], arg_list[3])
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
