import time as t

hora = t.localtime()
horaActual = t.strftime("%H:%M:%S", hora)
sep = ":"
stringhoraActual=horaActual.split(sep, 1)[0]
stringhoraActual = int(stringhoraActual)


def cuantoFalta(stringhoraActual):
    if int(stringhoraActual) < 19:
        print(f"Faltan {19-int(stringhoraActual)} horas para finalizar el horario laboral")
    else:
        print("Hora de irse!")
cuantoFalta(stringhoraActual)
