#!/usr/bin/python3
"""
Module that contains the Base class.
This is the base class for managing the `id` attribute for future classes.
"""


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
