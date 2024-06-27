# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:19:01 2022

@author: Jose Luis
"""

from Alumno import Alumno, Fecha, lista_alumnos, lista_asignaturas
from Profesor import lista_profesores

# Pedimos todos los datos, creamos un nuevo objeto de la clase Alumno y lo añadimos a "lista_alumnos"
def alta_alumno():
    print("ALTA DE ALUMNO")
    nombre = input("- Nombre: ")
    apellidos = input("- Apellidos: ")
    print("- Fecha de nacimiento: ")
    dia = input("\t\t- Dia: ")
    mes = input("\t\t- Mes: ")
    anyo = input("\t\t- Año: ")
    genero = input("- Genero: ")
    nie = input("- NIE: ")
    if input("- Tiene beca? (Y/N)").upper() == "Y":
        beca = True
    else:
        beca = False
    nuevo_alumno = Alumno(nombre, apellidos, Fecha(dia, mes, anyo), genero, nie, beca)
    lista_alumnos.append(nuevo_alumno)



#FUNCIONES DE BÚSQUEDA EN LAS TRES LISTAS
#Si el elemento buscado existe en la lista de objetos, devuelven el objeto
#Si no, devuelven "None"
def existe_alumno(nie):
   for i in lista_alumnos:
       if i.nie == nie:
           return i
   return None

def existe_asignatura(codigo_asignatura):
   for i in lista_asignaturas:
       if i.cod_asignatura == codigo_asignatura:
           return i
   return None

def existe_profesor(codigo_profesor):
   for i in lista_profesores:
       if i.cod_profesor == codigo_profesor:
           return i
   return None
#FIN DE FUNCIONES DE BÚSQUEDA EN LAS TRES LISTAS

# Si el alumno existe, lo imprime
def ficha_alumno():
    print("FICHA DE ALUMNO")
    nie = input("- NIE del alumno a buscar: ")
    alumno = existe_alumno(nie)
    if alumno != None:
        print(alumno)
    else:
        print(f"El alumno con NIE: {nie} no existe.")

#FUNCIONES PARA MATRICULAR, DESMATRICULAR Y APROBAR
#Son funciones idénticas, sólo cambia la acción concreta a realizar
#Se podría mejorar utilizando una única función a la que le pasaríamos el número de opción
def matricular_alumno():
    print("MATRICULAR ALUMNO")
    nie = input("- NIE del alumno: ")
    alumno = existe_alumno(nie)
    if alumno != None:
        cod_asignatura = input("- Código asignatura: ")
        asignatura = existe_asignatura(cod_asignatura)
        if asignatura != None:
            alumno.matricular(asignatura.cod_asignatura)
        else:
            print(f"La asignatura de código {cod_asignatura} no existe")
    else:
        print(f"El alumno con NIE: {nie} no existe.")
    
def desmatricular_alumno():
    print("DESMATRICULAR ALUMNO")
    nie = input("- NIE del alumno: ")
    alumno = existe_alumno(nie)
    if alumno != None:
        cod_asignatura = input("- Código asignatura: ")
        asignatura = existe_asignatura(cod_asignatura)
        if asignatura != None:
            alumno.desmatricular(asignatura.cod_asignatura)
        else:
            print(f"La asignatura de código {cod_asignatura} no existe")
    else:
        print(f"El alumno con NIE: {nie} no existe.")

def aprobar_alumno():
    print("APROBAR ALUMNO")
    nie = input("- NIE del alumno: ")
    alumno = existe_alumno(nie)
    if alumno != None:
        cod_asignatura = input("- Código asignatura: ")
        asignatura = existe_asignatura(cod_asignatura)
        if asignatura != None:
            alumno.aprobar(asignatura.cod_asignatura)
        else:
            print(f"La asignatura de código {cod_asignatura} no existe")
    else:
        print(f"El alumno con NIE: {nie} no existe.")
#FIN DE FUNCIONES PARA MATRICULAR, DESMATRICULAR Y APROBAR

# Si el profesor existe, imprimimos su ficha y todas sus asignaturas
def ficha_profesor():
    print("FICHA DE PROFESOR")
    cod_profesor = input("- Código de profesor: ")
    profesor = existe_profesor(cod_profesor)
    if profesor != None:
        print(profesor)
        profesor.imprime_asignaturas()
    else:
        print(f"El profesor con código: {cod_profesor} no existe.")



# MAIN
while True:
    print("\n  MENÚ PRINCIPAL")
    print("------------------")
    print("1- Alta alumno")
    print("2- Ficha alumno")
    print("3- Matricular alumno")
    print("4- Desmatricular alumno")
    print("5- Aprobar alumno")
    print("6- Ficha profesor")
    print("7- Salir")
    print("------------------")
    opcion = input("Selecione opción: ")
    
    if opcion == "1":
        alta_alumno()
    elif opcion == "2":
        ficha_alumno()
    elif opcion == "3":
        matricular_alumno()
    elif opcion == "4":
        desmatricular_alumno()
    elif opcion == "5":
        aprobar_alumno()
    elif opcion == "6":
        ficha_profesor()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")
    
