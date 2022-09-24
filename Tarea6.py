class Vehiculo:
    def __init__(self, Color, Ruedas, Puertas):
        self.color = Color
        self.ruedas = Ruedas
        self.puertas = Puertas

class Coche(Vehiculo):
    def __init__(self, Color, Ruedas, Puertas, Velocidad,
Cilindrada):
        super().__init__(Color, Ruedas, Puertas)
        self.velocidad = Velocidad
        self.cilindrada = Cilindrada


newCoche = Coche("Rojo", 4, 5, 120, 200)

print (
f"El color del auto es: {newCoche.color}", "\n", 
f"La cantidad de ruedas: {newCoche.ruedas}", "\n",
f"La cantidad de puertas: {newCoche.puertas}", "\n",
f"La de velocidad es de: {newCoche.velocidad}", "\n",
f"Y su cilindrada es de: {newCoche.cilindrada}"
)