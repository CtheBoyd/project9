class Point():

    def __init__(self, x_coord, y_coord):
        self._x_coord = point_1
        self._y_coord = point_2

        def get_x_coord(self):
            return self.x_coord

        def get_y_coord(self):
            return self.y_coord


    def distance_to():
            sum = 0
            for i in list():
                sum += i.age
                avg = sum / len(list)
                square_sum = 0
                for i in list():
                    square_sum += (i.age - avg) ** 2
                    var = square_sum / len(list)
                    std = var ** 0.5
                    retrun(std)


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