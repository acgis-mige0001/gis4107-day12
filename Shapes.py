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

##class Circle(object):

##class Shapes:
##    def __init__ (self):
##        self.type = ''
##
##shape1 = Shapes()
##shape1.type = "circle"
##
##shape2 = Shapes()
##shape2.type = "square"
##
##shape3 = Shapes()
##shape3.type = "rectangle"
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
        return (self.__radius * math.pi) ** 2
pass

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

if __name__ == '__main__':
    main()