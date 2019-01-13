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
    x = input("Enter number #1: ")
    y = input("Enter number #2: ")
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

#
class Point:

    # self denotes this object itself
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    # official string representation
    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    # define equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# equation for euclidean distance
def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# runs all functions if file is run as main file
if __name__ == "__main__":
    
    # asks for user input to complete 'print_hello' function
    x = input("Enter your name: ")
    print(print_hello(x))

    # asks for user input to complete 'get_numbers' function
    print("Enter two numbers to recieve sum")
    print(get_numbers())

    # asks for user input to complete 'cube' function
    x = input("Enter number to cube it: ")
    print(cube(int(x)))

    # asks for user input to complete 'get_hypotenuse' function
    print("Enter the legs of your triangles to receive the hypotenuse")
    x = input("Enter leg #1: ")
    y = input("Enter leg #2: ")
    print(get_hypotenuse(int(x), int(y)))

    # asks for user input to complete 'do_math' function
    print("Enter x & y to input into equation '((3 * (x ** 2)) + (4 * y)) / (2 * x)'")
    x = input("Enter x: ")
    y = input("Enter y: ")
    print(do_math(int(x), int(y)))

    # asks for user input to complete 'is_positive' function
    x = input("Enter number to see if it is positive: ")
    print(is_positive(int(x)))

    # asks for user input to complete 'both_positive' function
    print("Input 2 numbers to see if they are both positive")
    x = input("Enter number #1: ")
    y = input("Enter number #2: ")
    print(both_positive(int(x), int(y)))

    print("Input coordinates for two points")
    x = input("Enter #1 x-cordinate: ")
    y = input("Enter #1 y-cordinate: ")
    a = input("Enter #2 x-cordinate: ")
    b = input("Enter #2 y-cordinate: ")
    p1 = Point(int(x), int(y)) 
    p2 = Point(int(a), int(b))
    print(get_distance(p1, p2))


