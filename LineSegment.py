class Point():

    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

        def get_x_coord(self):
            return self.x_coord

        def get_y_coord(self):
            return self.y_coord


    def distance_to():
        x_coord = xc
        y_coord = yc

        distance = 0
        for i in list():
            distance += ((point_2.xc - point_1.xc)**2 + (point_2.yc - point_1.yc)**2)
            total = distance **.5

            return(total)


point_1 = Point(7,4)
point_2 = Point(-6,18)
print(point_1.distance_to(point_2))
line_seg_1 = LineSegment(point_1,point_2)
print(line_seg_1.length())
print(line_seg_1.slope())

point_3 = Point(-2,2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3,point_4)
print(line_seg_1.is_parallel_to(line_seg_2))
