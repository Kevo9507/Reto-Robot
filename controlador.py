# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:23:06 2024

@author: lab
"""

class RobotController:
    def __init__(self,model,view):
        self.model=model
        self.view= view
        
    def process(self):
        while True:
            command=input("Mover/detener o salir ")
            if command.lower() == "mover":
                elevation, rotation, length = self.view.get_user_input()
                self.model.move_elevation(elevation)
                self.model.move_rotation(rotation)
                self.model.move_length(length)
            elif command.lower() == "detener":
                self.model.stop_movement()
                self.view.display_message()
            elif command.lower() == "salir":
                break
            else:
                print("Escoga alguna de las opciones propuestas")
            