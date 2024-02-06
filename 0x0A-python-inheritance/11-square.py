#!/usr/bin/python3
"""Defines a Rectangle subclasss Square."""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """Represent a square."""


    def __init__(self, size):
        """Initialize a new square.


        Args:
            size (int): The size of the new square.
        """


self.integer_validator("size", size)
        super().__init__size, size)
        self.__size = size
