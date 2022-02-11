from tkinter import *
from tkinter import messagebox
import sqlite3




### Entrar -> Ingreso directo a la APP si el usuario y la contraseña exiten en la BBDD.
def Entrar():
    
        miConexion=sqlite3.connect("Login BBDD")
        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM LOGIN")

        # miCursor.execute("SELECT * FROM LOGIN WHERE USUARIO=" + variable, "AND CONTRASEÑA=" + variable2)

        datos=miCursor.fetchall()

        for i in datos:
            print(i)

            if i[0]==entryUsuario.get() and i[1]==entryPassword.get():
                raiz.destroy()
                
        try:
            while i[0]!=entryUsuario.get() or i[1]!=entryPassword.get():
                messagebox.showwarning("ERROR", "Los datos ingresados son incorrectos o no esta registrado.")
                break
        finally:

            miConexion.commit()
            miConexion.close()


### Registrarse -> Boton Registrarse

def Registrarse():
    raiz.destroy()
    registro()
    miConexion=sqlite3.connect("Login BBDD")
    miCursor=miConexion.cursor()

    miCursor.execute(
        """
        CREATE TABLE LOGIN(
            USUARIO VARCHAR(50) PRIMARY KEY,
            CONTRASEÑA VARCHAR(50)
        )
        """
    )

    miConexion.commit()

    miConexion.close

    messagebox.showinfo("BBDD", "Base de Datos MAIN creada con EXITO!")

### Registro: Panel de Registro. Usuario y Contraseña
def registro():
    raiz2=Tk()

    miFrame3=Frame()
    miFrame3.pack()

    labelRegUsu=Label(miFrame3, text="Usuario: ")
    labelRegUsu.grid(row=1, column=1)
    entryRegUsu=Entry(miFrame3)
    entryRegUsu.grid(row=1, column=2)

    labelRegPass=Label(miFrame3, text="Contraseña: ")
    labelRegPass.grid(row=2, column=1)
    entryRegPass=Entry(miFrame3)
    entryRegPass.grid(row=2, column=2)

    miFrame4=Frame()
    miFrame4.pack()

    def insertbbdd():

        try:
            miConexion=sqlite3.connect("Login BBDD")
            miCursor=miConexion.cursor()

            datos=entryRegUsu.get(), entryRegPass.get()
            miCursor.execute("INSERT INTO LOGIN VALUES(?,?)", (datos))

            miConexion.commit()
            miConexion.close

            raiz2.destroy()
        
            login2()

        except:
            messagebox.showwarning("ERROR", "Usuario existente, ingrese otro nombre de usuario")

    botonRegistro=Button(miFrame4, text="Registrarse", width=10, height=2, command=insertbbdd)
    botonRegistro.grid(row=1, column=2)

    # Actualizo los datos de la Base de Datos
    miConexion=sqlite3.connect("Login BBDD")
    
    miConexion.commit()
    miConexion.close()

    raiz2.mainloop()

### New Login -> Se abre un nuevo Login, luego de registrarse
def login2():

    def Entrar2():

        miConexion=sqlite3.connect("Login BBDD")
        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM LOGIN")

        datos=miCursor.fetchall()

        for i in datos:
            print(i)

            if i[0]==entryNewUsu.get() and i[1]==entryNewPass.get():
                raiz3.destroy()
        
        try:
            while i[0]!=entryNewUsu.get() or i[1]!=entryNewPass.get():
                messagebox.showwarning("ERROR", "Los datos ingresados son incorrectos o no esta registrado.")
                break

        finally:
            miConexion.commit()
            miConexion.close()



    raiz3=Tk()


    miFrame=Frame()
    miFrame.pack()

    labelNewUsu=Label(miFrame, text="Usuario: ")
    labelNewUsu.grid(row=1, column=1)
    entryNewUsua=StringVar()
    entryNewUsu=Entry(miFrame,textvariable=entryNewUsua)
    entryNewUsu.grid(row=1, column=2)

    labelNewPass=Label(miFrame, text="Contraseña: ")
    labelNewPass.grid(row=2, column=1)
    entryNewPassa=StringVar()
    entryNewPass=Entry(miFrame, textvariable=entryNewPassa)
    entryNewPass.grid(row=2, column=2)

    miFrame2=Frame()
    miFrame2.pack()

    botonNewEntrar=Button(miFrame2, text="Entrar", width=10, height=2, command=Entrar2)
    botonNewEntrar.grid(row=1, column=1)

    raiz3.mainloop()



### Interfaz Login

        
raiz=Tk()

miFrame=Frame()
miFrame.pack()

labelUsuario=Label(miFrame, text="Usuario: ")
labelUsuario.grid(row=1, column=1)
entryUsuarioa=StringVar()
entryUsuario=Entry(miFrame, textvariable=entryUsuarioa)
entryUsuario.grid(row=1, column=2)

labelPassword=Label(miFrame, text="Contraseña: ")
labelPassword.grid(row=2, column=1)
entryPassworda=StringVar()
entryPassword=Entry(miFrame,textvariable=entryPassworda)
entryPassword.grid(row=2, column=2)

miFrame2=Frame()
miFrame2.pack()

botonEntrar=Button(miFrame2, text="Entrar", width=10, height=2, command=Entrar)
botonEntrar.grid(row=1, column=1)

botonRegistrarse=Button(miFrame2, text="Registrarse", width=10, height=2, command=Registrarse)
botonRegistrarse.grid(row=1, column=2)



raiz.mainloop()

