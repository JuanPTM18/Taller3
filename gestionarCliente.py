from tkinter import*
import tkinter as tk
from Tooltip import*
from tkinter import messagebox
from icons import *

class Gestionar():


    def crearCliente(self):
        self.ventana=tk.Toplevel()
        self.ventana.geometry("300x300")

        self.lblTitulo=tk.Label(self.ventana,text="Crear Cliente")
        self.lblTitulo.place(relx=0.5,rely=0.1,anchor="center")
        self.lblusuario1=tk.Label(self.ventana,text="Usuario* ")
        self.lblusuario1.place(x=50, y=50)
        
        self.txtusuario1=Entry(self.ventana)
        self.txtusuario1.place(x=150, y=50)
        Tooltip(self.txtusuario1, "digita nombre de usuario completo, mínimo 8 caracteres.")

        self.lblNombre=tk.Label(self.ventana,text="Nombre*")
        self.lblNombre.place(x=50, y=80)

        self.txtNombre=Entry(self.ventana)
        self.txtNombre.place(x=150, y=80)
        Tooltip(self.txtNombre, "Ingrese su nombre completo, mínimo 8 caracteres.\nSolo letras [a-z]")
        

        self.lblApellido=tk.Label(self.ventana,text="apellido*")
        self.lblApellido.place(x=50, y=110)

        self.txtapellido=Entry(self.ventana)
        self.txtapellido.place(x=150, y=110)
        Tooltip(self.txtapellido, "Ingrese su apellido completo, mínimo 8 caracteres.\nSolo letras [a-z]")


        self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
        self.lbltelefono.place(x=50, y=140)

        self.txtTelefono=Entry(self.ventana)
        self.txtTelefono.place(x=150, y=140)
        Tooltip(self.txtTelefono, "Ingrese su telefono en este campo ")


        self.lblEmail=tk.Label(self.ventana,text="Email*")
        self.lblEmail.place(x=50, y=170)

        self.txtEmail=Entry(self.ventana)
        self.txtEmail.place(x=150, y=170)
        Tooltip(self.txtEmail, "Ingrese su correo en este campo")


        iconoGuardar=tk.PhotoImage(file=r"icons\user_add.png")
        self.btnguardar=Button(self.ventana,text="guardar", image=iconoGuardar, compound=LEFT)
        self.btnguardar.place(x=50, y=220)
        Tooltip(self.btnguardar, "presiona para guardar al cliente")

        iconoLimpiar=tk.PhotoImage(file=r"icons\textfield_delete.png")
        self.btnLimpiar=tk.Button(self.ventana, text="Limpiar", image=iconoLimpiar, compound=LEFT)
        self.btnLimpiar.place(x=120, y=220)
        Tooltip(self.btnLimpiar, "presiona para borrar todos los campos ")

        iconoSalir=tk.PhotoImage(file=r"icons\cancel.png")
        self.btnsalir=tk.Button(self.ventana,text="salir", image=iconoSalir, compound=LEFT)
        self.btnsalir.place(x=250, y=220)
        Tooltip(self.btnsalir, "pulsa para salir ")

    def eliminarCliente(self):
        self.ventana=tk.Toplevel()
        self.ventana.geometry("300x300")
        self.lbltitulo=tk.Label(self.ventana,text="Eliminar  Cliente")
        self.lbltitulo.place(relx=0.5,rely=0.1,anchor="center")

        self.lblcedula=tk.Label(self.ventana,text="Cedula*")
        self.lblcedula.place(relx=0.1,rely=0.2)
        self.txtcedula=Entry(self.ventana)
        self.txtcedula.place(relx=0.3,rely=0.2,width=150)
        Tooltip(self.txtcedula, "Ingrese la cedula de quien se quiere eliminar.")

        self.lblnombre=tk.Label(self.ventana,text="Nombres*")
        self.lblnombre.place(relx=0.1,rely=0.3)
        self.txtnombre=Entry(self.ventana,state="disabled")
        self.txtnombre.place(relx=0.3,rely=0.3,width=150)

        self.lblapellido=tk.Label(self.ventana,text="Apellidos")
        self.lblapellido.place(relx=0.1,rely=0.4)
        self.txtapellido=Entry(self.ventana,state="disabled")
        self.txtapellido.place(relx=0.3,rely=0.4,width=150)

        self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
        self.lbltelefono.place(relx=0.1,rely=0.5)
        self.txttelefono=Entry(self.ventana,state="disabled")
        self.txttelefono.place(relx=0.3,rely=0.5,width=150)

        self.lblemail=tk.Label(self.ventana,text="Email*")
        self.lblemail.place(relx=0.1,rely=0.6)
        self.txtemail=Entry(self.ventana,state="disabled")
        self.txtemail.place(relx=0.3,rely=0.6,width=150)


        iconoBuscar=tk.PhotoImage(file=r"icons\application_form_magnify.png")
        self.btnBuscar=tk.Button(self.ventana,text="Buscar", image=iconoBuscar, compound=LEFT)
        self.btnBuscar.place(relx=0.8,rely=0.2)
        Tooltip(self.btnBuscar, "presiona para buscar")

        iconoLimpiar=tk.PhotoImage(file=r"icons\textfield_delete.png")
        self.btnLimpiar=tk.Button(self.ventana, text="Limpiar", image=iconoLimpiar, compound=LEFT) 
        self.btnLimpiar.place(relx=0.4, rely=0.8)
        Tooltip(self.btnLimpiar, "presiona para borrar todos los campos ")

        iconoSalir=tk.PhotoImage(file=r"icons\cancel.png")
        self.btnsalir=tk.Button(self.ventana,text="salir", image=iconoSalir, compound=LEFT)
        self.btnsalir.place(relx=0.7, rely=0.8)
        Tooltip(self.btnsalir, "pulsa para salir ")

        iconoEliminar=PhotoImage(file=r"icons\user_delete.png")
        self.btnEliminar=tk.Button(self.ventana,text="Eliminar", image=iconoEliminar, compound=LEFT)
        self.btnEliminar.place(relx=0.1,rely=0.8)
        Tooltip(self.btnEliminar, "presiona para eliminar el cliente seleccionado")


    def ModificarCliente(self):
        self.ventana=tk.Toplevel()
        self.ventana.geometry("300x300")
        self.lbltitulo=tk.Label(self.ventana,text="Modificar Cliente")
        self.lbltitulo.place(relx=0.5,rely=0.1,anchor="center")

        self.lblcedula=tk.Label(self.ventana,text="Cedula*")
        self.lblcedula.place(relx=0.1,rely=0.2)
        self.txtcedula=Entry(self.ventana)
        self.txtcedula.place(relx=0.3,rely=0.2,width=150)
        Tooltip(self.txtcedula, "Ingrese la cedula del cliente a modificar.")


        self.lblnombre=tk.Label(self.ventana,text="Nombres*")
        self.lblnombre.place(relx=0.1,rely=0.3)
        self.txtnombre=Entry(self.ventana,state="disabled")
        self.txtnombre.place(relx=0.3,rely=0.3,width=150)
        

        self.lblapellido=tk.Label(self.ventana,text="Apellidos")
        self.lblapellido.place(relx=0.1,rely=0.4)
        self.txtapellido=Entry(self.ventana,state="disabled")
        self.txtapellido.place(relx=0.3,rely=0.4,width=150)

        self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
        self.lbltelefono.place(relx=0.1,rely=0.5)
        self.txttelefono=Entry(self.ventana,state="disabled")
        self.txttelefono.place(relx=0.3,rely=0.5,width=150)

        self.lblemail=tk.Label(self.ventana,text="Email*")
        self.lblemail.place(relx=0.1,rely=0.6)
        self.txtemail=Entry(self.ventana,state="disabled")
        self.txtemail.place(relx=0.3,rely=0.6,width=150)

        self.btnBuscar=tk.Button(self.ventana,text="Buscar")
        self.btnBuscar.place(relx=0.8,rely=0.2)
        Tooltip(self.btnBuscar, "pulsa para buscar el cliente que se desea modificar ")

        self.btnLimpiar=tk.Button(self.ventana,text="Limpiar")
        self.btnLimpiar.place(relx=0.3,rely=0.8)
        Tooltip(self.btnLimpiar, "presiona para borrar todos los campos ")

        self.btnSalir=tk.Button(self.ventana,text="Salir")
        self.btnSalir.place(relx=0.7,rely=0.8)
        Tooltip(self.btnSalir, "pulsa para salir")

        self.btnModificar=tk.Button(self.ventana,text="Modificar")
        self.btnModificar.place(relx=0.1,rely=0.8)
        Tooltip(self.btnModificar, "presione para modificar el cliente")

        self.ventana.mainloop()