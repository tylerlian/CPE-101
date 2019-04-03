################################
# CPE 101
# Section: 15
# Lab #6 : Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# imports system package
import lab6 as l6
import sys

# makes args list
args = sys.argv

list1 = ['0 0 3\n','1 abc 5\n']
list2 = ['1 abc ow23']
list3 = ['1 2 3','4  5 6\n','7 8 9\n']

assert l6.strip(list1) == ['0 0 3','1 abc 5']
assert l6.strip(list2) == ['1 abc ow23']
assert l6.strip(list3) == ['1 2 3','4  5 6','7 8 9']

assert l6.line_sep(list1) == ['0', '0', '3', '1', 'abc', '5']
assert l6.line_sep(list2) == ['1', 'abc', 'ow23']
assert l6.line_sep(list3) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

assert l6.check_values(l6.line_sep(list1)) == [5,0,1,9]
assert l6.check_values(l6.line_sep(list2)) == [1,0,2,1]
assert l6.check_values(l6.line_sep(list3)) == [9,0,0,45]

# -- impossible to test arg_check function 3 times --
# 1) if input only file name ("test1.txt"): file name
# 2) if input no file name: "Usage: [-s] file_name"
# 3) if input file name + '-s': file name
# Uncomment functions below to test individually
# assert l6.arg_check() == "test1.txt"
# assert l6.arg_check() == None
# assert l6.arg_check() == "test1.txt"

file_name1 = "test0.txt"
file_name2 = "test1.txt"
file_name3 = "test2.txt"

# prints out | int 3 float 1 other 2
assert l6.display(args, l6.check_values(l6.split_file(file_name1))) == None
# prints out | int 2 float 3 other 4
assert l6.display(args, l6.check_values(l6.split_file(file_name2))) == None
# prints out none because file does not exist
assert l6.display(args, l6.check_values(l6.split_file(file_name3))) == None

assert l6.split_file(file_name1) == ['abc123', '34', '2.34', 'h', '3333333', '2']
assert l6.split_file(file_name2) == ['hi', '34', '56.77', 'aef56', '5.6', '7.8', '23', 'blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah', 'g']
assert l6.split_file(file_name3) == None





