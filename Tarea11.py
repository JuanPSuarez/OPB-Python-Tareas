import pickle

class Vehiculo:
    def __init__(self,marca ,color, hp):
        self.marca = marca
        self.color = color
        self.hp = hp
    def __str__(self):
        return self.marca +" "+ self.color + " " + self.hp


Mengano = Vehiculo("Mustang", "Amarillo", "600hp")

print(Mengano)
file = open('tarea11_Vehiculo_objeto', 'w+b')


pickle.dump(Mengano, file)


file.seek(0)
nuevo_Mengano = pickle.load(file)

print(nuevo_Mengano)


file.close()