from tkinter import *
from tkinter import messagebox, END
from PIL import ImageTk, Image
import BBDD
import Licencia
import AcercaDe
import sqlite3


############################################### Registrarse -> Boton Registrarse ##################################################################

def Registrarse():
    #raiz.destroy()
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


############################################### Registro: Panel Usuario y Contraseña ##################################################################
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
    entryRegPass=Entry(miFrame3, show="*")
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

            #raiz2.destroy()
        
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


############################################### New Login, luego de Registrarse ##################################################################
def login2():

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
    entryNewPass=Entry(miFrame, textvariable=entryNewPassa, show="*")
    entryNewPass.grid(row=2, column=2)



    def Entrar2():

    
        miConexion=sqlite3.connect("Login BBDD")
        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM LOGIN")

        datos=miCursor.fetchall()

        for i in datos:
            print(i)

            if i[0]==entryNewUsu.get() and i[1]==entryNewPass.get():
                Main()
                
                
        try:
            while i[0]!=entryNewUsu.get() or i[1]!=entryNewPass.get():
                messagebox.showwarning("ERROR", "Los datos ingresados son incorrectos o no esta registrado.")
                break

        finally:
            miConexion.commit()
            miConexion.close()

    miFrame2=Frame()
    miFrame2.pack()

    botonNewEntrar=Button(miFrame2, text="Entrar", width=10, height=2, command=Entrar2)
    botonNewEntrar.grid(row=1, column=1)

    raiz3.mainloop()

############################################### Programa Principal ##################################################################
def Main():

    raizMain=Toplevel(raiz)
    miMenu=Menu(raizMain)
    raizMain.config(menu=miMenu,width=300, height=600)
    raizMain.title("Operaciones CRUD [BBDD]")


    ############################## Creacion de Frame
    miFrameMain=Frame(raizMain)
    miFrameMain.pack()

    ############################### Entry + Label + CheckButton ID:
    LabelID=Label(miFrameMain, text="ID: ", justify="right")
    LabelID.grid(row=1, column=1, columnspan=2, sticky="EW")
    EntryID=Entry(miFrameMain)
    EntryID.grid(row=1, column=3, columnspan=2, sticky="EW", padx=20, pady=20)
    EntryID.config(state="disabled")

    act=IntVar() 

    def borrarCampos():
        EntryID.delete(0, END)
        EntryNombre.delete(0, END)
        EntryApellido.delete(0, END)
        EntryPassword.delete(0, END)
        EntryDireccion.delete(0, END)
        textoComentarios.delete(1.0, END)

    def Activar():

        if act.get()==1:
            EntryID.config(state="normal")
            messagebox.showinfo("Base de Datos", "Se activo la casilla de ID, esto te permitira: \nActualizar\nLeer\nBorrar")

        else: 
            borrarCampos()
            EntryID.config(state="disabled")
            messagebox.showinfo("Base de Datos", "Se desactivo la casilla de ID, se borraron los datos de los casilleros")

    miFrame2Main=Frame(raizMain)
    miFrame2Main.pack()
    LabelBoton=Label(miFrame2Main, text="Opciones: ", justify="left", anchor="w")
    LabelBoton.grid(row=0, column=0)
    CheckID=Checkbutton(miFrame2Main, text="Acticar ID para BUSQUEDAS",  variable=act, onvalue=1, offvalue=0, command=Activar, justify="left", anchor="w")
    CheckID.grid(row=1, column=4)

    ############################### Entry + Label Nombre:
    EntryNombre2=StringVar()
    LabelNombre=Label(miFrameMain, text="Nombre: ")
    LabelNombre.grid(row=2, column=1, columnspan=2, sticky="EW")
    EntryNombre=Entry(miFrameMain, textvariable=EntryNombre2)
    EntryNombre.grid(row=2, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

    ############################### Entry + Label Apellido:
    EntryApellido2=StringVar()
    LabelApellido=Label(miFrameMain, text="Apellido: ")
    LabelApellido.grid(row=3, column=1, columnspan=2, sticky="EW")
    EntryApellido=Entry(miFrameMain, textvariable=EntryApellido2)
    EntryApellido.grid(row=3, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

    ############################### Entry + Label Password:
    EntryPassword2=StringVar()
    LabelPassword=Label(miFrameMain, text="Password: ")
    LabelPassword.grid(row=4, column=1, columnspan=2, sticky="EW")
    EntryPassword=Entry(miFrameMain, show="*", textvariable=EntryPassword2)
    EntryPassword.grid(row=4, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

    ############################### Entry + Label Direccion:
    EntryDireccion2=StringVar()
    LabelDireccion=Label(miFrameMain, text="Direccion: ")
    LabelDireccion.grid(row=5, column=1, columnspan=2, sticky="EW")
    EntryDireccion=Entry(miFrameMain, textvariable=EntryDireccion2)
    EntryDireccion.grid(row=5, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

    ############################### Cajon de Texto + Label Comentarios:
    LabelComentarios=Label(miFrameMain, text="Comentarios: ")
    LabelComentarios.grid(row=6, column=1, columnspan=2, sticky="EW")
    textoComentarios=Text(miFrameMain, width=16, height=5)
    textoComentarios.grid(row=6, column=3, columnspan=2, sticky="EW", padx=20, pady=20)
    Scroll=Scrollbar(miFrameMain, command=textoComentarios.yview)
    Scroll.grid(row=6, column=5, sticky="nsew")
    textoComentarios.config(yscrollcommand=Scroll.set)

    ############################### Botones

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
        # miCursor.execute(sql, (main.EntryNombre.get(), main.EntryApellido.get(), main.EntryPassword.get(), main.EntryDireccion.get(), main.textoComentarios.get(1.0, END)))

        # Consultas Parametrizadas.
        datos=EntryNombre.get(), EntryApellido.get(), EntryPassword.get(), EntryDireccion.get(), textoComentarios.get(1.0, END)

        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

        miConexion.commit()

        miConexion.close

        messagebox.showinfo("Base de Datos", "La informacion brindada fue insertada con exito")

    BotonCreate=Button(miFrameMain, text="Create", width=8, height=1, command=Crear)
    BotonCreate.grid(row=10, column=1, padx=10, pady=10)

    def Leer():

        miConexion=sqlite3.connect("BBDD Practica")

        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + EntryID.get())

        Datos=miCursor.fetchall()
        
        for i in Datos:

            EntryNombre2.set(i[1])
            EntryApellido2.set(i[2])
            EntryPassword2.set(i[3])
            EntryDireccion2.set(i[4])
            textoComentarios.insert(1.0, i[5])
                
        
        miConexion.commit()

        miConexion.close

    # main.EntryNombre.get(), main.EntryApellido.get(), main.EntryPassword.get(), main.EntryDireccion.get(), main.textoComentarios.get(1.0, END))

    BotonRead=Button(miFrameMain, text="Read", width=8, height=1, command=Leer)
    BotonRead.grid(row=10, column=2, padx=10, pady=19)

    def Actualizar():

        miConexion=sqlite3.connect("BBDD Practica")

        miCursor=miConexion.cursor()

        # miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + main.EntryNombre.get() +
        #    "', APELLIDO='" + main.EntryApellido.get() +
        #   "', PASSWORD='" + main.EntryPassword.get() +
        #  "', DIRECCION='" + main.EntryDireccion.get() +
        # "', COMENTARIOS='" + main.textoComentarios.get(1.0, END) +
            #"' WHERE ID=" + main.EntryID.get())

        # Actualziacion parametrizada

        datos=EntryNombre.get(), EntryApellido.get(), EntryPassword.get(), EntryDireccion.get(), textoComentarios.get("1.0", END)

        miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=? WHERE ID=" + EntryID.get() ,(datos))

        messagebox.showinfo("Base de Datos", "Las casillas fueron actualizadas con exito")
                
        miConexion.commit()

        miConexion.close

    BotonUpdate=Button(miFrameMain, text="Update", width=8, height=1, command=Actualizar)
    BotonUpdate.grid(row=10, column=3, padx=10, pady=10)

    
    def Borrar():

        miConexion=sqlite3.connect("BBDD Practica")

        miCursor=miConexion.cursor()

        miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + EntryID.get())

        messagebox.showinfo("Base de Datos", "Se borro con exito")
        
        miConexion.commit()

        miConexion.close

    BotonDelete=Button(miFrameMain, text="Delete", width=8, height=1, command=Borrar)
    BotonDelete.grid(row=10, column=4, padx=10, pady=10)
    
    
    ############################### Menu
    BBDDMenu=Menu(miMenu, tearoff=0)
    BorrarMenu=Menu(miMenu, tearoff=0)
    CRUDMenu=Menu(miMenu, tearoff=0)
    AyudaMenu=Menu(miMenu, tearoff=0)

    miMenu.add_cascade(label="BBDD", menu=BBDDMenu)
    miMenu.add_cascade(label="Borrar", menu=BorrarMenu)
    miMenu.add_cascade(label="CRUD", menu=CRUDMenu)
    miMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

    BBDDMenu.add_command(label="Conectar", command=BBDD.Conectar)

    
    def salirAplicacion():
        valor=messagebox.askquestion("Salir", "Desea salir de la aplicacion")

        if valor=="yes":
            raizMain.destroy()

    BBDDMenu.add_command(label="Salir", command=salirAplicacion)

    BorrarMenu.add_command(label="Borrar Campos", command=borrarCampos)

    CRUDMenu.add_command(label="Crear",command=Crear)
    CRUDMenu.add_command(label="Leer", command=Leer)
    CRUDMenu.add_command(label="Actualizar", command=Actualizar)
    CRUDMenu.add_command(label="Borrar", command=Borrar)

    AyudaMenu.add_command(label="Licencia", command=Licencia.Licencia)
    AyudaMenu.add_command(label="Acerca de...", command=AcercaDe.AcercaDe)

    raizMain.mainloop()



############################################### Boton Entrar del Login: Permite ingresar al Programa Principal ##################################################################
def Entrar():

        
        miConexion=sqlite3.connect("Login BBDD")
        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM LOGIN")

        # miCursor.execute("SELECT * FROM LOGIN WHERE USUARIO=" + variable, "AND CONTRASEÑA=" + variable2)

        datos=miCursor.fetchall()

        for i in datos:
            print(i)

            if i[0]==entryUsuario.get() and i[1]==entryPassword.get():
                Main()
                
        try:
            while i[0]!=entryUsuario.get() or i[1]!=entryPassword.get():
                messagebox.showwarning("ERROR", "Los datos ingresados son incorrectos o no esta registrado.")
                break
        finally:

            miConexion.commit()
            miConexion.close()
         




############################################### LOGIN PRINCIPAL ##################################################################
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
entryPassword=Entry(miFrame,textvariable=entryPassworda, show="*")
entryPassword.grid(row=2, column=2)

miFrame2=Frame()
miFrame2.pack()

botonEntrar=Button(miFrame2, text="Entrar", width=10, height=2, command=Entrar)
botonEntrar.grid(row=1, column=1)

botonRegistrarse=Button(miFrame2, text="Registrarse", width=10, height=2, command=Registrarse)
botonRegistrarse.grid(row=1, column=2)

raiz.mainloop()





