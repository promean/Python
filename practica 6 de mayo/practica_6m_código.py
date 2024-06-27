
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from alta_alumno_interfaz import Alta_Alumno
from ficha_alumno_interfaz import Ficha_Alumno
from Alumno import lista_alumnos, Alumno
from Fecha import Fecha
from ficha_profesor_interfaz import Ficha_Profesor
from Profesor import Profesor, lista_profesores
from Matricular_alumno_interfaz import Matricular_Alumno
from Asignatura import Asignatura, lista_asignaturas
from Desmatricular_alumno_interfaz import Desmatricular_Alumno
from Aprobar_alumno_interfaz import Aprobar_Alumno
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon


class Mi_ventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("practica_6m_menu_principal.ui", self)
        self.wAprobarAlumno=None
        self.wDesmatricularAlumno=None
        self.wMatricularAlumno=None
        self.wAltaAlumno=None
        self.wFichaAlumno=None
        self.wFichaProfesor=None
        self.actionAlta_alumno_2.triggered.connect(self.Alta_alumno)
        self.actionMatricular_alumno_2.triggered.connect(self.Ficha_alumno)
        self.actionMatricular_alumno.triggered.connect(self.Matricular_alumno)
        self.actionDesmatricular_alumno.triggered.connect(self.Desmatricular_alumno)
        self.actionAprobar_alumno.triggered.connect(self.Aprobar_alumno)
        self.actionFicha_profesor.triggered.connect(self.Ficha_profesor)
        self.actionAcerca_de.triggered.connect(self.Acerca_de)
        self.actionSalir_3.triggered.connect(self.Salir)
        
        self.setWindowIcon(QtGui.QIcon("icons8-hacker-50.png"))  
        self.setWindowTitle("Aplicación de gestión de alumnos 2.0")
      
    
    def Alta_alumno(self):
        if self.wAltaAlumno==None:
            self.wAltaAlumno= Alta_Alumno()
        self.wAltaAlumno.show()
    
    def Ficha_alumno(self):
        if self.wFichaAlumno==None:
            self.wFichaAlumno= Ficha_Alumno()
        self.wFichaAlumno.show()
    
    def Matricular_alumno(self):
        if self.wMatricularAlumno==None:
            self.wMatricularAlumno= Matricular_Alumno()
        self.wMatricularAlumno.show()
    
    def Desmatricular_alumno(self):
        if self.wDesmatricularAlumno==None:
            self.wDesmatricularAlumno= Desmatricular_Alumno()
        self.wDesmatricularAlumno.show()
    
    def Aprobar_alumno(self):
        if self.wAprobarAlumno==None:
            self.wAprobarAlumno= Aprobar_Alumno()
        self.wAprobarAlumno.show()
    
    def Ficha_profesor(self):
        if self.wFichaProfesor==None:
            self.wFichaProfesor= Ficha_Profesor()
        self.wFichaProfesor.show()
    
    def Acerca_de(self):
        dlg= QMessageBox(self)
        dlg.setWindowTitle("Acerca de")
        dlg.setText("Práctica de creación de ventanas para gestionar alumnos \n\
hecha por Marcelo Lara Salup :). Versión 2.0.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec_()
    
    def Salir(self):
        dlg= QMessageBox(self)
        dlg.setWindowTitle("Salir")
        dlg.setText("Desea cerrar la aplicación?")
        dlg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Question)
        dlg.exec_()
        boton=dlg.exec()
        if boton== QMessageBox.Yes:
            self.close()
            
    
  
#-- PROGRAMA PRINCIPAL--#

if __name__ == "__main__":
    profesor1 = Profesor("Carlo", "Ancelotti", Fecha("07","07","1975"), "Masculino", "0001")
    lista_profesores.append(profesor1)
    
    alumno1 = Alumno("Karim", "Benzema", Fecha("15","07","1991"),"Masculino","123123",True)
    alumno2 = Alumno("Luka", "Modric", Fecha("21","04","1995"),"Masculino","456789",True)
    lista_alumnos.append(alumno1)
    lista_alumnos.append(alumno2)
    
    asignatura1 = Asignatura("20105", "0001", 6, "T001", 0)
    asignatura2 = Asignatura("20205", "0001", 6, "T001", 0)
    asignatura3 = Asignatura("20305", "0001", 6, "T001", 0)
    lista_asignaturas.append(asignatura1)
    lista_asignaturas.append(asignatura2)
    lista_asignaturas.append(asignatura3)
    
    app = QApplication([])
    window = Mi_ventana()
    window.show()
    app.exec()
 
