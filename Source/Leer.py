import interfaz
import sqlite3
from tkinter import END

def Leer():

    miConexion=sqlite3.connect("BBDD Practica")

    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + interfaz.EntryID.get())

    Datos=miCursor.fetchall()
    
    for i in Datos:

        interfaz.EntryNombre2.set(i[1])
        interfaz.EntryApellido2.set(i[2])
        interfaz.EntryPassword2.set(i[3])
        interfaz.EntryDireccion2.set(i[4])
        interfaz.textoComentarios.insert(1.0, i[5])
            
    
    miConexion.commit()

    miConexion.close

# interfaz.EntryNombre.get(), interfaz.EntryApellido.get(), interfaz.EntryPassword.get(), interfaz.EntryDireccion.get(), interfaz.textoComentarios.get(1.0, END))