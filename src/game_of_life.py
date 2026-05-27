import numpy as np
from scipy.ndimage import convolve


class GameOfLife:

    # Kernel used to count the 8 neighbors around each cell.
    # The center is 0 because a cell should not count itself.    
    NEIGHBOR_KERNEL = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols

        # Manual initial state
        if initial_state is not None:
            self.grid = np.array(initial_state, dtype=int)

            # Validate that the provided pattern matches the board size
            if self.grid.shape != (rows, cols):
                raise ValueError(
                    f"Initial state must be of shape ({rows}, {cols})"
                )

        # Random initial state
        else:
            self.grid = np.random.randint(0, 2,
                (rows, cols), dtype=int)
            

    def step(self):

        '''Count living neighbors for every cell using convolution.
        mode="constant" treats cells outside the grid as dead.'''

        neighbors = convolve(self.grid,self.NEIGHBOR_KERNEL,mode="constant", cval=0)

        # Apply Conway's rules using boolean conditions
        alive = self.grid == 1

        # A dead cell with exactly 3 neighbors becomes alive
        born = (self.grid == 0) & (neighbors == 3)

        # A living cell survives with 2 or 3 neighbors
        survives = alive & ((neighbors == 2) | (neighbors == 3))

        # Update the grid for the next generation
        self.grid = (born | survives).astype(int)


    def run(self, steps):

        # Execute multiple generations
        for _ in range(steps):
            self.step()

    
    def get_state(self):
        # Return the current board state
        return self.grid