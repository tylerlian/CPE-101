################################
# CPE 101
# Section: 15
# Lab 3: Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

import sys

def max_of_two(x, y):
    
    # x is largest
    if x > y:
        return x

    # y is largest
    else:
        return y

def max_of_three(x, y, z):

    # x is largest
    if x > y and x > z:
        return x

    # y is largest    
    elif  y > z:
        return y

    # if x & y aren't largest z is    
    else: 
        return z

def mul(x, y):

    # multiplying by 0 = 0
    if x == 0 or y == 0:
        return 0

    # only positive = positive    
    elif (x < 0 and y < 0) or (y > 0 and x > 0):
        w = True
    
    # one negative * one positive = negative
    else:
        w = False

    # gets rid of negatives
    x, y = abs(x), abs(y)

    # initializes z as x
    z = x

    # multiplying process
    y -= 1
    while y > 0:
        x += z
        y -= 1  
    if w == False:
        x = 0 - x
    return x

def exp(x,y):
    
    # initializes z as x
    z = x

    # 0 power = 1
    if y == 0:
        return 1

    # 1st power = base    
    elif y == 1:
        return x

    # -1st power = 1 over base    
    elif y == -1:
        return 1 / x

    # positive power process    
    elif y > 0:
        y -= 1
        while y > 0:
            x = mul(x,z)
            y -= 1
        return x

    # negative power process    
    elif y < 0:
        y = abs(y)
        y -= 1
        while y > 0:
            x = mul(x,z)
            y -= 1
        return (1/x)


