# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:23:06 2024

@author: lab
"""

class RobotView:
    


    def display_message(self):
        print("El sistema se detuvo")

    def get_user_input(self):
        elevation = int(input("INGRESE LA ELEVACION: "))
        rotation = int(input("INGRESE LA ROTACION: "))
        length = int(input("INGRESE LA LONGITUD: "))
        return elevation, rotation, length