
from math import sqrt
import turtle
from LinearTransformation import LinearTransformation

class QuadraticBezier:

    def __init__(self, start, control, end):

        self.start = start 
        self.control = control
        self.end = end

    def get_points(self, no_of_points=10):

        self.no_of_points = no_of_points - 1

        for i in range(no_of_points):
            division = i / self.no_of_points

            x1 = self.start[0] + (self.control[0] - self.start[0]) * division
            y1 = self.start[1] + (self.control[1] - self.start[1]) * division

            x2 = self.control[0] + (self.end[0] - self.control[0]) * division
            y2 = self.control[1] + (self.end[1] - self.control[1]) * division

            final_x = x1 + (x2 - x1) * division
            final_y = y1 + (y2 - y1) * division

            yield final_x, final_y

class CubicBezier:

    def __init__(self, start, control1, control2, end):

        self.start = start 
        self.control1 = control1
        self.control2 = control2
        self.end = end

    def get_points(self, no_of_points=10):

        self.no_of_points = no_of_points - 1

        for i in range(no_of_points):
            division = i / self.no_of_points

            x1 = self.start[0] + (self.control1[0] - self.start[0]) * division
            y1 = self.start[1] + (self.control1[1] - self.start[1]) * division

            x2 = self.control1[0] + (self.control2[0] - self.control1[0]) * division
            y2 = self.control1[1] + (self.control2[1] - self.control1[1]) * division

            x3 = self.control2[0] + (self.end[0] - self.control2[0]) * division
            y3 = self.control2[1] + (self.end[1] - self.control2[1]) * division

            intermediate_x1 = x1 + (x2 - x1) * division
            intermediate_y1 = y1 + (y2 - y1) * division

            intermediate_x2 = x2 + (x3 - x2) * division
            intermediate_y2 = y2 + (y3 - y2) * division

            final_x = intermediate_x1 + (intermediate_x2 - intermediate_x1) * division
            final_y = intermediate_y1 + (intermediate_y2 - intermediate_y1) * division

            yield final_x, final_y

class Arc:

    def __init__(self, start, end, a, b, rotation=0, large_arc=True, sweep=True) -> None:
        self.start = start
        self.end = end
        self.a = a
        self.b = b
        self.rotation = rotation
        self.large_arc = large_arc
        self.sweep = sweep
        self.lt = LinearTransformation(rotation)

    def get_points(self):

        x = self.start[0]
        while x <= self.start[0] + (self.a * 2):

            part1 = self.b / self.a
            part2 = sqrt( self.a**2 - x**2 )

            y = part1 * part2
            result = self.lt.transform([x, y])

            if x >= self.end[0]: break
            yield round(result[0]), round(result[1])
            x += 0.1

        x = self.start[0]
        while x <= self.start[0] + (self.a * 2):

            part1 = self.b / self.a
            part2 = sqrt( self.a**2 - x**2 )

            y = part1 * part2
            result = self.lt.transform([x, -y])

            if x >= self.end[0]: break
            yield round(result[0]), round(result[1])
            x += 0.1
            


