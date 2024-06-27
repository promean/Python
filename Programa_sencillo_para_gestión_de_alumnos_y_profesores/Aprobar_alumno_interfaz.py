from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from Alumno import Alumno
from Alumno import lista_alumnos
from Fecha import Fecha
from Asignatura import lista_asignaturas, Asignatura
from PyQt5 import QtGui
from Profesor import Profesor, lista_profesores

class Aprobar_Alumno(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("aprobar_alumno_interfaz.ui",self)
        self.pushButton.clicked.connect(self.aprobar)
        self.pushButton_3.clicked.connect(self.cerrar)
        self.pushButton_2.clicked.connect(self.limpiar)
        
        self.setWindowIcon(QtGui.QIcon("icons8-hacker-50.png"))  
        self.setWindowTitle("Aprobar alumno")
    
    def aprobar(self):
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
            self.textEdit_2.setText(Alumno.nombre)
            self.textEdit_3.setText(Alumno.apellidos)


            if Asignatura.cod_asignatura in Alumno.lista_asignaturas_alumno:
                self.aprobado()
                self.textEdit_4.setText("Aprobado")
                Alumno.lista_asignaturas_alumno.remove(Asignatura.cod_asignatura)
                Alumno.creditos_superados += 6
                Asignatura.num_alumnos -= 1
                
                
            elif Asignatura.cod_asignatura not in Alumno.lista_asignaturas_alumno:
                self.no_matriculado()
                self.textEdit_4.setText("No matriculado")
            self.textEdit_5.setText(str(Asignatura.num_alumnos))
            
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
        
    def aprobado(self):
        dlg= QMessageBox(self)
        dlg.setWindowTitle("Enhorabuena")
        dlg.setText("Este alumno ha sido aprobado exitosamente :)")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec_()
        
    def no_matriculado(self):
        dlg= QMessageBox(self)
        dlg.setWindowTitle("Aviso")
        dlg.setText("Este alumno no está matriculado en esta asignatura :(")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec_()