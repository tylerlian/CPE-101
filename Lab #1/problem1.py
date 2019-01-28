################################
# CPE 101
# Section: 15
# Lab 1, Problem Set 1
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

if __name__ == "__main__":

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