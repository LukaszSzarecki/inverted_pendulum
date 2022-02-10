# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sin_choice = QtWidgets.QRadioButton(self.centralwidget)
        self.sin_choice.setGeometry(QtCore.QRect(850, 470, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sin_choice.setFont(font)
        self.sin_choice.setObjectName("sin_choice")
        self.triangle_choice = QtWidgets.QRadioButton(self.centralwidget)
        self.triangle_choice.setGeometry(QtCore.QRect(850, 510, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.triangle_choice.setFont(font)
        self.triangle_choice.setObjectName("triangle_choice")
        self.rectungle_choice = QtWidgets.QRadioButton(self.centralwidget)
        self.rectungle_choice.setGeometry(QtCore.QRect(850, 550, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectungle_choice.setFont(font)
        self.rectungle_choice.setObjectName("rectungle_choice")

        self.zero_choice = QtWidgets.QRadioButton(self.centralwidget)
        self.zero_choice.setGeometry(QtCore.QRect(850, 590, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.zero_choice.setFont(font)
        self.zero_choice.setObjectName("zero_choice")

        self.plot = QtWidgets.QPushButton(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(840, 670, 140, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plot.setFont(font)
        self.plot.setObjectName("plot")
        self.length_value = QtWidgets.QLineEdit(self.centralwidget)
        self.length_value.setGeometry(QtCore.QRect(840, 100, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.length_value.setFont(font)
        self.length_value.setObjectName("length_value")
        self.mass_value = QtWidgets.QLineEdit(self.centralwidget)
        self.mass_value.setGeometry(QtCore.QRect(840, 170, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mass_value.setFont(font)
        self.mass_value.setObjectName("mass_value")
        self.friction_value = QtWidgets.QLineEdit(self.centralwidget)
        self.friction_value.setGeometry(QtCore.QRect(840, 240, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.friction_value.setFont(font)
        self.friction_value.setObjectName("friction_value")
        self.angle_value = QtWidgets.QLineEdit(self.centralwidget)
        self.angle_value.setGeometry(QtCore.QRect(840, 310, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.angle_value.setFont(font)
        self.angle_value.setObjectName("angle_value")
        self.graph_input = plot_graph(self.centralwidget)
        self.graph_input.setGeometry(QtCore.QRect(40, 40, 750, 230))
        self.graph_input.setObjectName("graph_input")
        self.graph_angle = plot_graph(self.centralwidget)
        self.graph_angle.setGeometry(QtCore.QRect(40, 290, 750, 230))
        self.graph_angle.setObjectName("graph_angle")
        self.graph_velocity = plot_graph(self.centralwidget)
        self.graph_velocity.setGeometry(QtCore.QRect(40, 530, 750, 230))
        self.graph_velocity.setObjectName("graph_velocity")
        self.lenght_label = QtWidgets.QLabel(self.centralwidget)
        self.lenght_label.setGeometry(QtCore.QRect(840, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lenght_label.setFont(font)
        self.lenght_label.setObjectName("lenght_label")
        self.mass_label = QtWidgets.QLabel(self.centralwidget)
        self.mass_label.setGeometry(QtCore.QRect(840, 140, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mass_label.setFont(font)
        self.mass_label.setObjectName("mass_label")
        self.friction_label = QtWidgets.QLabel(self.centralwidget)
        self.friction_label.setGeometry(QtCore.QRect(840, 210, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.friction_label.setFont(font)
        self.friction_label.setObjectName("friction_label")
        self.angle_label = QtWidgets.QLabel(self.centralwidget)
        self.angle_label.setGeometry(QtCore.QRect(840, 280, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.angle_label.setFont(font)
        self.angle_label.setObjectName("angle_label")
        self.signals_label = QtWidgets.QLabel(self.centralwidget)
        self.signals_label.setGeometry(QtCore.QRect(830, 440, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signals_label.setFont(font)
        self.signals_label.setObjectName("signals_label")
        self.input_gr_label = QtWidgets.QLabel(self.centralwidget)
        self.input_gr_label.setGeometry(QtCore.QRect(380, 10, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_gr_label.setFont(font)
        self.input_gr_label.setObjectName("input_gr_label")
        self.angle_gr_label = QtWidgets.QLabel(self.centralwidget)
        self.angle_gr_label.setGeometry(QtCore.QRect(380, 265, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.angle_gr_label.setFont(font)
        self.angle_gr_label.setObjectName("angle_gr_label")
        self.velocity_rg_label = QtWidgets.QLabel(self.centralwidget)
        self.velocity_rg_label.setGeometry(QtCore.QRect(380, 510, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.velocity_rg_label.setFont(font)
        self.velocity_rg_label.setObjectName("velocity_rg_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Inverted Pendelum"))
        self.sin_choice.setText(_translate("MainWindow", "sinusoidal"))
        self.triangle_choice.setText(_translate("MainWindow", "triangular"))
        self.rectungle_choice.setText(_translate("MainWindow", "rectangular"))
        self.zero_choice.setText(_translate("MainWindow", "zero"))
        self.plot.setText(_translate("MainWindow", "PLOT"))
        self.lenght_label.setText(_translate("MainWindow", "Length [m]"))
        self.mass_label.setText(_translate("MainWindow", "Mass [kg]"))
        self.friction_label.setText(_translate("MainWindow", "Friction "))
        self.angle_label.setText(_translate("MainWindow", "Angle [°]"))
        self.signals_label.setText(_translate("MainWindow", "Input signals:"))
        self.input_gr_label.setText(_translate("MainWindow", "Input signal"))
        self.angle_gr_label.setText(_translate("MainWindow", "angle(time)"))
        self.velocity_rg_label.setText(_translate("MainWindow", "angular velocity(time)"))
from graphs_plot import plot_graph


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())