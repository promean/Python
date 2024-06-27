
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from Alumno import Alumno
from Alumno import lista_alumnos
from Fecha import Fecha
from PyQt5 import QtGui

class Alta_Alumno(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("practica_6m_alta_alumno.ui",self)
        self.actualiza_tabla()
        self.pushButton_3.clicked.connect(self.cerrar)
        self.pushButton_2.clicked.connect(self.anadir)
        self.pushButton.clicked.connect(self.limpiar)
        
        self.setWindowIcon(QtGui.QIcon("icons8-hacker-50.png"))  
        self.setWindowTitle("Dar de alta a un alumno")

    def anadir(self):
        nuevo_nombre=self.lineEdit.text()
        nuevo_apellido=self.lineEdit_2.text()
        nuevo_genero=self.comboBox.currentText() 
        nueva_fecha=self.dateEdit.date()
        nuevo_dni=self.lineEdit_3.text()
        nueva_beca=self.radioButton.isChecked()
        año=nueva_fecha.year()
        mes=nueva_fecha.month()
        dia=nueva_fecha.day()
        nuevo_fnac=Fecha(dia,mes,año)
        nuevo_alumno=Alumno(nuevo_nombre, nuevo_apellido,str(nuevo_fnac), str(nuevo_genero), nuevo_dni, nueva_beca)
        lista_alumnos.append(nuevo_alumno)
        self.actualiza_tabla()
                    
    def actualiza_tabla(self):
        for i in range(len(lista_alumnos)):
            self.tableWidget.setItem(i,0,QTableWidgetItem(lista_alumnos[i].nombre))   #nombre
            self.tableWidget.setItem(i,1,QTableWidgetItem(lista_alumnos[i].apellidos))  #apellidos
            self.tableWidget.setItem(i,2,QTableWidgetItem(str(lista_alumnos[i].fnacimiento))) #fecha
            self.tableWidget.setItem(i,3,QTableWidgetItem(lista_alumnos[i].genero)) #genero
            self.tableWidget.setItem(i,4,QTableWidgetItem(lista_alumnos[i].nie)) #nie
            self.tableWidget.setItem(i,5,QTableWidgetItem(str(lista_alumnos[i].beca)))  #beca
        
    def limpiar(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.dateEdit.setDate(QDate(2000,1,1))
        
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
        
        
    


