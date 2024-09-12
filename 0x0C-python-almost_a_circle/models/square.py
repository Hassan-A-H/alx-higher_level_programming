#!/usr/bin/python3

"""
This module defines the Square class, which inherits from the Rectangle class.

The Square class represents a square, which is a special kind of rectangle
where the width and height are equal. This class inherits from the Rectangle
class, utilizing its attributes and methods while simplifying width and height
to a single size attribute.

Classes:
    Square: Defines a square that inherits from the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    A square is a special type of rectangle where width and height are equal.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square (both width and height).
            x (int): x-coordinate of the square.
            y (int): y-coordinate of the square.
            id (int, optional): Identifier of the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        )

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Square instance using positional (*args)
        or keyword arguments (**kwargs).

        Args:
        *args: Variable-length argument list, where:
            1st argument represents id,
            2nd argument represents size (both width and height),
            3rd argument represents x-coordinate,
            4th argument represents y-coordinate.
        **kwargs: Key-value pairs to update attributes. Keys can be:
            'id', 'size', 'x', or 'y'. Keyword arguments are processed
            only if *args is empty.
        """

        if args:
            lst_attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if lst_attr[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, lst_attr[i], args[i])

        else:
            for key, val in kwargs.items():
                if key == "size":
                    setattr(self, "width", val)
                    setattr(self, "height", val)
                else:
                    setattr(self, key, val)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.

        The dictionary will have the following keys: 'id', 'size', 'x', 'y'.
        The 'size' key corresponds to both the width and height (since it's
        a square).

        Returns:
        dict: A dictionary containing the attributes of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
