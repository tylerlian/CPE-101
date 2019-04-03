
from itertools import chain
from operator import eq, lt


def validate_all(grid, cages):
    #Return True if all 3 validation functions below return True and False otherwise.
    validity = [
        validate_rows(grid),
        validate_cols(grid),
        validate_cages(grid, cages)
    ]
    return all(validity)
    


def validate_rows(grid):
    #Return True if all rows contain no duplicate positive numbers and False otherwise.
    validity = []
    
    for row in grid:
        clean_row = [value for value in row if value != 0]
        unique_row = set(clean_row)
        validity.append(len(clean_row) == len(unique_row))

    return all(validity)


def validate_cols(grid):
    #Return True if all columns contain no duplicate positive numbers and False otherwise. It is recommended that you transpose the grid (convert its rows to columns and columns to rows) and pass this transposition to validate_rows to reuse your existing code.
    transposed_grid = list(zip(*grid))
    return validate_rows(transposed_grid)


def validate_cages(grid, cages):
    flat_grid = list(chain.from_iterable(grid))
    validity = []
    
    for cage in cages:
        cage_values = [flat_grid[index] for index in cage["cells"]]
        full = 0 not in cage_values
        
        if full:
            operator = eq
        else:
            operator = lt
        
        validity.append(operator(sum(cage_values), cage["sum"]))
        
    for cage in cages:
        cage_values = [flat_grid[index] for index in cage["cells"]]
    return all(validity)
    
        
if __name__ == "__main__":
    # initialize cages
    cage_count = int(input())
    cages = []
    for _index in range(cage_count):
        raw_cage = input()
        cage_description = list(map(int, raw_cage.split()))
        cage_sum = cage_description.pop(0)
        _cell_count = cage_description.pop(0)
        cells = cage_description
        
        cages.append({"sum": cage_sum, "cells": cells})
        
    # initialize grid
    grid = [[0]*5]*5
    
    # populate grid
    flat_grid = list(chain.from_iterable(grid))

    index = 0
    while index < 25:
        flat_grid[index] += 1
        
        if flat_grid[index] > 5:
            flat_grid[index] = 0
            index -= 1
        else:
            grid = [
                flat_grid[index:index + 5]
                for index in range(0, len(flat_grid), 5)
            ]
            
            if validate_all(grid, cages):
                index += 1
    
    # print grid
    grid = [
        flat_grid[index:index + 5]
        for index in range(0, len(flat_grid), 5)
    ]
    
    for row in grid:
        print(*row)
