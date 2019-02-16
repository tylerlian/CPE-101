################################
# CPE 101
# Section: 15
# Assignment #2 : Tests
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# imports wordsearch file
import wordsearch as ws

# initializes strings
x = "fourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfour"
y = "pailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpail"
z = "mathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmath"

# initializes a,b,c to Nonetype
a, b, c = None, None, None

# initializes variables - display function
q = ws.display(x)
r = ws.display(y)
s = ws.display(z)
# tests display function
assert q == a
assert r == b
assert s == c

# tests find_word function
word1, word2, word3 = "four", "pail", "matt"
q = ws.find_word(x, word1)
assert q == 0
r = ws.find_word(y, word2)
assert r == 0
s = ws.find_word(z, word3)
assert s == -1

# initialize lists
x = "abcd"
y = "1234"
z = "a1b2c3"
# tests reverse_string function
assert ws.reverse_string(x) == "dcba"
assert ws.reverse_string(y) == "4321"
assert ws.reverse_string(z) == "3c2b1a"

# initializes lists
x = "abc123xyz"
y = "abcde12345vwxyz67890jklmno"
z = "abcd1234wxyz7890"
# tests transpose_string function
assert ws.transpose_string(x, 3, 0) == "a1x"
assert ws.transpose_string(y, 5, 1) == "b2w7k"
assert ws.transpose_string(z, 4, 2) == "c3y9"
