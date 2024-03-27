# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:36:22 2024

@author: Aidan
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("P170")
root.geometry("650x1000")

label_grado3 = Label(root, text="")
label_grado3.place(relx=0.5, rely=0.2, anchor=CENTER)

label_grado5 = Label(root, text="")
label_grado5.place(relx=0.5, rely=0.5, anchor=CENTER)

label_grado10 = Label(root, text="")
label_grado10.place(relx=0.5, rely=0.8, anchor=CENTER)

class grado3():
    def __init__(self, matematicas, arte):
        self.matematicas = matematicas
        self.arte = arte
        
    def porcentaje(self):
        calificacion_3 = self.matematicas + self.arte
        calificacion_grado3_100 = calificacion_3 * 100
        porcentaje_grado3 = calificacion_grado3_100 / 200
        label_grado3["text"] = porcentaje_grado3
        
class grado5():
    def __init__(self, matematicas, arte, ciencias):
        self.matematicas = matematicas
        self.arte = arte
        self.ciencias = ciencias
        
    def porcentaje(self):
        calificacion_5 = self.matematicas + self.arte + self.ciencias
        calificacion_grado5_100 = calificacion_5 * 100
        porcentaje_grado5 = calificacion_grado5_100 / 300
        label_grado5["text"] = porcentaje_grado5
        
class grado10():
    def __init__(self, matematicas, arte, ciencias, ingles):
        self.matematicas = matematicas
        self.arte = arte
        self.ciencias = ciencias
        self.ingles = ingles

    def porcentaje(self):
        calificacion_10 = self.matematicas + self.arte + self.ciencias + self.ingles
        calificacion_grado10_100 = calificacion_10 * 100
        porcentaje_grado10 = calificacion_grado10_100 / 400
        label_grado10["text"] = porcentaje_grado10
        
objeto_grado3 = grado3(9.5, 10)
objeto_grado5 = grado5(9.2, 10, 9)
objeto_grado10 = grado10(9, 10, 9.8, 10)

btn_grado3 = Button(root, text="Grado 3", command=objeto_grado3.porcentaje)
btn_grado3.place(relx=0.5, rely=0.1, anchor=CENTER)

btn_grado5 = Button(root, text="Grado 5", command=objeto_grado5.porcentaje)
btn_grado5.place(relx=0.5, rely=0.4, anchor=CENTER)

btn_grado10 = Button(root, text="Grado 10", command=objeto_grado10.porcentaje)
btn_grado10.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        

root.mainloop()