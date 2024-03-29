# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        exercise_template_tests.py
#
# Purpose:     Test functions for functions in exercise_template.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

import sys
import inspect

import Geometry
reload(Geometry)

# Add import statement for the module under test as follows:
# import module_under_test as alias

# For example:
# import world_pop_explorer as wpe
# reload(wpe)

def main():
    # Find and call all functions that begin with "test"
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()

# Copy/paste/change the test template below to create new test functions, where:
#    - the test function name must begin with the word "test"
#    - desc = Description of the test being made
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)"""
#
def template_for_test_functions():
    desc = ""
    expected = ""
    actual = ""
    print_test_results(func, desc, expected, actual)

# ------------------------------------------------------------------------------

# Create test functions here using the template_for_test_functions above.
# The name of the test functions needs to begin with "test"

def test_point_location():
    desc = 'Returns the x and y values of a point'
    x = 2.5
    y = 3.3
    point = Geometry.Point(x,y)
    f_x = float(x)
    f_y = float(y)
    point.x = f_x
    point.y = f_y
    expected = f_x , f_y
    actual = float(point.x) , float(point.y)
    print_test_results(Geometry.Point, desc, expected, actual)
    print str(point) + '\n'

def test_line_length():
    desc = 'Returns the length of a line if given the X, Y coordinates of its points'
    x1 = 2.5
    x2 = 4.5
    y1 = 3.3
    y2 = 6.3
    from_point = Geometry.Point(x1, y1)
    to_point = Geometry.Point(x2, y2)

    line = Geometry.Line(from_point,to_point)
    length = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

    expected = float(length)
    actual = line.get_length()
    print_test_results(Geometry.Line, desc, expected, actual)
    print str(line) + '\n'

def test_polyline_length():
    desc = 'Returns the total length of a polyline'

    x1 = 2.5
    x2 = 4.5
    x3 = 7.5
    y1 = 3.3
    y2 = 6.3
    y3 = 8.8

    from_point = Geometry.Point(x1, y1)
    to_point = Geometry.Point(x2, y2)
    to_point2 = Geometry.Point(x3,y3)

    line = Geometry.Line(from_point, to_point)
    line2 = Geometry.Line(to_point, to_point2)

    polyline = Geometry.Polyline()
    polyline.add_segment(line)
    polyline.add_segment(line2)

    length1 = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
    length2 = (((x3 - x2)**2) + ((y3 - y2)**2))**0.5

    expected = float(length1 + length2)
    actual = polyline.total_length()
    print_test_results(Geometry.Polyline, desc, expected, actual)
    print str(polyline) + '\n'


# ------------------------------------------------------------------------------
# Test template helper functions.  Code in this section should not need to
# modified.
#
def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") == 0:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, desc, expected, actual):
    """func_tested is the function being tested
       desc = Test description
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    if expected == actual:
        print "PASSED: {}".format(func_name)
        print "Detail: {}".format(desc)
    else:
        print "FAILED: {}".format(func_name)
        print "Desc:   {}".format(desc)
        print "Expect: {}".format(expected)
        print "Actual: {}".format(actual)
    print ""

if __name__ == '__main__':
    main()
