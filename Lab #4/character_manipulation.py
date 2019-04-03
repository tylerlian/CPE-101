################################
# CPE 101
# Section: 15
# Lab #4 : Character Manipulation
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# checks if the character is lowercase
def is_lower(char):

    # if character code is less than lowercase it is uppercase
    if ord(char) < ord("a") or ord(char) > ord("z"):

        # letter is uppercase
        return False

    else:

        # letter is lowercase
        return True

# test for lowercase letters
for i in range(1,128):
    char = chr(i)
    print(chr(i))
    print(is_lower(char))

# moves the character 13 characters forward
def char_rot_13(char):

    # checks if a letter
    if char.isalpha():
    
        # checks if it is lowercase
        if char.islower():
    
            # checks if letter goes past z
            if (ord(char) + 13) > ord("z"):
               
                # re-routes letter back to a
                value = ord("z") - ord(char)
                changed = 12 - value
                char = ord("a")
                c_char = char + changed
                return chr(c_char)
            else:
                
                # moves letter 13 forward
                c_char = ord(char) + 13
                return chr(c_char)
        
        # checks if a letter is uppercase
        elif char.isupper():
        
            # checks if letter goes past Z
            if (ord(char) + 13) > ord("Z"):
        
                # re-routes letter back to A
                value = ord("Z") - ord(char)
                changed = 12 - value
                char = ord("A")
                c_char = char + changed
                return chr(c_char)
                
            else:
        
                # moves letter 13 forward
                c_char = ord(char) + 13
                return chr(c_char)
    else:
        
        # if not a letter just returns
        return char

# tests if the characters correctly changes the characters
assert char_rot_13("n") == "a"
assert char_rot_13("N") == "A"
assert char_rot_13("9") == "9"

        


