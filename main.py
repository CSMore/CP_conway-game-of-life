from src.game_of_life import GameOfLife
from src.visualization import animate_game, save_gif
from src.patterns import GLIDER, BLINKER, BLOCK, TOAD
from src.benchmark import run_benchmark


def generate_pattern_gif(name, pattern, steps=30):
    rows = len(pattern)
    cols = len(pattern[0])

    game = GameOfLife(
        rows=rows,
        cols=cols,
        initial_state=pattern
    )

    save_gif(
        game,
        steps=steps,
        path=f"images/{name}.gif",
        title=f"Conway's Game of Life - {name}"
    )


def main():
    generate_pattern_gif("glider", GLIDER, steps=30)
    generate_pattern_gif("blinker", BLINKER, steps=20)
    generate_pattern_gif("block", BLOCK, steps=20)
    generate_pattern_gif("toad", TOAD, steps=20)

    game = GameOfLife(
        rows=5,
        cols=5,
        initial_state=GLIDER
    )

    animate_game(
        game,
        steps=30,
        title="Conway's Game of Life - Glider"
    )

    run_benchmark()


if __name__ == "__main__":
    main()