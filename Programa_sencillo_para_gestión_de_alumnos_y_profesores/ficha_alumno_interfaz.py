from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from Alumno import Alumno
from Alumno import lista_alumnos
from Fecha import Fecha
from PyQt5 import QtGui

class Ficha_Alumno(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ficha_alumno_interfaz.ui",self)
        self.pushButton.clicked.connect(self.cerrar)
        self.pushButton_3.clicked.connect(self.limpiar)
        self.pushButton_2.clicked.connect(self.buscar)
        
        self.setWindowIcon(QtGui.QIcon("icons8-hacker-50.png"))  
        self.setWindowTitle("Ficha del alumno")
        
    def buscar(self):
        nie=self.lineEdit.text()
        Alumno=None
        for alumno in lista_alumnos:
            if alumno.nie==nie:
                Alumno = alumno
                break
        if Alumno == None:
            self.error()
        if Alumno != None:
            self.textEdit.setText(Alumno.nombre)
            self.textEdit_2.setText(Alumno.apellidos)
            self.textEdit_4.setText(Alumno.genero)
            self.textEdit_3.setText(str(Alumno.fnacimiento))
            self.textEdit_6.setText(str(Alumno.beca))
            self.textEdit_5.setText(str(Alumno.creditos_superados))

    def limpiar(self):
        self.lineEdit.setText("")
    
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
    
    def error(self):
        dlg= QMessageBox(self)
        dlg.setWindowTitle("Error")
        dlg.setText("Alumno no encontrado, introduzca otro nie")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Warning)
        dlg.exec_()
    
   