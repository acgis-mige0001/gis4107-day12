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

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'The X, Y coordinates of the point {0}, {1}'.format(self.x, self.y)

class Line(object):

    def  __init__(self, from_point, to_point):
        self.from_point = from_point #x1, y1
        self.to_point = to_point #x2, y2

    def get_length(self):
        length = (((self.to_point.x - self.from_point.x)**2) + ((self.to_point.y - self.from_point.y)**2))**0.5
        return float(length)

    def __str__(self):
        return 'The length of a line with point coordinates of ({0}, {1}), ({2}, {3})'.format(self.from_point.x, self.from_point.y, self.to_point.x, self.to_point.y)





if __name__ == '__main__':
    main()