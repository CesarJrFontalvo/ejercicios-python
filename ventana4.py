#Ventanas 4: Entradas

from tkinter import *

#Declarando la función 
def saludar():
    saludo.set("Hola bienvenido " + nombre.get())
    print ("Hola: " + nombre.get() + " " + apellidoP.get() + " " + apellidoM.get())
    print("Tu edad es: "+ edad.get())
    print("Tu sexo es: "+ sexo.get())

#Crear la ventana
ventana = Tk()
ventana.configure(bg='#856ff8')

# Variables
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()
edad = StringVar()
sexo = StringVar()
saludo = StringVar()

# Agregar titulo y tamaño
ventana.title("Entradas en tkinter")
ventana.geometry("400x300")

#se crean las etiquetas, las cajas de texto y su posicion en la ventana
Label(ventana,text="Escribe tu nombre:").place(x=10,y=10)
Entry(ventana,textvariable = nombre).place(x=170,y=10)

Label(ventana,text="Escribe tu apellido paterno:").place(x=10,y=40)
Entry(ventana,textvariable = apellidoP).place(x=170,y=40)

Label(ventana,text="Escribe tu apellido materno:").place(x=10,y=70)
Entry(ventana,textvariable = apellidoM).place(x=170,y=70)

Label(ventana,text="Edad:").place(x=10,y=100)
Entry(ventana,textvariable = edad).place(x=50,y=100)

Label(ventana,text="Sexo:").place(x=10,y=130)
Entry(ventana,textvariable = sexo).place(x=50,y=130)

# Crear el Boton saludar
Button(ventana,text="saludo personalisado", command = saludar).place(x=10,y=160)

# Mostar el saludo en una caja de texto
Entry(ventana,textvariable = saludo).place(x=10,y=190)

ventana.mainloop()