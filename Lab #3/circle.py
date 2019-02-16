################################
# CPE 101
# Section: 15
# Lab 3: Circle
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# imports packages
import point as p

# creates circle class
class Circle:

    # initializes the variables x, y, z
    def __init__(self, x, y, z):
        self.center = p.Point(x, y)
        self.radius = z
    
    # creates alias for circle center and radius input
    def __repr__(self):
        return ("%s, %s") % (p.Point(self.center), self.radius)

    # checks for equality
    def __eq__(self, other):
        type(other) == Circle
        return self.center == other.center and self.radius == other.radius