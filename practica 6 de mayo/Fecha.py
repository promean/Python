# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:11:59 2024

@author: José Luis Vicén Cruz
"""
# La fecha la construimos con cadenas de caracteres
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
        if not self.escorrecta():
            self.dia = "00"
            self.mes = "00"
            self.año = "0000"
        
    #El formato de salida será "dd/mm/aaaa"
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    #Una fecha se considera válida si el día está entre 1 y 31, el mes entre 1 y 12 y el año entre 1900 y 2100
    def escorrecta(self):
        if (int(self.dia) in range(1,32)) and (int(self.mes) in range(1,13)) and (int(self.año) in range(1900,2101)):
            return True
        else:
            return False
        
if __name__ == "__main__":
    #Unos datos de prueba, una fecha correcta y otra incorrecta
    fecha_prueba = Fecha("25","02","2022")
    fecha_incorrecta = Fecha("45","02","2022")
