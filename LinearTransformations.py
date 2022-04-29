from numpy import dot, radians, tan

class LinearTransformation:

    def __init__(self, degrees):
        self.degrees = degrees
        self.transformer = [
            [1, 0],
            [1, tan(radians(degrees))]
        ]

    def transform(self, matrix):
        new_matrix = dot(matrix, self.transformer)
        return new_matrix