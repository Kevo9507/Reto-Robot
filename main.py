# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:23:07 2024

@author: lab
"""

from modelo import RobotModel
from vista import RobotView
from controlador import RobotController

def main():
    model= RobotModel()
    view=RobotView()
    controller= RobotController(model, view)
    controller.process()

   


main()