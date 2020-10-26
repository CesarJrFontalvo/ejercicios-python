#Ventanas 4: Entradas

from tkinter import *

def saludar():
    print ("Hola: " + nombre.get() + " " + apellidoP.get() + " " + apellidoM.get())

ventana = Tk()
ventana.configure(bg='#856ff8')
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()

ventana.title("Entradas en tkinter")
ventana.geometry("400x200")

Label(ventana,text="Escribe tu nombre:").place(x=10,y=10)
Entry(ventana,textvariable = nombre).place(x=170,y=10)

Label(ventana,text="Escribe tu apellido paterno:").place(x=10,y=40)
Entry(ventana,textvariable = apellidoP).place(x=170,y=40)

Label(ventana,text="Escribe tu apellido materno:").place(x=10,y=70)
Entry(ventana,textvariable = apellidoM).place(x=170,y=70)

Button(ventana,text="saludo personalisado", command = saludar).place(x=10,y=100)

ventana.mainloop()