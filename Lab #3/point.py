################################
# CPE 101
# Section: 15
# Lab 3: Point
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# creates point class
class Point:
    
    # initializes x, y
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # creates alias for point input
    def __repr__(self):
        return ("%s, %s") % (self.x, self.y)

    # checks for equality
    def __eq__(self, other):
        type(other) == Point
        return self.x == other.x and self.y == other.y   