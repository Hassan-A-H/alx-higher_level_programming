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
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
