################################
# CPE 101
# Section: 15
# Lab #4 : String Manipulation
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# imports character_manipulation file
import character_manipulation as cm

# changes a whole string to be 
def str_rot_13(my_str):

    # creates an array from string
    y = []
    x = my_str
    array_x = list(x)

    # adds letter to array after 13 letter change
    for item in array_x:
        y.append(cm.char_rot_13(item))

    # makes array into a string
    y = ''.join(y)
    return y

# tests if string is correctly changed
assert str_rot_13("anNB9") == "naAO9"
assert str_rot_13("cCbBa") == "pPoOn"
assert str_rot_13("vZqRQ") == "iMdED" 

# replaces letter in a string
def str_translate(my_str, old, new):
    x = my_str
    
    # if the letter is not in the string return
    if x.count(old) == 0:
        return x

    # if letter does exist in string    
    elif x.count(old) != 0:
        
        # replaces old letter with new
        array_x = list(x)
        z = array_x.index(old)
        array_x.pop(array_x.index(old))
        array_x.insert(z, new)
        y = ''.join(array_x)
        y = str(y)
        return str_translate(y, old, new)

# checks of string is changed properly
assert str_translate("dill", "l", "d") == "didd"
assert str_translate("bill", "b", "i") == "iill"
assert str_translate("oopsie poopsie", "o", "e") == "eepsie peepsie"