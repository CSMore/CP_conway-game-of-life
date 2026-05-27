from src.game_of_life import GameOfLife
from src.visualization import animate_game


initial_state = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

game = GameOfLife(
    rows=5,
    cols=5,
    initial_state=initial_state
)

animate_game(game, steps=100)