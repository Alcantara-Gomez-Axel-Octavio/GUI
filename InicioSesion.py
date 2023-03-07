#   Iniciar sesion
#Alcantara Gomez Axel Octavio
#7 de marzo 2023

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


if __name__=="__main__":
    print("Solo se mostrara si es el principal")

class InicioSesion: 

    def __init__(self, raiz):

        raiz.title("Inicio de sesion")

        self.usuario=StringVar()
        self.contrasena=StringVar()


        mainFrame = ttk.Frame(raiz, padding="10 30 10 30")
        mainFrame.grid(column=0,row=0)

        usuarioEntry = ttk.Entry(mainFrame, width=20,textvariable=self.usuario)
        usuarioEntry.grid(column=1,row=0, sticky=(W,E))

        usuarioEntry = ttk.Entry(mainFrame, width=20,textvariable=self.usuario)
        contrasenaEntry = ttk.Entry(mainFrame, width=20,textvariable=self.contrasena)
        usuarioEntry.grid(column=1,row=0, sticky=(W,E)) 
        contrasenaEntry.grid(column=1,row=3, sticky=(W,E)) 


        ttk.Label(mainFrame, text="Usuario:").grid(column = 0, row=0)
        ttk.Label(mainFrame, text="").grid(column = 1, row=1)
        ttk.Label(mainFrame, text="Contrasena:").grid(column = 0, row=3)


    
        ttk.Button(mainFrame, text="Calcular",command=self.Leer ).grid(column = 1, row=5, sticky=(E))

        usuarioEntry.focus()
        raiz.bind("<Return>",self.Leer)

    def Leer(self, *args):
        print("")
        #try:
          

        #except:       
            #messagebox.showinfo("Error", "Este dato no es valido.")
            #self.pies.set("")