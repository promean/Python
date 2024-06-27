# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:28:40 2024

@author: José Luis Vicén Cruz
"""

lista_asignaturas = []

class Asignatura:
    def __init__(self, cod_asignatura, cod_profesor, num_creditos, cod_titulacion, num_alumnos):
        self.cod_asignatura = cod_asignatura
        self.cod_profesor = cod_profesor
        self.num_creditos = num_creditos
        self.cod_titulacion = cod_titulacion
        self.num_alumnos = num_alumnos
    
    def __str__(self):
        return f"- Código asignatura: {self.cod_asignatura}\n\
- Código profesor: {self.cod_profesor}\n\
- Número de créditos: {self.num_creditos}\n\
- Código titulación: {self.cod_titulacion}\n\
- Número de alumnos: {self.num_alumnos}"

    def asignar_profesor(self, codigo_profesor):
        self.cod_profesor = codigo_profesor

if __name__ == "__main__":
    #Datos de prueba
    asignatura1 = Asignatura("20105", "0001", 6, "T001", 0)
    asignatura2 = Asignatura("20205", "0001", 6, "T001", 0)
    asignatura3 = Asignatura("20305", "0001", 6, "T001", 0)
    lista_asignaturas.append(asignatura1)
    lista_asignaturas.append(asignatura2)
    lista_asignaturas.append(asignatura3)

