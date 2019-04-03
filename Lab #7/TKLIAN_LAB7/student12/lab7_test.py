import unittest
from wordsearch import *

PUZZLE = "POXYGENOEIASHGSPSODIBNWEPOTIHAPSOIHGXZLMVAWFPOIHBARBHPOSINBSBEIOHAFPOIHDIGOPAIHBEPOIHAGODIBAHPOLISHI"

def main():

    unittest.main()

class MyTest(unittest.TestCase):

    def test_find_word(self):
 
        self.assertEqual(find_word(PUZZLE, "OXYGEN"), "OXYGEN: (FORWARD) row: 0 column: 1")

        self.assertEqual(find_word(PUZZLE, "POLISH"), "POLISH: (FORWARD) row: 9 column: 3")

        self.assertEqual(find_word(PUZZLE, "DOG"), "DOG: (BACKWARD) row: 8 column: 8")

    def test_reverse_string(self):

        self.assertEqual(reverse_string("OXYGEN"), "NEGYXO")

        self.assertEqual(reverse_string("POLISH"), "HSILOP")
        
        self.assertEqual(reverse_string("DOG"), "GOD")
    
    def test_transpose_string(self):

        self.assertEqual(transpose_string("DASOASGAS", 3), "DOGAAASSS")

        self.assertEqual(transpose_string("OPDO", 2), "ODPO")

        self.assertEqual(transpose_string("OOPSOOPSOOPSOOPS", 4), "OOOOOOOOPPPPSSSS")

if __name__ == '__main__':
    main()
    