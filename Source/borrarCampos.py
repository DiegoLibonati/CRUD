import interfaz
from tkinter import END

def borrarCampos():
    interfaz.EntryID.delete(0, END)
    interfaz.EntryNombre.delete(0, END)
    interfaz.EntryApellido.delete(0, END)
    interfaz.EntryPassword.delete(0, END)
    interfaz.EntryDireccion.delete(0, END)
    interfaz.textoComentarios.delete(1.0, END)
