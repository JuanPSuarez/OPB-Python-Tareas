from tkinter import *
ventana = Tk()
ventana.config(bg="lightgrey")
var = StringVar()
listaTexto = Listbox(ventana)
listaTexto.config(bg="lightgrey")
for item in ["Bitcoin", "Ethereum", "Monero", "Dogecoin"]:
    listaTexto.insert(END, item)
listaTexto.pack()

textoBottom = Label(text="Lista de nombres de criptomonedas")
textoBottom.pack()

ventana.mainloop()