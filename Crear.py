import interfaz
import sqlite3
from tkinter import END, messagebox

def Crear():

    miConexion=sqlite3.connect("BBDD Practica")

    miCursor=miConexion.cursor()

    #sql = """
    #INSERT INTO 
     #   DATOSUSUARIOS
      #  (NOMBRE_USUARIO, APELLIDO, PASSWORD, DIRECCION, COMENTARIOS)
    #VALUES
     #   (?, ?, ?, ?, ?)
    #"""
    # miCursor.execute(sql, (interfaz.EntryNombre.get(), interfaz.EntryApellido.get(), interfaz.EntryPassword.get(), interfaz.EntryDireccion.get(), interfaz.textoComentarios.get(1.0, END)))

    # Consultas Parametrizadas.
    datos=interfaz.EntryNombre.get(), interfaz.EntryApellido.get(), interfaz.EntryPassword.get(), interfaz.EntryDireccion.get(), interfaz.textoComentarios.get(1.0, END)

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

    miConexion.commit()

    miConexion.close

    messagebox.showinfo("Base de Datos", "La informacion brindada fue insertada con exito")