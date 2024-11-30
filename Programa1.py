print(" ")#sirve para dejar espacio a la hora de ejecutar
print("Oscar Alonso Reyes Yañez_3w_1208_programa sobre si aprobaste o no dependiendo la  nota")
print(" ")#sirve para dejar espacio a la hora de ejecutar
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha suspendido.")

if __name__ == "__main__":
    nombre = input("Introduce el nombre del alumno: ")
    while True:
        try:
            nota = float(input("Introduce la nota del alumno (0-10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un valor numérico para la nota.")

    alumno = Alumno(nombre, nota)

    alumno.imprimir()
    alumno.resultado()
