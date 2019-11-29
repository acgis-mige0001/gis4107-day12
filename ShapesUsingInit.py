#-------------------------------------------------------------------------------
# Name:        ShapesUsingInit
# Purpose:     Initialize shape objects
#
# Author:      elle.migeon
#
# Created:     29-11-2019
# Copyright:   (c) elle.migeon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------

def main():
    pass

import math

class Circle(object):
    def __init__(self, radius, area):
        self.radius = radius
        self.area = area

    def __str__(self):
        return 'Circle area with a radius of {0} is {1}'.format(self.radius, self.area)

class Square(object):
    def __init__(self, side, area):
        self.side = side
        self.area = area

    def __str__(self):
        return 'Square area with a side of {0} is {1}'.format(self.side, self.area)

class Rectangle(object):
    def __init__(self, width, height, area):
        self.width = width
        self.height = height
        self.area = area

    def __str__(self):
        return 'Rectangle area with a width of {0} and height of {1} is {2}'.format(self.width, self.height, self.area)

if __name__ == '__main__':
    main()