# import yangke.performance.cooling as cool
# import math
# import numpy as np
#
# pressure_larynx_total = 160.70  # 喉部压力全压 Pa
# pressure_larynx_dynamic = 160.7 - 120.49  # 喉部压力动压
# pressure_larynx_static = 120.49  # 喉部压力静压 Pa
# temperature_water_in = 39.06 + 273.15  # K
# temperature_water_out = 30.68 + 273.15  # K
# temperature_environment_dry = 30.29 + 273.15  # K
# temperature_environment_wet = 23.20 + 273.15  # K
# pressure_environment = 99470  # Pa
# flowrate_water = 5889 / 3600  # m3/s
# flowrate_air = 255.97 * 10000 / 3600  # m3/s
# ratio_air2water = 0.4844  # 气水比
# radius_of_fan = 10.36 / 2
#
# fai = cool.get_relative_humidity_of_moist_air(temperature_environment_dry, temperature_environment_wet,
#                                               pressure_environment)
#
# rho_air = cool.get_rho_of_moist_air(fai, temperature_environment_dry)
#
# area = math.pi * radius_of_fan * radius_of_fan
# flowrate_air_cal = cool.get_air_flow_m3ph(f=area, rho2=rho_air, p=pressure_larynx_dynamic)
# print(flowrate_air_cal)
# print(f"{flowrate_air}")
# -*- coding: utf-8 -*-


import sys
import os
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QLabel


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        menu = self.menuBar().addMenu("set")
        action1 = QAction("start_1", self)
        action2 = QAction("start_2", self)
        action1.triggered.connect(self.start_program)
        action2.triggered.connect(self.start_program)
        menu.addAction(action1)
        menu.addAction(action2)
        self.show()

    def start_program(self):
        w = QMainWindow()
        if 'start_1' in self.sender().text():
            print("start_dp")
            w.setCentralWidget(QLabel("测试start_dp"))
        elif self.sender().text() == "start_2":
            print("start_hpd")
            w.setCentralWidget(QLabel("测试start_hpd"))
        w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w1 = MainFrame()
    sys.exit(app.exec_())
