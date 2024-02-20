#!/usr/bin/python3
"""
Module containing the console, entry point for command interpreter
"""
import cmd
import uuid
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Place": Place,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, args):
        """Quits the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF and quits program"""
        return True

    def emptyline(self):
        """Does nothing given emptyline"""
        pass

    # def default(self, args):
    #     """Default for undefined commands"""
    #     supported_commands = {
    #         ...
    #     }
    #     if args in supported_commands:
    #         ...
    #     else:
    #         print("Unknown command: {}".format(args))

    def do_create(self, args):
        """
        Creates new instance and saves it to storage. Prints instance id.
        Usage: create <class name>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        new_inst = self.__classes[class_name]()
        storage.save()
        print(new_inst.id)

    def do_show(self, args):
        """
        Prints string representation of instance based on class name and id
        Usage: show <class_name> <instance_id>
        """
        args = args.split()
        if len(args) != 2:
            print("** class name or instance id missing **")
            return

        class_name, instance_id = args

        if class_name not in self.__classes:
            print("** class doen't exist **")
            return

        storage.reload()
        instances = storage.all()
        instance = None
        for key, inst in instances.items():
            cls_name, _ = key.split(".")
            if cls_name == class_name and inst.id == instance_id:
                instance = inst
                break

        if instance is None:
            print("** no instance found **")
            return

        print(str(instance))

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id. Saves to storage.
        Usage: destroy <class_name> <instance_id>
        """
        args = args.split()
        if len(args) != 2:
            print("** class name or instance id missing **")
            return

        class_name, instance_id = args

        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        instances = storage.all()
        instance = None
        key_to_delete = None
        for key, inst in instances.items():
            cls_name, _ = key.split(".")
            if cls_name == class_name and inst.id == instance_id:
                instance = inst
                key_to_delete = key
                break

        if instance is None:
            print("** no instance found **")
            return

        instances.pop(key_to_delete, None)
        storage.save()
        print("** instance deleted **")

    def do_all(self, args):
        """
        Prints the string representation of all instances
        based or not on the class name

        Usage: all [<class_name>]
        """
        args = args.split()
        if args:
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
                return
            class_name = args[0]
            instances = storage.all(class_name)
        else:
            instances = storage.all()

        for instance in instances:
            print(str(instance))

    def do_update(self, args):
        """
        Updates instance based on class name and id
        by adding or updating attribute. Saves to storage.

        Useage: update <class_name> <instance_id>
        <attribut_name> "<attribute_value>"
        """
        args = args.split()
        if len(args) != 4:
            print("** attribute name or value missing **")
            return

        class_name, instance_id, attr_name, attr_val = args

        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        instances = storage.all()
        instance = None
        for key, inst in instances.items():
            cls_name, _ = key.split(".")
            if cls_name == class_name and inst.id == instance_id:
                instance = inst
                break

        if instance is None:
            print("** no instance found **")
            return

        try:
            if attr_val.isdigit():
                attr_val = int(attr_val)
            elif attr_val.replace('.', '', 1).isdigit():
                attr_val = float(attr_val)
        except ValueError:
            pass

        setattr(instance, attr_name, attr_val)
        instance.save()
        print("** instance updated successfully **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
