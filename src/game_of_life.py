import numpy as np


class GameOfLife:

    def __init__(self, rows, cols, initial_state=None):

        self.rows = rows
        self.cols = cols

        if initial_state is not None:
            self.grid = np.array(initial_state)

        else:
            self.grid = np.random.randint(0, 2, (rows, cols))

    def count_neighbors(self, row, col):

        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                if i == 0 and j == 0:
                    continue

                new_row = row + i
                new_col = col + j

                if (
                    0 <= new_row < self.rows
                    and 0 <= new_col < self.cols
                ):
                    neighbors += self.grid[new_row][new_col]

        return neighbors

    def step(self):

        new_grid = np.copy(self.grid)

        for row in range(self.rows):
            for col in range(self.cols):

                neighbors = self.count_neighbors(row, col)

                # Celda viva
                if self.grid[row][col] == 1:

                    if neighbors < 2 or neighbors > 3:
                        new_grid[row][col] = 0

                # Celda muerta
                else:

                    if neighbors == 3:
                        new_grid[row][col] = 1

        self.grid = new_grid

    def run(self, steps):

        for _ in range(steps):
            self.step()

    def get_state(self):

        return self.grid