# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:19:57 2024

@author: Jose Luis
"""

from Persona import Persona, Fecha
from Asignatura import lista_asignaturas

lista_profesores = []

class Profesor(Persona):
    def __init__(self, nombre, apellidos, fnacimiento, genero, cod_profesor):
        super().__init__(nombre, apellidos, fnacimiento, genero)
        self.cod_profesor = cod_profesor

    def __str__(self):
        return super().__str__()+f"\n- Código profesor: {self.cod_profesor}"
    
    def get_codigo_profesor(self):
        return self.cod_profesor
    
    
    #Buscamos en "lista_asignaturas" aquellas cuyo campo "cod_profesor" coincide con "cod_profesor" del profesor,
    #en cuyo caso se imprime la asignatura.
    def imprime_asignaturas(self):
        print("-"*30)
        encontrado = False
        for i in lista_asignaturas:
            if i.cod_profesor == self.cod_profesor:
                encontrado = True
                print(i)
                print("-"*30)
                
        if not encontrado:
            print("No imparte ninguna asignatura")

                
if __name__ == "__main__":
    #Unos datos de prueba
    profesor1 = Profesor("Carlo", "Ancelotti", Fecha("07","07","1975"), "Masculino", "0001")
    lista_profesores.append(profesor1)

