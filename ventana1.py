from tkinter import *
import time

def parpadear ():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana = Tk()    
ventana.title("Ventana 1")
boton= Button(ventana,text="boton",command=parpadear)
boton.pack()
ventana.mainloop()