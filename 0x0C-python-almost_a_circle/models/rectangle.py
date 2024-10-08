#!/usr/bin/python3
"""
Module that contains the Rectangle class, inheriting from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Private Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate.
        __y (int): Y-coordinate.

    Methods:
        __init__: Initializes a Rectangle object.
        width (property): Getter and setter for width.
        height (property): Getter and setter for height.
        x (property): Getter and setter for x.
        y (property): Getter and setter for y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate (default is 0).
            y (int, optional): The y-coordinate (default is 0).
            id (int, optional): The id for the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance using the character `#` in stdout.
        The rectangle is printed based on its width, height, and
        takes into account x and y for spacing.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance
        in the format:[Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Rectangle instance based on the positional
 (*args)
        or keyword arguments (**kwargs).

        Args:
        *args: Variable length argument list, where:
            1st argument is id,
            2nd is width,
            3rd is height,
            4th is x,
            5th is y.
        **kwargs: Key/value pairs to update attributes, where keys represent
                  attribute names.
                  Keyword arguments are processed only if *args is empty.
        """
        if args:
            lst_attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, lst_attr[i], args[i])
        else:
            for key, val in kwargs.items():
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
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
