# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:38:20 2024

@author: José Luis Vicén Cruz
"""

from Persona import Persona, Fecha
from Asignatura import lista_asignaturas

lista_alumnos = []

class Alumno(Persona):
    def __init__(self, nombre, apellidos, fnacimiento, genero, nie, beca):
        super().__init__(nombre, apellidos, fnacimiento, genero)
        self.nie = nie
        self.creditos_superados = 0         # Un alumno nuevo no tiene creditos superados
        self.beca = beca
        self.lista_asignaturas_alumno = []  # Un alumno nuevo no tiene asignaturas
        
    def __str__(self):
        return super().__str__()+f"\n- NIE: {self.nie}\n\
- Créditos superados: {self.creditos_superados}\n\
- Tiene beca: {self.beca}\n\
- Asignaturas: {self.lista_asignaturas_alumno}"

    def sumar_creditos(self, num_creditos):
        self.creditos_superados += num_creditos
    
    #Añadimos el código de asignatura a "lista_asignaturas_alumno"
    #Recorremos "lista_asignaturas", y a la asignatura seleccionada le sumamos 1 en el campo "cod_asignatura"
    def matricular(self, cod_asignatura):
        self.lista_asignaturas_alumno.append(cod_asignatura)
        for i in lista_asignaturas:
            if i.cod_asignatura == cod_asignatura:
                i.num_alumnos += 1
    
    #Justo lo contrario al método anterior "matricular()"
    def desmatricular(self, cod_asignatura):
        self.lista_asignaturas_alumno.remove(cod_asignatura)
        for i in lista_asignaturas:
            if i.cod_asignatura == cod_asignatura:
                i.num_alumnos -= 1
    
    #Utilizamos los métodos "desmatricular()" y "sumar_creditos()"
    def aprobar(self, cod_asignatura):
        self.desmatricular(cod_asignatura)
        for i in lista_asignaturas:
            if i.cod_asignatura == cod_asignatura:
                self.sumar_creditos(i.num_creditos)
    
if __name__ == "__main__":
    #Unos datos de prueba
    alumno1 = Alumno("Karim", "Benzema", Fecha("15","07","1991"),"Masculino","123123",True)
    alumno2 = Alumno("Luka", "Modric", Fecha("21","04","1995"),"Masculino","456789",True)
    lista_alumnos.append(alumno1)
    lista_alumnos.append(alumno2)




        

        
        