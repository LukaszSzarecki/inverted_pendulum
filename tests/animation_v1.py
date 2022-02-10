from runge_kutta import *

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

# --------------------------------------------------------------
# Parametry ukladu
params = {
    'friction': 0.0,
    'gravity': 9.81,
    'length': 1,
    'mass': 1
}
# warunki pocz
initial_angle = 5.0
x_0 = [np.radians(initial_angle), 0]  # teta_0, omega_0 - predkosc katowa poczatkowa

# t = 0
# h = 0.01
# tmax = 50
# czas = np.linspace(0, tmax, int(tmax//h))
# Dane sygnalu wejsciowego
ktory_sygnal = ''

czest_sin = 2  # [Hz - ilosc okresow w dziedzinie czasu]
czest_pros = 5  # [Hz]
czest_troj = 5 # [Hz]

# --------------------------------------------------------------
# Sygnaly
data = calculate_state_variables(x_0, ktory_sygnal,params)
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
plt.show()
