import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate_game(game, steps=100):

    fig, ax = plt.subplots()

    image = ax.imshow(
        game.get_state(),
        cmap="binary"
    )

    def update(frame):

        game.step()

        image.set_array(game.get_state())

        return [image]

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=steps,
        interval=100,
        blit=True
    )

    plt.title("Conway's Game of Life")

    plt.show()