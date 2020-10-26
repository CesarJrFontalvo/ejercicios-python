#python ventana 2 boton uitar y color de letra
from tkinter import *

def imprime():
    print("Acabas de presionar el botón Imprime")

ventana = Tk()
ventana.title("Segunda ventana")
botonI = Button(ventana, text="imprimir",fg="blue", command=imprime)
botonI.pack()
botonS = Button(ventana, text="Salir", fg="red", command=ventana.quit)
botonS.pack()
ventana.mainloop()