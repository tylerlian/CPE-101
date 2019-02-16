################################
# CPE 101
# Section: 15
# Lab 1, Problem Set 1
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

if __name__ == "__main__":

    # initializes the variables
    user1, user2, sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, finalsum, finalnum = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # obtains user input
    user1 = input("Enter your first number: ")
    user2 = input("Enter your second number: ")

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