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
        Tooltip(self.txtusuario1, "Ingrese su usuario en este campo")

        self.lblNombre=tk.Label(self.ventana,text="Nombre*")
        self.lblNombre.place(x=50, y=80)

        self.txtNombre=Entry(self.ventana)
        self.txtNombre.place(x=150, y=80)
        Tooltip(self.txtNombre, "Ingrese su nombre completo, solo letras desde la [A-Z]")


        self.lblApellido=tk.Label(self.ventana,text="apellido*")
        self.lblApellido.place(x=50, y=110)

        self.txtapellido=Entry(self.ventana)
        self.txtapellido.place(x=150, y=110)
        Tooltip(self.txtapellido, "Ingrese su apellido completo, solo letras desde la [A-Z]")



        self.lbltelefono=tk.Label(self.ventana,text="Telefono*")
        self.lbltelefono.place(x=50, y=140)

        self.txtTelefono=Entry(self.ventana)
        self.txtTelefono.place(x=150, y=140)
        Tooltip(self.txtTelefono, "digita en este campo su numero telefonico, solo numeros ")



        self.lblEmail=tk.Label(self.ventana,text="Email*")
        self.lblEmail.place(x=50, y=170)

        self.txtEmail=Entry(self.ventana)
        self.txtEmail.place(x=150, y=170)
        Tooltip(self.txtEmail, "Ingrese su correo electronico en este campo")


        self.btnguardar=Button(self.ventana,text="guardar")
        self.btnguardar.place(x=50, y=220)
        Tooltip(self.btnguardar, "pulsa este boton para guardar")


        self.btnlimpiar=Button(self.ventana,text="limpiar")
        self.btnlimpiar.place(x=120, y=220)
        Tooltip(self.btnlimpiar, "boton para limpiar todos los campos")

        self.btnsalir=Button(self.ventana,text="salir")
        self.btnsalir.place(x=250, y=220)
        Tooltip(self.btnsalir, "pulsa para salir")

    def eliminarCliente(self):
        self.ventana=tk.Toplevel()
        self.ventana.geometry("300x300")
        self.lbltitulo=tk.Label(self.ventana,text="Eliminar  Cliente")
        self.lbltitulo.place(relx=0.5,rely=0.1,anchor="center")

        self.lblcedula=tk.Label(self.ventana,text="Cedula*")
        self.lblcedula.place(relx=0.1,rely=0.2)
        self.txtcedula=Entry(self.ventana)
        self.txtcedula.place(relx=0.3,rely=0.2,width=150)

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

        self.btnLimpiar=tk.Button(self.ventana,text="Limpiar")
        self.btnLimpiar.place(relx=0.3,rely=0.8)

        self.btnSalir=tk.Button(self.ventana,text="Salir")
        self.btnSalir.place(relx=0.7,rely=0.8)

        self.btnEliminar=tk.Button(self.ventana,text="Eliminar")
        self.btnEliminar.place(relx=0.1,rely=0.8)

    def ModificarCliente(self):
        self.ventana=tk.Toplevel()
        self.ventana.geometry("300x300")
        self.lbltitulo=tk.Label(self.ventana,text="Modificar Cliente")
        self.lbltitulo.place(relx=0.5,rely=0.1,anchor="center")

        self.lblcedula=tk.Label(self.ventana,text="Cedula*")
        self.lblcedula.place(relx=0.1,rely=0.2)
        self.txtcedula=Entry(self.ventana)
        self.txtcedula.place(relx=0.3,rely=0.2,width=150)

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

        self.btnLimpiar=tk.Button(self.ventana,text="Limpiar")
        self.btnLimpiar.place(relx=0.3,rely=0.8)

        self.btnSalir=tk.Button(self.ventana,text="Salir")
        self.btnSalir.place(relx=0.7,rely=0.8)

        self.btnEliminar=tk.Button(self.ventana,text="Modificar")
        self.btnEliminar.place(relx=0.1,rely=0.8)

        self.ventana.mainloop()