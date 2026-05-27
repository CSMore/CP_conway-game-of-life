import matplotlib.animation as animation
import matplotlib.pyplot as plt


def _build_animation(game, steps, interval, title):

    # Create figure
    fig, ax = plt.subplots(figsize=(6, 6))

    # Remove axes
    ax.axis("off")

    # Title
    ax.set_title(title)

    # Display initial state
    image = ax.imshow(
        game.get_state(),
        cmap="binary",
        interpolation="nearest",
        vmin=0,
        vmax=1
    )

    # Generation counter
    gen_text = ax.text(
        0.02,
        0.97,
        "Gen: 0",
        transform=ax.transAxes,
        color="red",
        fontsize=9,
        va="top"
    )

    
    def update(frame):
    # Update animation
        game.step()

        image.set_array(game.get_state())

        gen_text.set_text(f"Gen: {frame + 1}")

        return image, gen_text

    # Create animation
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=steps,
        interval=interval,
        blit=True,
        repeat=False
    )

    plt.tight_layout()

    return fig, ani


def animate_game(game, steps=100, title="Conway's Game of Life"):

    # Build and show live animation
    fig, ani = _build_animation(
        game=game,
        steps=steps,
        interval=100,
        title=title
    )

    plt.show()

    return ani


def save_gif(
    game,
    steps,
    path="images/game_of_life.gif",
    fps=8,
    title="Conway's Game of Life"
):

    """
    Save simulation as animated GIF.
    Requires Pillow.
    """

    # Build animation using the same logic as live visualization
    fig, ani = _build_animation(
        game=game,
        steps=steps,
        interval=1000 // fps,
        title=title
    )

    print("Generating GIF...")

    # Save GIF
    ani.save(
        path,
        writer="pillow",
        fps=fps
    )

    print(f"GIF saved successfully: {path}")

    # Save 
    screenshot_path = path.replace(".gif", "_simulation.png")
    plt.savefig(
        screenshot_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)