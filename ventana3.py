#Posicionamiento

from tkinter import *

""" Funcion para que la ventana 
    se centre en la pantalla  """
def centrar_ventana(toplevel):
       toplevel.update_idletasks()
       w = toplevel.winfo_screenwidth()
       h = toplevel.winfo_screenheight()
       size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
       x = w/2 - size[0]/2
       y = h/2 - size[1]/2
       toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

#cerear la ventana
ventana = Tk()

# Llamado de funcion centrar_ventana
centrar_ventana(ventana)

#Tamaño de la ventana
ventana.geometry("400x200")

ventana.title("Posicionamientos")
#posicionamiento con grid
boton1 = Button(ventana, text="Posicionamiento grid").grid(row=0,column=1)
etiqueta1 = Label(ventana, text="Posicionamiento grid").grid(row=0,column=0)

#posicionamiento con place
etiqueta2 = Label(ventana, text="Posicionamiento place").place(x=10,y=40)
boton2 = Button(ventana, text="Posicionamiento place").place(x=150,y=40)
ventana.mainloop()