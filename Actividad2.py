#Actividad de interfaz 2
#Alcantara Gomez Axel Octavio
# 9 Marzo del 2023
from tkinter import *
from tkinter import ttk

# Crear ventana principal
root = Tk()

# Crear frame principal
main_frame = ttk.Frame(root, width=200, height=200)
main_frame.pack()

# Crear frame secundario
sub_frame = ttk.Frame(main_frame, width=300, height=300,padding="30 30 30 30",relief="raised")
sub_frame.pack()
sub_frame.grid(column=0,row=0,pady=25)

ttk.Label(sub_frame, text="Nombre:").grid(column = 0, row=0, pady= 12)
nombre = ttk.Entry(sub_frame, width=20)
nombre.grid(column=1,row=0)

ttk.Label(sub_frame, text="A. Paterno:").grid(column = 0, row=1, pady= 12)
aPaterno = ttk.Entry(sub_frame, width=20)
aPaterno.grid(column=1,row=1)

ttk.Label(sub_frame, text="A. Materno:").grid(column = 0, row=2, pady= 12)
aMaterno = ttk.Entry(sub_frame, width=20)
aMaterno.grid(column=1,row=2)

ttk.Label(sub_frame, text="Correo").grid(column = 0, row=3, pady= 12)
correo = ttk.Entry(sub_frame, width=20)
correo.grid(column=1,row=3)

ttk.Label(sub_frame, text="Movil").grid(column = 0, row=4, pady= 12)
movil = ttk.Entry(sub_frame, width=20)
movil.grid(column=1,row=4)

#

sub_frame2 = ttk.Frame(main_frame, width=300, height=300,padding="10 30 10 30")
sub_frame2.grid(column=1,row=0)

ttk.Radiobutton(sub_frame2,text="Estudiante").grid(column = 0, row=0)
ttk.Radiobutton(sub_frame2,text="Empleado").grid(column = 0, row=1)
ttk.Radiobutton(sub_frame2,text="Empleado").grid(column = 0, row=2)



sub_frame3 = ttk.Frame(main_frame, width=300, height=300,padding="30 10 30 10",relief="raised")
sub_frame3.grid(column=0,row=1)

ttk.Label(sub_frame3, text="Aficiones:").grid(column = 0, row=0, pady= 12)
ttk.Checkbutton(sub_frame3,text="Leer").grid(column = 0, row=1)
ttk.Checkbutton(sub_frame3,text="Musica").grid(column = 1, row=1)
ttk.Checkbutton(sub_frame3,text="Videojuegos").grid(column = 2, row=1)

#

sub_frame4 = ttk.Frame(main_frame, width=200, height=300,padding="10 10 10 10")
sub_frame4.grid(column=1,row=1)

estado = StringVar()
comboEstados = ttk. Combobox(sub_frame4, textvariable=estado)
comboEstados.grid()
comboEstados[ 'values'] = ("Jalisco", "Nayarit", "Colima", "Michoacán")

sub_frame5 = ttk.Frame(main_frame, width=200, height=300,padding="10 10 10 10")
sub_frame5.grid(column=0,row=2)

ttk.Button(sub_frame5, text="Guardar").grid(column = 0, row=0, padx= 12)
ttk.Button(sub_frame5, text="Cancelar").grid(column = 1, row=0,padx= 12)
# Mostrar ventana
root.mainloop()

        