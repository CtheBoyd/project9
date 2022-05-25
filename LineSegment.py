class Point():

    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self, point):
        distance = 0

        distance += (((point_2._x_coord - point_1._x_coord) ** 2) + ((point_2._y_coord - point_1._y_coord) ** 2))

        endpoint = distance ** .5

        return (endpoint)


class LineSegment():

    def __init__(self, line_seg_1, line_seg_2):
        self._line_seg_1 = endpoint_1
        self._line_seg_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):

        if endpoint_1 >= endpoint_2:
            return (endpoint_1 - endpoint_2)

        else:
            return (endpoint_2 - endpoint_1)

    def is_parallel_to(self):


point_1 = Point(7, 4)
point_2 = Point(-6, 18)
print(point_1.distance_to(point_2))
line_seg_1 = LineSegment(point_1, point_2)
print(line_seg_1.length())
print(line_seg_1.slope())

point_3 = Point(-2, 2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3, point_4)
print(line_seg_1.is_parallel_to(line_seg_2))



