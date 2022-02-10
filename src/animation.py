import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use("TkAgg")

def animate(x0):
    fig, ax = plt.subplots()

    ax.clear()
    line, = ax.plot((0, 0), (0, 0))
    left = -7
    right = 7
    wysokosc = 5
    plt.xlim((left, right))
    plt.ylim((left, right))

    def init():
        line.set_linewidth(2)

        ax.grid(True)
        ax.set_aspect('equal')
        ax.set_title("Inverted pendulum simulation - close window after each plot")
        return line,

    def update(i):
        line.set_ydata((0, wysokosc * np.cos(x0[i])))
        line.set_xdata((0, wysokosc * np.sin(x0[i])))
        return line,

    ani = animation.FuncAnimation(fig, func=update, init_func=init, frames=len(x0), interval=0.1, blit=True)
    plt.show()