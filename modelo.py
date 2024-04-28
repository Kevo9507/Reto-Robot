# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:21:40 2024

@author: lab
"""

class RobotModel:
    def __init__(self):
        self.total_elevation = 0
        self.total_rotation = 0
        self.total_length = 0
        self.detenido=0

    def move_elevation(self, value):
        self.total_elevation+= value
        print(f"Su ELEVACION es de: {self.total_elevation} grados")

    def move_rotation(self, value):
        self.total_rotation += value
        print(f"Su ROTACION es de: {self.total_rotation} grados")

    def move_length(self, value):
        self.total_length += value
        print(f"La LONGITUD es de {self.total_length} metros")

    def stop_movement(self):
        print(f"El valor de la elevación es de= {self.detenido} grados")
        print(f"El valor de la rotación es de= {self.detenido} grados")
        print(f"El valor de la longitud es de= {self.detenido} metros")
        
       

