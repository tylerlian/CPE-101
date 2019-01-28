################################
# CPE 101
# Section: 15
# Lab 1, Problem Set 1
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

if __name__ == "__main__":

    # initialized variables
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0

    # obtains user input
    number = input("Enter a number: ")
    number = int(number)

    # removes the numbers after the decimal point
    number = number / 7
    print(number)
    number = number * (10 ** 6)
    number = int(number)

    # seperates all the digits apart
    a = number // 1000000
    b = (number - 1000000 * a) // 100000
    c = (number - 1000000 * a - 100000 * b) // 10000
    d = (number - 1000000 * a - 100000 * b - 10000 * c) // 1000
    e = (number - 1000000 * a - 100000 * b - 10000 * c - 1000 * d) // 100
    f = (number - 1000000 * a - 100000 * b - 10000 * c - 1000 * d - 100 * e) // 10
    g = (number - 1000000 * a - 100000 * b - 10000 * c - 1000 * d - 100 * e - 10 * f)

    # adds all the digits together
    final = b + c + d + e + f + g
    
    # outputs answer
    print(final)