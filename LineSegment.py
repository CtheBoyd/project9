# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/25/2022
# Description: Takes cartesian points, creates lines from two points, finds the slope of the line, then compares with another line to find parallelity.
#

class Point:
    """class for pulling cartesian points"""

    def __init__(self, x_coord, y_coord):
        """pulls cartesian x and y coordinates"""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """method for getting x coordinate"""
        return self._x_coord

    def get_y_coord(self):
        """method for getting y coordinate"""
        return self._y_coord

    def distance_to(self, point_2):
        """distance formula"""
        distance = 0
        distance += (((point_2._x_coord - point_1._x_coord) ** 2) + ((point_2._y_coord - point_1._y_coord) ** 2))
        endpoint = distance ** .5
        return (endpoint)


class LineSegment:
    """class for testing each line length, slope, and parallelity"""

    def __init__(self, point_1, point_2):
        """pulls the ending points of each line"""
        self.endpoint_1 = point_1
        self.endpoint_2 = point_2

    def get_endpoint_1(self):
        """method for getting the first ending point"""
        return self.endpoint_1

    def get_endpoint_2(self):
        """method for getting the second ending point"""
        return self.endpoint_2

    def length(self):
        """returns the length of each line"""
        return self.endpoint_1.distance_to(self.endpoint_2)

    def is_parallel_to(self, line_segment):
        """tests if two lines are parallel"""
        if self.slope() == line_segment.slope():
            return True
        else:
            return False

    def slope(self):
        """returns the slope of each line"""
        return (self.endpoint_2.get_y_coord() - self.endpoint_1.get_y_coord()) / (
                self.endpoint_2.get_x_coord() - self.endpoint_1.get_x_coord())

point_1 = Point(7, 4)

point_2 = Point(-6, 18)

#print(point_1.distance_to(point_2))

line_seg_1 = LineSegment(point_1, point_2)

#print(line_seg_1.length())

#print(line_seg_1.slope())

point_3 = Point(-2, 2)

point_4 = Point(24, 12)

line_seg_2 = LineSegment(point_3, point_4)

#print(line_seg_2.length())

#print(line_seg_2.slope())

#print(line_seg_1.is_parallel_to(line_seg_2))
