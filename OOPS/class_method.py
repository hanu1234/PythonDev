class Shape:
    def __init__(self, sides):
        self.sides = sides

    @classmethod
    def create_square(cls):
        return cls(sides=4)

    @classmethod
    def create_triangle(cls):
        return cls(sides=4)

    def get_sides(self):
        return self.sides


square = Shape.create_square()
print(square.get_sides())
