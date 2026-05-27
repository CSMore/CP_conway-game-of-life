import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from src.game_of_life import GameOfLife


def save_plot(fig, path):

    """
    Save matplotlib figure.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Saved: {path}")


def run_benchmark():

    # Grid sizes
    sizes = [32, 64, 128, 256, 512, 1024]
    repetitions = 10
    # Store execution times
    times = []

    # -----------------------------
    # Benchmark execution
    # -----------------------------

    for size in sizes:

        print(f"Running benchmark for {size}x{size} grid...")

        game = GameOfLife(size, size)

        start = time.perf_counter()

        # Execute multiple iterations
        for _ in range(repetitions):
            game.step()

        end = time.perf_counter()

        # Average time per step
        average_time = (end - start) / repetitions

        times.append(average_time)

        print(f"{size}x{size}: {average_time:.6f} seconds")

    # Number of cells in each grid
    cells = np.array([size * size for size in sizes])
    times = np.array(times)

    # -----------------------------
    # Reference complexity curves
    # -----------------------------

    # O(n)
    ref_linear = (times[0] / cells[0]) * cells

    # # O(n^2)
    ref_quad = (times[0] / (cells[0] ** 2)) * (cells ** 2)

    # -----------------------------
    # Normal benchmark plot
    # -----------------------------

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    # Experimental results
    ax1.plot(
        cells,
        times,
        marker="o",
        label="Experimental Results"
    )

    # Complexity curves
    ax1.plot(
        cells,
        ref_linear,
        linestyle="--",
        label="O(n)"
    )

    ax1.plot(
        cells,
        ref_quad,
        linestyle="--",
        label="O(n²)"
    )

    # Labels
    ax1.set_xlabel("Number of Cells")
    ax1.set_ylabel("Average Time per Step (s)")

    # Title
    ax1.set_title("Game of Life - Performance Benchmark")

    # Legend and grid
    ax1.legend()
    ax1.grid(True)


    # Save figure
    save_plot(
        fig1,
        "images/performance_benchmark.png"
    )

    # -----------------------------
    # Log-Log plot
    # -----------------------------

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    # Experimental results in log-log scale
    ax2.loglog(
        cells,
        times,
        marker="o",
        label="Experimental Results"
    )

    # Reference curves in log-log scale
    ax2.loglog(
        cells,
        ref_linear,
        linestyle="--",
        label="O(n)"
    )

    ax2.loglog(
        cells,
        ref_quad,
        linestyle="--",
        label="O(n^2)"
    )

    # Labels
    ax2.set_xlabel("Number of Cells (log scale)")
    ax2.set_ylabel("Average Time per Step (log scale)")

    # Title
    ax2.set_title("Game of Life - Log-Log Performance")

    # Legend and grid
    ax2.legend()
    ax2.grid(True)

    # Save figure
    save_plot(
        fig2,
        "images/loglog_performance.png"
    )

    # Show plots
    plt.show()