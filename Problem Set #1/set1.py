################################
# CPE 101
# Section: 15
# Lab 1, Problem Set 1
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

if __name__ == "__main__":

    #### Problem #1 ####

    # initialize variables
    original_number = 0

    # obtains user input and makes the string an int
    user = input("Enter a number: ")
    number = int(user)

    # makes variable 'original_number' have the same value as 'number'
    original_number = number

    # uses the math equation for problem 1 on variable 'number'
    number = number * 2
    number = number + 10
    number = number / 2
    number = number - original_number
    number = int(number)

    # prints final output
    print(number)

    #### Problem #2 ####

    # initializes the variables
    user1, user2, sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, finalsum, finalnum = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # obtains user input
    user1 = input("Enter a number: ")
    user2 = input("Enter a number: ")

    # applies math equation for problem 2 to user inputted variables
    sum1 = int(user1) + int(user2)
    sum2 = sum1 + int(user2)
    sum3 = sum2 + sum1
    sum4 = sum3 + sum2
    sum5 = sum4 + sum3
    sum6 = sum5 + sum4
    sum7 = sum6 + sum5
    sum8 = sum7 + sum6

    # adds together all the sums created
    finalsum = int(user1) + int(user2) + sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8

    # divides the final value by the 7th sum
    finalnum = finalsum / sum5

    # outputs the final value
    print(finalnum)

    #### Problem #3 ####

    # initializes variables
    number = ""
    subtract = 0

    # gets input from user
    number = input("Enter a number: ")
    number = int(number)

    # splits number into 4 parts
    a = number // 1000
    b = (number - 1000 * a) // 100
    c = (number - 1000 * a - 100 * b) // 10
    d = (number - 1000 * a - 100 * b - 10 * c)

    # rearranges the original number backwards
    number2 = str(d) + str(b) + str(c) + str(a)

    # turns strings into int variables
    number2 = int(number2)

    # subtracts smaller number from larger number 
    big = max(number,number2)
    small = min(number,number2)
    subtract = big - small

    # splits the int into 4 parts
    a = subtract // 1000
    b = (subtract - 1000 * a) // 100
    c = (subtract - 1000 * a - 100 * b) // 10
    d = (subtract - 1000 * a - 100 * b - 10 * c)

    # adds together individual digits
    finishedsum = a + b + c + d
    
    # splits the int into 2 parts
    a = finishedsum // 10
    b = (finishedsum - 10 * a)

    # adds the variables together
    final = a + b

    #prints the final output
    print(final)

    #### Problem #4 ####

    # initialized variables
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0

    # obtains user input
    number = input("Enter a number: ")
    number = int(number)

    # removes the numbers after the decimal point
    number = number / 7
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