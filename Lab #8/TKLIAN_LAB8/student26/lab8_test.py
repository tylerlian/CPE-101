import unittest
from calcudoku import *

CAGES = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], \
        [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], \
        [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]

ZERO_CAGES = [[0, 3, 0, 5, 6], [0, 2, 1, 2], [0, 3, 3, 8, 13], \
        [0, 4, 4, 9, 14, 19], [0, 1, 7], [0, 3, 10, 11, 16], \
        [0, 4, 12, 17, 21, 22], [0, 2, 15, 20], [0, 3, 18, 23, 24]]

GRID = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

O_GRID = [[3,5,2,1,2],
          [5,2,3,1,2],
          [1,4,1,5,2],
          [2,2,4,1,5],
          [4,1,2,2,1]]

C_GRID = [[3,5,2,1,4],
          [5,1,3,4,2],
          [2,4,1,5,3],
          [1,2,4,3,5],
          [4,3,5,2,1]]

W_GRID = [[3,5,2,1,4],
          [5,1,3,1,2],
          [1,4,1,5,1],
          [1,2,4,1,5],
          [4,1,5,2,1]]

def main():

    unittest.main()

class MyTest(unittest.TestCase):

    def test_validate_all(self):
 
        self.assertEqual(validate_all(W_GRID, CAGES), False)

        self.assertEqual(validate_all(GRID, ZERO_CAGES), False)

        self.assertEqual(validate_all(C_GRID, CAGES), True)

    def test_validate_rows(self):

        self.assertEqual(validate_rows(O_GRID), False)

        self.assertEqual(validate_rows(C_GRID), True)
        
        self.assertEqual(validate_rows(W_GRID), False)
    
    def test_validate_cols(self):

        self.assertEqual(validate_cols(O_GRID), False)
        
        self.assertEqual(validate_cols(C_GRID), True)

        self.assertEqual(validate_cols(W_GRID), False)

    def test_validate_cages(self):

        self.assertEqual(validate_cages(O_GRID, ZERO_CAGES), False)

        self.assertEqual(validate_cages(W_GRID, CAGES), False)

        self.assertEqual(validate_cages(C_GRID, CAGES), True)

if __name__ == '__main__':
    main()
    