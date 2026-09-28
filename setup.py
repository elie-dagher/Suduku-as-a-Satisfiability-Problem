import numpy as np

def createTrulyRandomGame(size: int):
    # Set of ints should be between 1 and the side length of the Sukoku board.
    valid_ints = {num: 0 for num in range(1, size + 1)}
    board = []
    rng = np.random.default_rng()

    # Create our board and place random ints, x represent blank values. Keep track of what numbers we are placing
    for i in range(size):
        res = []
        
        for j in range(size):
            place_int = rng.choice([True, False], p=[0.25, 0.75])

            if place_int == True:
                placement_num = int(rng.integers(1, size + 1))

                while valid_ints.get(placement_num, 0) >= size:
                    placement_num = int(rng.integers(1, size + 1))

                res.append(placement_num)
                valid_ints[placement_num] = valid_ints.get(placement_num, 0) + 1
            else:
                res.append("x")

        board.append(res)

    for line in board:
        print(line)

createTrulyRandomGame(4)