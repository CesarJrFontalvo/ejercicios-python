# Ventana 5:Radio

from tkinter import *

def operacion():
    numero = num.get()
    if opcion.get() == 1:
        total = numero * 10
    elif  opcion.get() == 2:
        total = numero * 20
    elif  opcion.get() == 3:
        total = numero * 30
    elif  opcion.get() == 4:
        total = numero * 40
    elif  opcion.get() == 5:
        total = numero * 50
    else:
        total = numero * numero
        print("el total de la operacion es: " + str(total))   
        
ventana = Tk()
opcion = IntVar()
num = IntVar()
ventana.title("Radiobutton en tkinter")
ventana.geometry("400x300")

Label(ventana, text ="Escribe el número: ").place(x=20, y=20)
Entry(ventana, textvariable=num).place(x=130, y=20)
Label(ventana, text ="Escribe el opción: ").place(x=20, y=50)

Radiobutton(ventana,text="X10",value=1, variable=opcion).place(x=20,y=80)
Radiobutton(ventana,text="X20",value=2, variable=opcion).place(x=70,y=80)
Radiobutton(ventana,text="X30",value=3, variable=opcion).place(x=120,y=80)
Radiobutton(ventana,text="X40",value=4, variable=opcion).place(x=20,y=110)
Radiobutton(ventana,text="X50",value=5, variable=opcion).place(x=70,y=110)
Radiobutton(ventana,text="Cuadrado",value=6, variable=opcion).place(x=120,y=110)
Button(ventana,text="Realizar  operación", command=operacion).place(x=20,y=140)

ventana.mainloop() 