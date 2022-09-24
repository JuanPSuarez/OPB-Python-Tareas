txtArchivo = open("tarea10.txt", "w+")
txtArchivo.write("Este es una linea de texto en mi archivo\n")
txtArchivo.close()

txtArchivo = open("tarea10.txt", "r+")
txtArchivo.readline()
txtArchivo.write("Esta es la segunda linea.\n")

txtArchivo.seek(0)
print(txtArchivo.read())
txtArchivo.close()