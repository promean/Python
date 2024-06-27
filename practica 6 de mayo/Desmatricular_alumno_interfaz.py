from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from Alumno import Alumno
from Alumno import lista_alumnos
from Fecha import Fecha
from Asignatura import lista_asignaturas, Asignatura
from PyQt5 import QtGui

class Desmatricular_Alumno(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("desmatricular_alumno_interfaz.ui",self)
        
        self.pushButton.clicked.connect(self.desmatricular)
        self.pushButton_3.clicked.connect(self.cerrar)
        self.pushButton_2.clicked.connect(self.limpiar)
        
        self.setWindowIcon(QtGui.QIcon("icons8-hacker-50.png"))  
        self.setWindowTitle("Desmatricular alumno")
        
    
    def desmatricular(self):
        nie=self.lineEdit.text()
        codigo=self.lineEdit_2.text()
        
        Alumno=None
        Asignatura=None
        
        for alumno in lista_alumnos:
            if alumno.nie==nie:
                Alumno = alumno
                break
        
        
        for asignatura in lista_asignaturas:
            if asignatura.cod_asignatura==codigo:
                Asignatura = asignatura
                break
            
        if Alumno == None:
            self.error_nie()
        if Asignatura== None:
            self.error_asignatura()
            
        if Alumno != None and Asignatura != None:
            if Asignatura.cod_asignatura in Alumno.lista_asignaturas_alumno:
                Asignatura.num_alumnos-= 1
                self.desmatriculado()
                self.lineEdit_5.setText(Alumno.nombre)
                self.lineEdit_6.setText(Alumno.apellidos)
                self.lineEdit_7.setText(str(Asignatura.num_alumnos))
                Alumno.lista_asignaturas_alumno.remove(Asignatura.cod_asignatura)
                
               
                
            else:
                self.desmatriculado_antes()
            
        
            
    def limpiar(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
    
    def cerrar(self):
        dlg= QMessageBox(self)
        
        dlg.setWindowTitle("Salir")
        dlg.setText("Desea cerrar la ventana?")
        dlg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Question)
        
        dlg.exec_()
        
        boton=dlg.exec()
        if boton== QMessageBox.Yes:
            self.close()
    
    def error_nie(self):
        dlg= QMessageBox(self)
        
        dlg.setWindowTitle("Error")
        dlg.setText("Este nie no existe")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Warning)
        
        dlg.exec_()
    
    def error_asignatura(self):
        dlg= QMessageBox(self)
        
        dlg.setWindowTitle("Error")
        dlg.setText("Este código de asignatura no existe")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Warning)
        
        dlg.exec_()
        
    def desmatriculado(self):
        dlg= QMessageBox(self)
        
        dlg.setWindowTitle("Enhorabuena")
        dlg.setText("Este alumno ha sido desmatriculado exitosamente :)")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        
        dlg.exec_()
        
    def desmatriculado_antes(self):
        dlg= QMessageBox(self)
        
        dlg.setWindowTitle("Aviso")
        dlg.setText("Este alumno ya estaba desmatriculado")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        
        dlg.exec_()