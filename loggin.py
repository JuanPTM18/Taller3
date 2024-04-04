import tkinter as tk 
from tkinter import*
from tkinter import messagebox
from Registro import*
from Menu import*
from icons import*
from Tooltip import*


class loggin(Menu,Registro):
    def mostrarAyuda(self,event):
        messagebox.showinfo("ayuda","debe agregar tu nombre de usuario y una contraseña de minimo 8 caracteres\nluego presione el boton ingresar")
    #menu = Menu()
    def verCaracteres(self,event):
        self.txtPasword.configure(show='')
        self.btnVer.configure(text="ocultar")

    def ocultarCaracteres(self,event):
        self.txtPasword.configure(show="*")
        self.btnVer.configure(text="ver")
    def validarLongitud(self,event):
        longitud=len(self.txtPasword.get())#el get trae el texto que tiene la caja 
        if longitud >=8:
            self.btnIngresar.configure(state="normal")#para poder oprimir
        else:
            self.btnIngresar.configure(state="disabled")

    

    def __init__(self):
        
        self.ventana=tk.Tk()
        self.ventana.geometry("300x150")
        self.ventana.resizable(0,0)

        self.lblTitulo=tk.Label(self.ventana,text="inicio sesion ")
        self.lblTitulo.grid(row=0,column=0,columnspan=3)

        self.lblUsuario=tk.Label(self.ventana,text="Usuario")
        self.lblUsuario.grid(row=1,column=0,)
        self.txtUsuario=tk.Entry(self.ventana,width=25)
        self.txtUsuario.grid(row=1,column=1)

        self.lblPasword=tk.Label(self.ventana,text="contraseña")
        self.lblPasword.grid(row=2,column=0)
        self.txtPasword=tk.Entry(self.ventana,width=25,show="*")#show para que el usuario vea los asteriscos
        self.txtPasword.grid(row=2,column=1)
        self.txtPasword.bind("<KeyRelease>",self.validarLongitud)#escucha

        self.btnVer=tk.Button(self.ventana,text="ver")
        self.btnVer.grid(row=2,column=2)

        self.btnVer.bind("<Enter>",self.verCaracteres)#escucha ver caracteres
        self.btnVer.bind("<Leave>",self.ocultarCaracteres)

        self.btnIngresar=tk.Button(self.ventana,text="ingresar",command=self.crearVentanaM,width=20,state="disabled")#pa que el usuario no pueda dar clic 
        self.btnIngresar.grid(row=3,column=1)

        self.btnRegistro=tk.Button(self.ventana,text="Registrase",command=self.Registrarse)
        self.btnRegistro.grid(row=4,column=1)

        self.btnLimpiar=tk.Button(self.ventana,text="limpiar") 
        self.btnLimpiar.grid(row=3,column=2)

        iconoAyuda=tk.PhotoImage(file=r"icons\help.png")
        self.btnAyuda=tk.Button(self.ventana,image=iconoAyuda)
        self.btnAyuda.place(relx=1,x=-40,rely=0.1,width=25,height=25)

        Tooltip(self.btnAyuda,"presione para obtener ayuda!\nALT+a")
        self.btnAyuda.bind('<Button-1>',self.mostrarAyuda)

        self.ventana.bind('<Alt-a>',self.mostrarAyuda)




 

        self.ventana.mainloop()











        

