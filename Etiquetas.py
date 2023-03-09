#Etiquetas
#Alcantara Gomez Axel Octavio
#7 de marzo 2023

from tkinter import *
from tkinter import ttk


raiz = Tk()
etqTexto = ttk.Label(raiz, text="Etiquetas")
etqTexto.grid()

imagen = PhotoImage(file= 'Conchita.png')

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen["image"]  = imagen

etqCombinada = ttk.Label(raiz, text="Me gusta el pan", compound="center")
etqCombinada.grid()
etqCombinada[ "image" ] = imagen

raiz.mainloop()