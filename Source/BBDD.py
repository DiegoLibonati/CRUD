import sqlite3
from tkinter import messagebox

def Conectar():

    try:

        miConexion=sqlite3.connect("BBDD Practica")

        miCursor=miConexion.cursor()

        miCursor.execute('''
        CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(10),
            PASSWORD VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(50)
        )''')

        miConexion.commit()

        miConexion.close

        messagebox.showinfo("Base de Datos", "La Base de Datos fue creada con exito")

    except:
        messagebox.showwarning("Base de Datos", "LA BASE DE DATOS YA EXISTE")
