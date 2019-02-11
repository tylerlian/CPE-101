################################
# CPE 101
# Section: 15
# Assignment #2 : Tests
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# imports wordsearch file
import wordsearch as ws

# initializes empty lists
a = []
b = []
c = []

# initializes strings
x = "fourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfourfour"
y = "pailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpailpail"
z = "mathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmathmath"

# creates list for comparison
for i in range(5):
    a.append("fourfourfo")
    a.append("urfourfour")
for i in range(5):
    b.append("pailpailpa")
    b.append("ilpailpail")
for i in range(5):
    c.append("mathmathma")
    c.append("thmathmath")

# initializes variables - display function
q = ws.display(x)
r = ws.display(y)
s = ws.display(z)
# tests display function
assert q == a
assert r == b
assert s == c

# tests find_word function
word = ['pail', 'four', 'math']
q = ws.find_word(a, word)
assert q == "pail: word not found"
r = ws.find_word(b, word)
assert r == "pail: (FORWARD) row: 9 column: 2"
s = ws.find_word(c, word)
assert s == "pail: word not found"

# initialize lists
x = ["abcd"]
y = ["1234"]
z = ["a1b2c3"]
# tests reverse_string function
assert ws.reverse_string(x) == ["dcba"]
assert ws.reverse_string(y) == ["4321"]
assert ws.reverse_string(z) == ["3c2b1a"]

# initializes lists
x = ["abc", "123", "xyz"]
g = len(x[0])
y = ["abcd", "1234", "wxyz"]
h = len(y[0])
z = ["abcd", "1234", "wxyz", "7890"]
i = len(z[0])
# tests transpose_string function
assert ws.transpose_string(x, g) == ["a1x", "b2y", "c3z"]
assert ws.transpose_string(y, h) == ["a1w", "b2x", "c3y", "d4z"]
assert ws.transpose_string(z, i) == ["a1w7", "b2x8", "c3y9", "d4z0"]
