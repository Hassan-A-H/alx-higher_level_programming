#!/usr/bin/python3
"""
Module that contains the Base class.
This is the base class for managing the `id` attribute for future classes.
"""
import json


class Base:
    """
    The Base class will be the “base” of all other classes in this project.

    Class Attributes:
        __nb_objects (int): Counter for the number of instantiated objects.

    Instance Attributes:
        id (int): The unique identifier for an instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base instance.

        Args:
            id (int, optional): The id of the instance. If None, the id is
            automatically assigned by incrementing the `__nb_objects` counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
        list_dictionaries (list): A list of dictionaries to convert into a
        JSON string.

        Returns:
        str: A JSON string representation of list_dictionaries.
        If list_dictionaries
             is None or empty, returns "[]".
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string.

        Args:
        json_string : A string representing a list of dictionaries

        Returns:
        list: A list of the JSON string representation json_string.
        If list_dictionaries
             is None or empty, returns [].
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances of the class.
            Each instance should have
            a `to_dictionary` method to convert the instance to a dictionary.
        """
        filename = "{}.json".format(cls.__name__)
        lst_dict = []

        if list_objs:
            for obj in list_objs:
                lst_dict.append(obj.to_dictionary())

        json_str = cls.to_json_string(lst_dict)

        with open(filename, "w") as f:
            f.write(json_str)
