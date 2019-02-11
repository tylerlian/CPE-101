################################
# CPE 101
# Section: 15
# Lab 3: Test Equalities
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# imports circle and point classes
import circle as c
import point as p

# creates three circles
cir1 = c.Circle(3, 6, 9)
cir2 = c.Circle(3, 6, 9)
cir3 = c.Circle(6, 3, 9)

# tests if circles are equal or not
assert cir1 == cir2
assert cir1 != cir3
assert cir2 != cir3
