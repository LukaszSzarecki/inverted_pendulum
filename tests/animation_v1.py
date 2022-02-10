from runge_kutta import *

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use("TkAgg")

# --------------------------------------------------------------
# Parametry ukladu
params = {
    'friction': 1.0,
    'gravity': 9.81,
    'length': 1,
    'mass': 1
}
# warunki pocz
initial_angle = 5.0
x_0 = [np.radians(initial_angle), 0]  # teta_0, omega_0 - predkosc katowa poczatkowa

ktory_sygnal = 'sin'

# --------------------------------------------------------------
# Sygnaly
data = calculate_state_variables(x_0, ktory_sygnal, params)
ts = data['time']
[x0, x1] = data['state_var']
u = input_signal(ts, ktory_sygnal)

# --------------------------------------------------------------
# # Wyswietlanie
#
# Plot kata od czasu
plt.figure(1)
plt.title('Kąt odchylenia [degrees]')
plt.plot(ts, np.degrees(x0))
# plt.plot(ts, xs[:, :])
plt.grid()

# Plot predkosci katowej od czasu
plt.figure(2)
plt.title('Predkosc katowa [rad/s]')
plt.plot(ts, x1)
plt.grid()

# Plot sygnalu wejsciowego od czasu
plt.figure(3)
plt.title('Sygnal wejsciowy')
plt.plot(ts, u)

# --------------------------------------------------------------
# Animacja

import matplotlib.animation as animation

fig, ax = plt.subplots()

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
    ax.set_title("Symulacja odwróconego wahadła")
    return line,


def animate(i):
    line.set_ydata((0, wysokosc * np.cos(x0[i])))
    line.set_xdata((0, wysokosc * np.sin(x0[i])))
    return line,


ani = animation.FuncAnimation(fig, func=animate, init_func=init, frames=len(x0), interval=0.1, blit=True)

plt.show()
