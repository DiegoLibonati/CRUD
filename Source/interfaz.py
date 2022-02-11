from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Salir
import BBDD
import borrarCampos
import Crear
import Leer
import Actualizar
import Borrar
import Licencia
import AcercaDe
import ActivarID



############################# Creacion de RAIZ y MENU

raiz=Tk()
miMenu=Menu(raiz)
raiz.config(menu=miMenu,width=300, height=600)
raiz.title("Operaciones CRUD [BBDD]")

act=IntVar()

############################## Creacion de Frame
miFrame=Frame()
miFrame.pack()

############################### Entry + Label + CheckButton ID:
LabelID=Label(miFrame, text="ID: ", justify="right")
LabelID.grid(row=1, column=1, columnspan=2, sticky="EW")
EntryID=Entry(miFrame)
EntryID.grid(row=1, column=3, columnspan=2, sticky="EW", padx=20, pady=20)
EntryID.config(state="disabled")

miFrame2=Frame()
miFrame2.pack()
LabelBoton=Label(miFrame2, text="Opciones: ", justify="left", anchor="w")
LabelBoton.grid(row=0, column=0)
CheckID=Checkbutton(miFrame2, text="Acticar ID para BUSQUEDAS",  variable=act, onvalue=1, offvalue=0, command=ActivarID.Activar, justify="left", anchor="w")
CheckID.grid(row=1, column=4)

############################### Entry + Label Nombre:
EntryNombre2=StringVar()
LabelNombre=Label(miFrame, text="Nombre: ")
LabelNombre.grid(row=2, column=1, columnspan=2, sticky="EW")
EntryNombre=Entry(miFrame, textvariable=EntryNombre2)
EntryNombre.grid(row=2, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

############################### Entry + Label Apellido:
EntryApellido2=StringVar()
LabelApellido=Label(miFrame, text="Apellido: ")
LabelApellido.grid(row=3, column=1, columnspan=2, sticky="EW")
EntryApellido=Entry(miFrame, textvariable=EntryApellido2)
EntryApellido.grid(row=3, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

############################### Entry + Label Password:
EntryPassword2=StringVar()
LabelPassword=Label(miFrame, text="Password: ")
LabelPassword.grid(row=4, column=1, columnspan=2, sticky="EW")
EntryPassword=Entry(miFrame, show="*", textvariable=EntryPassword2)
EntryPassword.grid(row=4, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

############################### Entry + Label Direccion:
EntryDireccion2=StringVar()
LabelDireccion=Label(miFrame, text="Direccion: ")
LabelDireccion.grid(row=5, column=1, columnspan=2, sticky="EW")
EntryDireccion=Entry(miFrame, textvariable=EntryDireccion2)
EntryDireccion.grid(row=5, column=3, columnspan=2, sticky="EW", padx=20, pady=20)

############################### Cajon de Texto + Label Comentarios:
LabelComentarios=Label(miFrame, text="Comentarios: ")
LabelComentarios.grid(row=6, column=1, columnspan=2, sticky="EW")
textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=6, column=3, columnspan=2, sticky="EW", padx=20, pady=20)
Scroll=Scrollbar(miFrame, command=textoComentarios.yview)
Scroll.grid(row=6, column=5, sticky="nsew")
textoComentarios.config(yscrollcommand=Scroll.set)


############################### Botones
BotonCreate=Button(miFrame, text="Create", width=8, height=1, command=Crear.Crear)
BotonCreate.grid(row=10, column=1, padx=10, pady=10)

BotonRead=Button(miFrame, text="Read", width=8, height=1, command=Leer.Leer)
BotonRead.grid(row=10, column=2, padx=10, pady=19)

BotonUpdate=Button(miFrame, text="Update", width=8, height=1, command=Actualizar.Actualizar)
BotonUpdate.grid(row=10, column=3, padx=10, pady=10)

BotonDelete=Button(miFrame, text="Delete", width=8, height=1, command=Borrar.Borrar)
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
BBDDMenu.add_command(label="Salir", command=Salir.salirAplicacion)

BorrarMenu.add_command(label="Borrar Campos", command=borrarCampos.borrarCampos)

CRUDMenu.add_command(label="Crear",command=Crear.Crear)
CRUDMenu.add_command(label="Leer", command=Leer.Leer)
CRUDMenu.add_command(label="Actualizar", command=Actualizar.Actualizar)
CRUDMenu.add_command(label="Borrar", command=Borrar.Borrar)

AyudaMenu.add_command(label="Licencia", command=Licencia.Licencia)
AyudaMenu.add_command(label="Acerca de...", command=AcercaDe.AcercaDe)



raiz.mainloop()