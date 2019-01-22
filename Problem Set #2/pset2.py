################################
# CPE 101
# Section: 15
# Lab 2, Problem Set 2
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# import packages 
import math

#### print_hello ####

# inputs 'Hello' in front of given name
def print_hello(name):
    x = ("Hello " + name)
    return x

#### get_numbers ####

# returns the sum of two numbers inputted by user
def get_numbers():
    x = input("Enter a number: ")
    y = input("Enter a number: ")
    sum = int(x) + int(y)
    return sum

#### cube ####

# cubes the number given by user
def cube(x):
    y = x ** 3
    return y 

#### get_hypotenuse ####

# finds the hypotenuse of the triangle given
def get_hypotenuse(x, y):
    h = (x ** 2) + (y ** 2)
    h = (h ** .5)
    return h

#### do_math ####

# does math equation assigned with numbers inputted by user
def do_math(x, y):
    z = ((3 * (x ** 2)) + (4 * y)) / (2 * x)
    return z

#### is_positive ####

# tells user if their number is positive or not
def is_positive(x):
    return x > 0

#### both_positive ####

# uses definition 'is_positive' to show if two numbers inputted by user are both positive
def both_positive(x, y):
    z = is_positive(x)
    w = is_positive(y)
    return z == w == True

# creates coordinate points
class Point:

    # self denotes this object itself
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # official string representation
    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    # define equality
    def __eq__(self, other):
        type(other) == Point
        return self.x == other.x and self.y == other.y

# equation for euclidean distance
def get_distance(p1, p2):
    a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return round(a, 2)

if __name__ == "__main__":
    
    # tests the program to see if it works as it should
    assert print_hello("John") == "Hello John"
    
    # tells user that program works if no errors
    print("print_hello: Correct")

    # allows the user to see their sum
    print("The sum of the numbers inputted: " + str(get_numbers()))
    
    # tests the program to see if it works as it should
    assert cube(3) == 27
    assert cube(2) == 8
    assert cube(1) == 1

    # tells user that program works if no errors
    print("cube: Correct")

    # tests the program to see if it works as it should
    assert get_hypotenuse(3, 4) == 5
    assert get_hypotenuse(5, 12) == 13
    assert get_hypotenuse(8, 15) == 17

    # tells user that program works if no errors
    print("get_hypotenuse: Correct")

    # tests the program to see if it works as it should
    assert do_math(1, 1) == 3.5
    assert do_math(6, 0) == 9
    assert do_math(2, 4) == 7

    # tells user that program works if no errors
    print("do_math: Correct")

    # tests the program to see if it works as it should
    assert is_positive(3) == True
    assert is_positive(-2) == False
    assert is_positive(1) == True

    # tells user that program works if no errors
    print("is_positive: Correct")

    # tests the program to see if it works as it should
    assert both_positive(3, 4) == True
    assert both_positive(2, -2) == False
    assert both_positive(-1, -3) == False

    # tells user that program works if no errors
    print("both_positive: Correct")

    # creates points to test function
    p1 = Point(float(1),float(2))
    p2 = Point(float(2),float(2))
    p3 = Point(float(3),float(4))

    # tests the program to see if it works as it should
    assert get_distance(p1, p2) == 1.00
    assert get_distance(p1, p3) == 2.83
    assert get_distance(p2, p3) == 2.24

    print("get_distance: Correct")