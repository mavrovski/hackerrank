import math

class Point(object):
    def __init__(self, x, y=None, z=None):
        if type(x) is list:
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        return Point((self.y*other.z) - (self.z*other.y), (self.z*other.x) - (self.x*other.z), (self.x*other.y) - (self.y*other.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __str__(self):
        return str(self.x) + ', ' + str(self.y) + ', ' + str(self.z)


A = Point(list(map(float, input().split(' '))))
B = Point(list(map(float, input().split(' '))))
C = Point(list(map(float, input().split(' '))))
D = Point(list(map(float, input().split(' '))))

X = (B - A).cross(C - B)
Y = (C - B).cross(D - C)

PHI = round(math.degrees(math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))), 2)

print(PHI)