#!usr/bin/python3

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

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        )
