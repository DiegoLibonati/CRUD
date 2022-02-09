from tkinter import messagebox
import interfaz
import borrarCampos

def Activar():

    if interfaz.act.get()==1:
        interfaz.EntryID.config(state="normal")
        messagebox.showinfo("Base de Datos", "Se activo la casilla de ID, esto te permitira: \nActualizar\nLeer\nBorrar")

    else: 
        borrarCampos.borrarCampos()
        interfaz.EntryID.config(state="disabled")
        messagebox.showinfo("Base de Datos", "Se desactivo la casilla de ID, se borraron los datos de los casilleros")
    
  