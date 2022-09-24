class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrarAlumno(self):
        print(f"El alumno {self.nombre}, tiene de nota {self.nota}")
    
    def estaAprobado(self):
        if self.nota >= 6:
            print(f"El alumno {self.nombre}, esta aprobado.")
        else:
            print(f"El alumno {self.nombre}, esta desaprobado.")

a1 = Alumno("Juan", 9)
a1.mostrarAlumno()
a1.estaAprobado()
a2 = Alumno("Fulano", 10)
a2.mostrarAlumno()
a2.estaAprobado()
a3 = Alumno("Mengano", 4)
a3.mostrarAlumno()
a3.estaAprobado()

