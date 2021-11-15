from polygon import Polygon

class Triangle(Polygon):
        def __init__(self):
                Polygon.__init__(self, 3)

        def findArea(self):
                a, b, c = self.sides
                s = (a + b + c) / 2
                area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
                print('The area of triangle is %0.2f', area)


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
