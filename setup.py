import numpy as np
from typing import List

def hashFunction(row: int, col: int) -> int:
    return (col << 16) | row

def createGame(size: int) -> List[List[int]]:
    if size % 2 != 0:
        print("Grid length must be even for a valid Sudoku game.")
        return 
    
    dct = [[0 for i in range(size)] for i in range(size)]

    # Set of ints should be between 1 and the side length of the Sukoku board.
    valid_ints = {num: 0 for num in range(1, size + 1)}
    rng = np.random.default_rng()

    # Create our board and place random ints, x represent blank values. Keep track of what numbers we are placing
    for row in range(size):
        for col in range(size):
            place_int = rng.choice([True, False], p=[0.25, 0.75])

            if place_int == True:
                placement_num = int(rng.integers(1, size + 1))

                while valid_ints.get(placement_num, 0) >= size:
                    placement_num = int(rng.integers(1, size + 1))

                dct[row][col] = placement_num

                valid_ints[placement_num] = valid_ints.get(placement_num, 0) + 1
            else:
                dct[row][col] = ("_")

    return dct

def solveGame(dct: List[List[int]]) -> List[List[int]]:
    """ 
    For a grid of length N, to place a value (v), our algorithm must satisfy:
    1) The cell (x, y) does contain a value.
    2) The row y has exactly one v:
        Atleast 1: v_1y or v_1y' or ... has no occurances of v for all y <= N
        At most 1: if v_1y then not v_1y'

    3) The col x has exactly one v:
        Atleast 1: v_x1 or v_x1' or ... has no occurance of v, for all y <= N
        At most 1: v_x1 then not v_x'1
    4)
    5)

    
    """

print(createGame(4))