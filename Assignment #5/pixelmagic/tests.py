"""The test file for Project 5 Pixelmagic
CPE 101
Winter 2019
Author: 
    Tyler Lian
"""

import pixelmagic as pt

list1 = [1,2,3,4,5,6,7,8,9]
pixel_list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = [1,6,4,3,2,3]
pixel_list2 = [[1,6,4],[3,2,3]]
list3 = [8,2,3]
pixel_list3 = [[8,2,3]]
assert pt.group_pixels(list1) == pixel_list1
assert pt.group_pixels(list2) == pixel_list2
assert pt.group_pixels(list3) == pixel_list3

d_pixel_list1 = [[10,10,10],[40,40,40],[70,70,70]]
d_pixel_list2 = [[10,10,10],[30,30,30]]
d_pixel_list3 = [[70,70,70]]
header = [300,300,70]
assert pt.decode_puzzle(pixel_list1, header) == d_pixel_list1
assert pt.decode_puzzle(pixel_list2, header) == d_pixel_list2
assert pt.decode_puzzle(pixel_list3, header) == d_pixel_list3

assert pt.scale(2, 4, 10, 10, 10) == 0
assert pt.scale(4, 2, 5, 5, 5) == 0.3675444679663241
assert pt.scale(7, 3, 0, 0, 1) == -6.615773105863909

list1 = [[2,2,2],[8,8,8],[14,14,14]]
list2 = [[2,2,2],[6,6,6]]
list3 = [[14,14,14]]
assert pt.fade_image(pixel_list1, 3, 3, 3, 3) == list1
assert pt.fade_image(pixel_list2, 2, 1, 5, 3) == list2
assert pt.fade_image(pixel_list3, 1, 1, 1, 1) == list3

pixel_list1 = [[1,2,3],[4,5,6],[7,8,9]]
pixel_list2 = [[1,6,4],[3,2,3]]
pixel_list3 = [[8,2,3]]
assert pt.blur_image(pixel_list1, 3, 2) == [[4,5,6], [4,5,6], [4,5,6]]
assert pt.blur_image(pixel_list2, 2, 1) == [[2,4,3], [2,4,3]]
assert pt.blur_image(pixel_list3, 1, 5) == [[8,2,3]]

assert pt.blur_range(1,4) == [-3, 6]
assert pt.blur_range(3,5) == [-2, 9]
assert pt.blur_range(9,2) == [7, 12]
