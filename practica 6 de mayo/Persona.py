# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:00:25 2024

@author: José Luis Vicén Cruz
"""

from Fecha import Fecha

class Persona:
    def __init__(self, nombre, apellidos, fnacimiento, genero):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fnacimiento = fnacimiento      #Es un objeto de la clase Fecha
        self.genero = genero
        
    def __str__(self):
        return f"- Nombre: {self.nombre}\n\
- Apellidos: {self.apellidos}\n\
- Fecha de nacimento: {self.fnacimiento}\n\
- Genero: {self.genero}"



if __name__ == "__main__":
    #Un dato de prueba
    persona_prueba = Persona("Kylian", "Mbapee",Fecha("12", "03", "2003"), "Masculino")
