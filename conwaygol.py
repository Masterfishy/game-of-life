import numpy as np
from time import sleep

def living_neighbors(cell, world):

    r, c = world.shape

    lower_row = max([ cell[0]-1, 0 ])
    upper_row = min([ cell[0]+2, r ])

    lower_col = max([ cell[1]-1, 0 ])
    upper_col = min([ cell[1]+2, c ])

    neighbors = world[lower_row:upper_row, lower_col:upper_col]

    return np.sum(neighbors) - world[cell]

def next_generation(world):
    x, y = world.shape
    future = np.copy(world)

    for i in range(x):
        for j in range(y):
            cell = (i, j)
            living = living_neighbors(cell, world)

            if world[cell]:
                future[cell] = 1 if living == 2 or living == 3 else 0
            else:
                future[cell] = 1 if living == 3 else 0

    return future

world = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

world = world.ravel()

while True:
    world = next_generation(world)
    print(world)
    sleep(2)
