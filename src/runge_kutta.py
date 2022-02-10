# Numerical method for ODEs Runge Kutta
import numpy as np

# timeline declaration
h = 0.001
tmax = 30

# details of the input signal
freq_sin = 2  # [Hz - ilosc okresow w dziedzinie czasu]
freq_rect = 5  # [Hz]
freq_trian = 5  # [Hz]


def input_signal(t, which_sig=''):
    if which_sig == 'sin':
        return 0.3 * np.sin(2 * np.pi * t * (freq_sin / tmax))
    elif which_sig == 'triangle':
        return 0.2 * np.arcsin(np.sin(2 * np.pi * t * (freq_trian / tmax))) / np.pi
    elif which_sig == 'rectangle':
        return 0.2 * np.sign(np.sin(2 * np.pi * t / (tmax / freq_rect)))
    elif which_sig == 'zero':
        return 0 * t
    else:
        return 0 * t


# equations of state variables
def pendelum_eq(x, t, sig, which_sig, params):
    b = params['friction']
    g = params['gravity']
    l = params['length']
    m = params['mass']

    return np.array([
        x[1],
        (3 * g / 2 * l) * np.sin(x[0]) - (3 * b / m * l * l) * x[1] - (3 / m * l * l) * sig(t, which_sig)
    ])


# mathematical pendulum equation
# -(b / m) * x[1] - (g / l) * np.sin(x[0]) + sig(t, which_sig)


# RungeKutte4 method

def rk4(x, fun, t, h, sig, which_sig, params):
    k1 = fun(x, t, sig, which_sig, params)
    k2 = fun(x + h / 2 * k1, t + h / 2, sig, which_sig, params)
    k3 = fun(x + h / 2 * k2, t + h / 2, sig, which_sig, params)
    k4 = fun(x + h * k3, t + h, sig, which_sig, params)

    x = x + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    t = t + h
    return (t, x)


def calculate_state_variables(x_0, ktory_sygnal, params):
    t = 0
    ts = np.array([t])
    xs = np.array([x_0])
    for i in range(int(tmax / h)):
        (t, x_0) = rk4(x_0, pendelum_eq, t, h, input_signal, ktory_sygnal, params)
        ts = np.append(ts, t)
        xs = np.concatenate((xs, np.array([x_0])))

    values = {
        'time': ts,
        'state_var': xs.transpose()
    }
    return values
