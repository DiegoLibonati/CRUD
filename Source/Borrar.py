import interfaz
import sqlite3
from tkinter import END, messagebox

def Borrar():

    miConexion=sqlite3.connect("BBDD Practica")

    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + interfaz.EntryID.get())

    messagebox.showinfo("Base de Datos", "Se borro con exito")
            
    
    miConexion.commit()

    miConexion.close