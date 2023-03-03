#App para convertir pies a metros usando Tkinter
#Alcantara Gomez Axel Octavio
#23 de febrero 2023

from tkinter import *
from tkinter import ttk


if __name__=="__main__":
    print("Solo se mostrara si es el principal")

class Conversor: 

    def __init__(self, raiz):

        raiz.title("Pies a metros")

        self.pies=StringVar()
        self.metros=StringVar()


        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0,row=0)

        piesEntry = ttk.Entry(mainFrame,textvariable=self.pies)
        piesEntry.grid(column=1,row=0)

        ttk.Label(mainFrame, text="Pies").grid(column = 2, row=0)
        ttk.Label(mainFrame, text="Ingresa tus pies:").grid(column = 0, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a:").grid(column = 0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column = 1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column = 2, row=1)
        ttk.Button(mainFrame, text="Calcular",command=self.Calcular ).grid(column = 2, row=2)

        raiz.bind("<Return>",self.Calcular)

    def Calcular(self, *args):
        pies=float(self.pies.get())
        print("Se preciono el boton")
        Metros=pies*0.3048
        self.metros.set(Metros)