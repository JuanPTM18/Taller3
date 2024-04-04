from tkinter import*
import tkinter as tk
from Tooltip import*
from gestionarCliente import*
from icons import*
from Registro import*


class Menu(Gestionar):

   
    def crearVentanaM(self):
        
        self.ventana=tk.Toplevel()
        self.ventana.geometry("550x300")
        self.menu = tk.Menu(self.ventana)
        self.ventana.resizable(0,0)
        self.lblbienvenido=tk.Label(self.ventana,text="BIENVENIDO",width=150)
        self.lblbienvenido.place(relx=0.5,rely=0.3,anchor="center")
        
        self.gestionarCliente = tk.Menu(self.menu,tearoff=0)

        self.gestionarCliente.add_command(label="crear cliente ",command=self.crearCliente)
        self.gestionarCliente.add_command(label="eliminar cliente",command=self.eliminarCliente)
        self.gestionarCliente.add_command(label="modificar cliente",command=self.ModificarCliente)

        self.gestionarCuenta = tk.Menu(self.menu,tearoff=0)

        self.gestionarTrans = tk.Menu(self.menu,tearoff=0)

        self.consultarInfo=tk.Menu(self.menu,tearoff=0)

        self.salir=tk.Menu(self.menu,tearoff=0)

        self.menu.add_cascade(label="gestionar Clientes", menu=self.gestionarCliente)
        self.menu.add_cascade(label="gestionar Cuentas", menu=self.gestionarCuenta)
        self.menu.add_cascade(label="gestionar Transacciones", menu=self.gestionarTrans)
        self.menu.add_cascade(label="consultar informacion",menu=self.consultarInfo)
        self.menu.add_cascade(label="Salir",menu=self.salir)


        self.ventana.config(menu=self.menu)

        self.ventana.mainloop()






   