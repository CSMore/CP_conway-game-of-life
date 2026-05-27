from src.game_of_life import GameOfLife
from src.visualization import animate_game, save_gif
from src.patterns import GLIDER, BLINKER, BLOCK, TOAD
from src.benchmark import run_benchmark


def generate_pattern_gif(name, pattern, steps=30):
    """
    Generate and save a GIF animation for a given Game of Life pattern.
    """
    # Get the board dimensions from the selected pattern.
    rows = len(pattern)
    cols = len(pattern[0])
    
    # Create a game instance using the manual initial pattern.
    game = GameOfLife(
        rows=rows,
        cols=cols,
        initial_state=pattern
    )

    # Save the evolution of the pattern as a GIF file.
    save_gif(
        game,
        steps=steps,
        path=f"images/{name}.gif",
        title=f"Conway's Game of Life - {name}"
    )


def main():
    """
    Generate pattern animations, show a live simulation, and run the benchmark.
    """
    # Generate GIF animations for classic Conway patterns.
    generate_pattern_gif("glider", GLIDER, steps=30)
    generate_pattern_gif("blinker", BLINKER, steps=20)
    generate_pattern_gif("block", BLOCK, steps=20)
    generate_pattern_gif("toad", TOAD, steps=20)

    # Create a separate game instance for the live visualization.
    game = GameOfLife(
        rows=5,
        cols=5,
        initial_state=GLIDER
    )
    # Display the live animation.
    animate_game(
        game,
        steps=30,
        title="Conway's Game of Life - Glider"
    )

    # Run the performance benchmark and generate the result graphs.
    run_benchmark()


if __name__ == "__main__":
    main()