# Conway's Game of Life

This project implements Conway's Game of Life using Python, NumPy, SciPy, and Matplotlib.

## Description

Conway's Game of Life is a cellular automaton that simulates the evolution of cells on a two-dimensional grid. Each cell can be alive or dead, and its state changes in each generation according to the number of living neighbors.

The rules used are:

- A living cell with fewer than 2 living neighbors dies from underpopulation.
- A living cell with 2 or 3 living neighbors survives.
- A living cell with more than 3 living neighbors dies from overpopulation.
- A dead cell with exactly 3 living neighbors becomes alive.

---

## Project Structure

```text
CP_conway-game-of-life/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── images/
│   ├── game_of_life.gif
│   ├── game_of_life_simulation.png
│   ├── performance_benchmark.png
│   └── loglog_performance.png
└── src/
    ├── __init__.py
    ├── game_of_life.py
    ├── visualization.py
    ├── benchmark.py
    └── patterns.py
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd CP_conway-game-of-life
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Dependencies

The project uses the following libraries:

- NumPy
- SciPy
- Matplotlib
- Pillow

---

## Execution

Run the main application:

```bash
python main.py
```

This will:

- Generate a GIF animation
- Display the live simulation
- Execute the performance benchmark
- Export benchmark graphs to the `images/` folder

---

## Included Patterns

The project includes several classic Conway patterns:

- Glider
- Blinker
- Block

Patterns are defined in:

```text
src/patterns.py
```

---

## Animation and Visualization

The simulation uses `matplotlib.animation.FuncAnimation` to display the evolution of the cellular automaton.

Generated files:

- `images/game_of_life.gif`
- `images/game_of_life_simulation.png`

---

## Benchmark

The benchmark evaluates the performance of the implementation using different grid sizes:

- 32x32
- 64x64
- 128x128
- 256x256
- 512x512
- 1024x1024

For each grid size, the average execution time per simulation step is measured.

The benchmark generates:

- `images/performance_benchmark.png`
- `images/loglog_performance.png`

---

## Complexity Analysis

The implementation updates the entire grid during each simulation step. Therefore, the execution time depends on the total number of cells.

If the grid contains:

```text
rows * cols
```

cells, every iteration must process all cells to determine their next state.

The current implementation uses vectorized operations with NumPy and convolution operations from SciPy to efficiently compute neighbors for all cells simultaneously.

The experimental benchmark shows behavior closer to linear growth relative to the total number of cells, especially when compared to a quadratic reference curve.

The log-log visualization also helps analyze scalability for larger grid sizes.

---

## Memory Usage

The simulation stores the current state of the grid as a NumPy array.

During execution, additional arrays are temporarily created for:

- Neighbor counting
- State transitions

As a result, memory usage increases proportionally with the number of cells in the grid.

---

## Limitations

Although the implementation is significantly faster than a pure Python nested-loop approach, large grids such as 1024x1024 still require noticeable processing time.

Potential future improvements include:

- Parallel execution
- GPU acceleration
- Numba integration
- Sparse matrix optimization

This version prioritizes readability, modularity, and clear object-oriented design.

---

## Generated Results

After execution, the following files are automatically generated inside the `images/` folder:

- GIF animation of the simulation
- Simulation screenshot
- Performance benchmark graph
- Log-log performance graph

---

## Technologies Used

- Python 3
- NumPy
- SciPy
- Matplotlib
- Pillow

---

## Author

Carolina Salas
