################################
# CPE 101
# Section: 15
# Lab 3: Tests
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# imports packages
import pset3 as ps3

# tests max of two
assert ps3.max_of_two(3,5) == 5
assert ps3.max_of_two(-1,7) == 7
assert ps3.max_of_two(-10,-5) == -5

# tests max of 3
assert ps3.max_of_three(2,2,2) == 2
assert ps3.max_of_three(-6,-9,3) == 3
assert ps3.max_of_three(-6,-9,-3) == -3

# tests multiplication
assert ps3.mul(3,5) == 15
assert ps3.mul(5,-3) == -15
assert ps3.mul(-8,-9) == 72

# tests exponent
assert ps3.exp(2,3) == 8
assert ps3.exp(5,2) == 25
assert ps3.exp(0,0) == 1