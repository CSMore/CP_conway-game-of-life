"""
Classic initial patterns for Conway's Game of Life.
"""

# Glider: a small pattern that moves diagonally across the grid.
GLIDER = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Blinker: an oscillator that alternates between horizontal and vertical states.
BLINKER = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Block: a stable pattern that does not change between generations.
BLOCK = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

# Toad: an oscillator that repeats its shape every two generations.
TOAD = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
]