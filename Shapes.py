# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

def main():
    pass

import math

class Circle(object):
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return 'Circle area with a radius of {0} is {1}'.format(self.radius, self.area)

class Square(object):
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side

    @property
    def area(self):
        return (self.__side) ** 2
    def __str__(self):
        return 'Square area with a side of {0} is {1}'.format(self.side, self.area)

class Rectangle(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def area(self):
        return (self.__height) * (self.__width)

    def __str__(self):
        return 'Rectangle area with a width of {0} and height of {1} is {2}'.format(self.width, self.height, self.area)

if __name__ == '__main__':
    main()