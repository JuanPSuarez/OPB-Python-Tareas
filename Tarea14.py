from tkinter import *

def funcionSelect():
    texto.config(text="{}".format(opcion.get()))
def funcionReset():
    opcion.set(None)
    texto.config(text="")

ventana = Tk()
opcion = StringVar()
opcion.set(None)

rdbtn1 = Radiobutton(ventana, text="Opcion 1", variable=opcion, value='Opcion 1', command=funcionSelect)
rdbtn1.pack()

rdbtn2 = Radiobutton(ventana, text="Opcion 2", variable=opcion, value='Opcion 2', command=funcionSelect)
rdbtn2.pack()

rdbtn3 = Radiobutton(ventana, text="Opcion 3", variable=opcion,   value='Opcion 3', command=funcionSelect)
rdbtn3.pack()

rdbtn4 = Radiobutton(ventana, text="Opcion 4", variable=opcion,   value='Opcion 4', command=funcionSelect)
rdbtn4.pack()

texto = Label(ventana)
texto.pack()
botonReiniciar = Button(ventana, text="Reiniciar", command=funcionReset)
botonReiniciar.pack()

ventana.mainloop()