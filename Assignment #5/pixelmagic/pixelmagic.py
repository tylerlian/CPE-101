"""The module file for Project 5 Pixelmagic
CPE 101
Winter 2019
Author: 
    Tyler Lian
"""       

import sys

ARGS = sys.argv

def check_sys():

    '''Checks for errors in input of variables

    Args:
        ARGS (list): global list with user inputs

    Returns:
        file (file object): makes given file name into a variable

    '''

    modes = ["decode", "fade", "blur"]
    invalid = False
    try:
        for mode in modes:
            if ARGS[1] == mode:
                invalid = True
        if invalid == False:
            print("Error: Invalid Mode")
            sys.exit()
        elif len(ARGS) < 3:
            raise IndexError
        elif ARGS[1] == "fade" and len(ARGS) != 6:
            print("Usage: python pixelmagic.py fade " + \
                "<image> <row> <col> <radius>")
            sys.exit()
        elif ARGS[1] == "decode" and len(ARGS) != 3:
            print("Usage: python pixelmagic.py decode <image>")
            sys.exit()
        elif ARGS[1] == "blur" and (len(ARGS) < 3 or len(ARGS) > 4):
            print("Usage: python pixelmagic.py blur " + \
                "<image> <reach>")
            sys.exit()
        file = read_file(ARGS[2])
    except FileNotFoundError or PermissionError:
        print("Error: Unable to Open " + ARGS[2])
        sys.exit()
    except IndexError:
        print("Usage: python pixelmagic.py <mode> <image>")
        sys.exit()
    except:
        sys.exit()

    return file

def check_mode():
    
    '''Checks for errors in input of variables

    Args:
        None
    
    Returns:
        (string): returns the mode name

    '''

    if "decode" in ARGS:
        return "decode"
    if "fade" in ARGS:
        return "fade"
    if "blur" in ARGS:
        return "blur"

def append_image(file_name):

    '''Appends all pixels of an the image into a list

    Args:
        file_name (file object): object of given file name
    
    Returns:
        new_list (list): list of all the pixels

    '''

    new_list = []
    file_type = file_name.readline()
    dimensions = file_name.readline().split(" ")
    dimensions[1] = dimensions[1].strip("\n")

    new_list.append(dimensions[0])
    new_list.append(dimensions[1])
    new_list.append(file_name.readline().strip("\n"))

    while True:

        try:
            line = file_name.readline()
            line = line.split(" ")
            line[2] = line[2].strip("\n")
            for i in range(3):
                new_list.append(line[i])
        except:
            break

    file_name.close()

    return new_list

def read_file(file_name):

    '''Reads the file given

    Args:
        file_name (string): turns string into file variable
    
    Returns:
        file (file object): file variable of 

    '''

    file = open(file_name, 'r')

    return file

def write_image(file_name, pixels, header):
        
    '''Writes pixel list into an image file

    Args:
        file_name (file object): name of file to write on
        pixels (list): list of all pixels
        header (list): includes width, height, and max pixel
    
    Returns:
        (string): returns the mode name

    '''

    file = open(file_name, 'w')
    file.write('P3\n')
    file.write(str(header[0]) + ' ' + str(header[1]) + '\n')
    file.write(str(header[2]) + '\n')

    for counter in range(len(pixels)):
        file.write(str(pixels[counter][0]) + " " \
            + str(pixels[counter][1]) + " " \
            + str(pixels[counter][2]) + "\n")

    file.close()

def group_pixels(pixels):
        
    '''Groups pixels into rgb

    Args:
        pixels (list): list of individual digits
    
    Returns:
        full_list (list): list of list of rbg pixels

    '''

    full_list, pixel_list = [], []
    num_of_pixels = int(len(pixels) / 3)

    for i in range(num_of_pixels):
        pixel_list = []
        for j in range(3):
            pixel_list.append(pixels[j])
        del pixels[0:3]
        full_list.append(pixel_list)

    return full_list
    
def decode_puzzle(pixels, header):
    
    '''Decodes pixel puzzle

    Args:
        pixels (list): list of pixels
        header (list): includes width, height, and max_pixel
    
    Returns:
        pixels (list): updated pixel list

    '''
    
    max_pixel = int(header[2])
    length = len(pixels)

    for i in range(length):
        red = int(pixels[i][0])
        if red * 10 > max_pixel:
            red = max_pixel
        else:
            red *= 10

        for j in range(3):
            pixels[i][j] = red

    return pixels

def scale(x, y, row, col, radius):
    
    '''Creates scale value

    Args:
        x (int): x-coordinate
        y (int): y-coordinate
        col (int): column given by user
        row (int): row given by user
        radius (int): radius given by user
    
    Returns:
        scale_value (float): scale value to multiply pixel by

    '''
    try:
        dist_x = x - col
        dist_y = y - row

        distance = ((dist_x)**2 + (dist_y)**2)**0.5  

        scale_value = (radius - distance) / radius
    except:
        pass
        
    return scale_value

def fade_image(pixels, width, row, col, radius):
    
    '''Fades image given by values supplied by user

    Args:
        pixels (list): list of pixels
        width (int): width of image
        row (int): rows to fade
        col (int): columns to fade
        radius (int): radius given by user
    
    Returns:
        pixels (list): updated list of pixels

    '''

    for num, pixel in enumerate(pixels):

        x = num % width
        y = num / width 
        
        scale_value = scale(x, y, row, col, radius)

        if scale_value < 0.2:
            scale_value = 0.2

        for color in range(3):
            pixel[color] = int(int(pixel[color]) * scale_value)

    return pixels

def blur_image(pixels, width, reach):
    
    '''Blurs the image based on given reach

    Args:
        pixels (list): list of pixels
        width (int): width of image
        reach (int): reach between pixels
    
    Returns:
        new_pixel_list (list): updated list of pixels

    '''

    new_pixel_list = []
    length = len(pixels)
    for num, pixel in enumerate(pixels):
        x = num % width
        y = num // width
        total = 0
        new_pixel = [0,0,0]
        y_range = blur_range(y, reach)
        for y_coord in range(y_range[0], y_range[1]): 
            height = length // width
            if 0 <= y_coord and y_coord < height:
                x_range = blur_range(x, reach)
                for x_coord in range(x_range[0], x_range[1]):
                    if 0 <= x_coord and x_coord < width:
                        total += 1
                        try:
                            for color in range(3):
                                value = y_coord * width + x_coord
                                new_pixel[color] += \
                                    int(pixels[value][color])
                        except:
                            pass
        average_r, average_g, average_b = \
             new_pixel[0] // total, new_pixel[1] // total, \
                 new_pixel[2] // total
        if total == 0:
            new_pixel_list.append([new_pixel[0], \
                new_pixel[1],new_pixel[2]])
        else:
            new_pixel_list.append([average_r, average_g, average_b])  
    return new_pixel_list

def blur_range(coord, reach):
    
    '''Finds blur range

    Args:
        coord (int) = the location of the pixel
        reach (int) = how far should blur check for
    
    Returns:
        alist (list) = list including range of blur

    '''

    alist = []
    low_coord = coord - reach
    alist.append(low_coord)
    upp_coord = coord + reach + 1
    alist.append(upp_coord)
    return alist

def main():

    '''Runs program

    Args:
        None
    
    Returns:
        None

    '''

    file_name = check_sys()
    mode = check_mode()
    pixels = append_image(file_name)
    header = pixels[0:3] 
    pixels = pixels[3:len(pixels)]
    pixels = group_pixels(pixels)

    if mode == "decode":
        decode = decode_puzzle(pixels, header)
        write_image('decoded.ppm', decode, header)

    if mode == "fade":
        fade = fade_image(pixels, int(header[0]), int(ARGS[3]),\
                        int(ARGS[4]), int(ARGS[5]))
        write_image('faded.ppm', fade, header)
    
    if mode == "blur":
        try:
            reach = int(ARGS[4])
        except:
            reach = 4
        blur = blur_image(pixels, int(header[0]),\
            reach)
        write_image('blurred.ppm', blur, header)

if __name__== "__main__":
    main()