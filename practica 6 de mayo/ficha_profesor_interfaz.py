from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from Fecha import Fecha
from Profesor import lista_profesores
from PyQt5 import QtGui

class Ficha_Profesor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ficha_profesor_interfaz.ui",self)
        self.pushButton.clicked.connect(self.cerrar)
        self.pushButton_3.clicked.connect(self.limpiar)
        self.pushButton_2.clicked.connect(self.buscar)
        
        self.setWindowIcon(QtGui.QIcon("icons8-hacker-50.png"))  
        self.setWindowTitle("Ficha del profesor")
        
    def buscar(self):
       codigo=self.lineEdit.text()
       Profesor=None
       for profesor in lista_profesores:
           if profesor.cod_profesor==codigo:
               Profesor = profesor
               break
       if Profesor== None:
           self.error()
       if Profesor!= None:
        self.textEdit.setText(Profesor.nombre)
        self.textEdit_2.setText(Profesor.apellidos)
        self.textEdit_4.setText(str(Profesor.fnacimiento))
        self.textEdit_3.setText(Profesor.genero)
       

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
        dlg.setText("Profesor no encontrado, introduzca otro código")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Warning)
        dlg.exec_()
    
