#!/usr/bin/python3
"""
This is the console model
it provides an entry to the console with
some specific implementations
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """provides the entry point to the imterpreter"""

    prompt = "(hbnb) "
    my_classes = {"BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"}

    def do_quit(self, s):
        """this implements the quit"""
        return True

    def do_EOF(self, s):
        """this implements the EOF"""
        print()
        return True

    def help_quit(self):
        """the implements the help for quit"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """this implements the help for EOF"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """this overrides the empty line default method"""
        pass

    def do_create(self, s):
        """Creates a new instance of BaseModel, Saves it and prints the id"""
        if len(s) == 0:
            print("** class name missing **")
        elif s not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(s)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, s):
        """Prints the string rep of an instance"""
        if len(s) == 0:
            print("** class name missing **")
            return
        args = list(s.split())
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        try:
            classname = f"{args[0]}.{args[1]}"
            if classname not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[classname])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, s):
        """Deletes an Instance based on the class name and id"""
        if len(s) == 0:
            print("** class name missing **")
            return
        args = list(s.split())
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        try:
            classname = f"{args[0]}.{args[1]}"
            if classname not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[classname]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, s):
        """Prints all the objects or objects a particular class"""
        obj_lists = []
        args = list(s.split())
        if len(s) == 0:
            for keys in storage.all().values():
                obj_lists.append(keys)
            print(obj_lists)
        elif s in HBNBCommand.my_classes:
            for key, value in storage.all().items():
                if s in key:
                    obj_lists.append(value)
            print(obj_lists)
        else:
            print("** class doesn't exist **")

    def do_update(self, s):
        """Updates as instance based on the class name and id"""
        args = list(s.split())
        obj_dict = storage.all()
        if len(args) >= 4:
            classname = f"{args[0]}.{args[1]}"
            attr_value = args[3]
            attr_value = attr_value.strip('"')
            attr_value = attr_value.strip("'")
            casting = type(eval(args[3]))
            setattr(storage.all()[classname], args[2], casting(attr_value))
            storage.all()[classname].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, s):
        """retrieve the number of instances of a class"""
        if len(s) == 0:
            print("** class name missing **")
        elif s not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key, value in storage.all().items():
                if s in key:
                    count += 1
            print(count)

    def default(self, s):
        """for accepting arguments in <class name>.all()"""
        args = s.split(".")

        if len(args) == 1:
            print(f"** Invalid syntax: {s}")
            return
        args1 = args[1].split("(")
        if args1[0] == "all":
            HBNBCommand.do_all(self, args[0])
        elif args1[0] == "count":
            HBNBCommand.do_count(self, args[0])
        elif args1[0] == "show":
            arg_id = args1[1]
            arg_id = arg_id.split(")")
            arg_id = arg_id[0].strip('"')
            argument = args[0] + " " + arg_id
            HBNBCommand.do_show(self, argument)
        elif args1[0] == "destroy":
            arg_id = args1[1]
            arg_id = arg_id.split(")")
            arg_id = arg_id[0].strip('"')
            argument = args[0] + " " + arg_id
            HBNBCommand.do_destroy(self, argument)
        elif args1[0] == "update":
            mul_args = args1[1].split(",", 1)
            arg_id = mul_args[0].strip("'").strip('"')
            arg_dict_str = mul_args[1].strip(')').strip()

            try:
                arg_dict = eval(arg_dict_str)
                if isinstance(arg_dict, dict):
                    for key, value in arg_dict.items():
                        argument = args[0] + " " + arg_id + " " + key +\
                                   " " + repr(value)
                        HBNBCommand.do_update(self, argument)
                else:
                    mul_args = args1[1].split(",")
                    arg_id = mul_args[0]
                    arg_id = arg_id.strip('"')
                    arg_id = arg_id.strip("'")
                    arg_name = mul_args[1]
                    arg_name = arg_name.strip(',')
                    arg_name = arg_name.strip(" ")
                    arg_name = arg_name.strip("'")
                    arg_name = arg_name.strip('"')
                    arg_val = mul_args[2]
                    arg_val = arg_val.strip(" ")
                    arg_val = arg_val.strip(")")
                    argument = args[0] + " " + arg_id + " " + arg_name +\
                        " " + arg_val
                    HBNBCommand.do_update(self, argument)
            except (SyntaxError, NameError, IndexError):
                print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
