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

if __name__ == '__main__':
    main()