from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from runge_kutta import *
import numpy as np


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        # User inputs
        self.length = 1
        self.mass = 1
        self.friction = 0
        self.initial_angle = 1
        self.which_input_signal = ''

        # Plot clicked --button
        self.gui.plot.clicked.connect(self.plot_all)
        # Signal choice --radio buttons

        self.gui.sin_choice.toggled.connect(self.sin_selected)
        self.gui.rectungle_choice.toggled.connect(self.rectangle_selected)
        self.gui.triangle_choice.toggled.connect(self.triangle_selected)
        self.gui.zero_choice.toggled.connect(self.zero_selected)

    def take_user_inputs(self):
        self.length = float(self.gui.length_value.text())
        self.mass = float(self.gui.mass_value.text())
        self.friction = float(self.gui.friction_value.text())
        self.initial_angle = float(self.gui.angle_value.text())
        self.x_0 = [np.radians(self.initial_angle), 0]

    def sin_selected(self, selected):
        if selected:
            self.which_input_signal = 'sin'

    def triangle_selected(self, selected):
        if selected:
            self.which_input_signal = 'triangle'

    def rectangle_selected(self, selected):
        if selected:
            self.which_input_signal = 'rectangle'

    def zero_selected(self, selected):
        if selected:
            self.which_input_signal = 'zero'

    def prepare_data(self):
        self.take_user_inputs()
        self.parameters = {
            'friction': self.friction,
            'gravity': 9.81,
            'length': self.length,
            'mass': self.mass
        }
        data = calculate_state_variables(self.x_0, self.which_input_signal, self.parameters)
        self.split_data(**data)

    def split_data(self, time, state_var):
        [self.x0, self.x1] = state_var
        self.ts = time
        self.u = input_signal(self.ts, self.which_input_signal)

    # Graphs plotting

    def plot_all(self):
        self.prepare_data()
        # Input plot
        self.gui.graph_input.canvas.axes.clear()
        self.gui.graph_input.canvas.axes.plot(self.ts, self.u)
        self.gui.graph_input.canvas.draw()
        # Angle plot
        self.gui.graph_angle.canvas.axes.clear()
        self.gui.graph_angle.canvas.axes.plot(self.ts, self.x0 * (180 / np.pi))
        self.gui.graph_angle.canvas.draw()
        # Velocity plot
        self.gui.graph_velocity.canvas.axes.clear()
        self.gui.graph_velocity.canvas.axes.plot(self.ts, self.x1)
        self.gui.graph_velocity.canvas.draw()
