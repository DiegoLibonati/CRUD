from tkinter import messagebox
import interfaz

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "Desea salir de la aplicacion")

    if valor=="yes":
        interfaz.raiz.destroy()