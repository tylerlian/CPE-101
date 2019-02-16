################################
# CPE 101
# Section: 15
# Lab 1, Problem Set 1
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

if __name__ == "__main__":

    # initializes variables
    number = ""
    subtract = 0

    # gets input from user
    number = input("Enter a number: ")
    number = int(number)

    # splits number into 4 parts
    a = number//1000
    b = (number - 1000 * a)//100
    c = (number - 1000 * a - 100 * b)//10
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
    a = subtract//1000
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