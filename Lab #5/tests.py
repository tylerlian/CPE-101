################################
# CPE 101
# Section: 15
# Lab #5 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# import lab5 file
import lab5 as l5

# initialize lists
list1 = [1,3,4,2,5]
list2 = [5,3,1,7,9]
list3 = [4,8,12,3,-1]

# tests square_list function
assert l5.square_list(list1) == [1,9,16,4,25]
assert l5.square_list(list2) == [25,9,1,49,81]
assert l5.square_list(list3) == [16,64,144,9,1]

# tests add_n_all function
assert l5.add_n_all(list1, 2) == [3,5,6,4,7]
assert l5.add_n_all(list2, 0 ) == [5,3,1,7,9]
assert l5.add_n_all(list3, -1) == [3,7,11,2,-2]

# tests is_even_all function
assert l5.is_even_all(list1) == [False,False,True,True,False]
assert l5.is_even_all(list2) == [False,False,False,False,False]
assert l5.is_even_all(list3) == [True,True,True,False,False]

# tests are_positive function
assert l5.are_positive(list1) == [1,3,4,2,5]
assert l5.are_positive(list2) == [5,3,1,7,9]
assert l5.are_positive(list3) == [4,8,12,3]

# tests are_greater_than_n function
assert l5.are_greater_than_n(list1,2) == [3,4,5]
assert l5.are_greater_than_n(list2,3) == [5,7,9]
assert l5.are_greater_than_n(list3,0) == [4,8,12,3]

# tests are_divisible_by_n function
assert l5.are_divisible_by_n(list1,2) == [4,2]
assert l5.are_divisible_by_n(list2,-2) == []
assert l5.are_divisible_by_n(list3,3) == [12,3]

# tests sum_101 function
assert l5.sum_101(list1) == 15
assert l5.sum_101(list2) == 25
assert l5.sum_101(list3) == 26

# tests index_of_smallest function
assert l5.index_of_smallest(list1) == 0
assert l5.index_of_smallest(list2) == 2
assert l5.index_of_smallest(list3) == 4


