import interfaz
import sqlite3
from tkinter import END, messagebox

def Actualizar():

    miConexion=sqlite3.connect("BBDD Practica")

    miCursor=miConexion.cursor()

   # miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + interfaz.EntryNombre.get() +
    #    "', APELLIDO='" + interfaz.EntryApellido.get() +
     #   "', PASSWORD='" + interfaz.EntryPassword.get() +
      #  "', DIRECCION='" + interfaz.EntryDireccion.get() +
       # "', COMENTARIOS='" + interfaz.textoComentarios.get(1.0, END) +
        #"' WHERE ID=" + interfaz.EntryID.get())

    # Actualziacion parametrizada

    datos=interfaz.EntryNombre.get(), interfaz.EntryApellido.get(), interfaz.EntryPassword.get(), interfaz.EntryDireccion.get(), interfaz.textoComentarios.get("1.0", END)

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=? WHERE ID=" + interfaz.EntryID.get() ,(datos))

    messagebox.showinfo("Base de Datos", "Las casillas fueron actualizadas con exito")
            
    
    miConexion.commit()

    miConexion.close