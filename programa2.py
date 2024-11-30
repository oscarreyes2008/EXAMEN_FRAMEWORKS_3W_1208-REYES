print(" ")#sirve para dejar espacio a la hora de ejecutar
print("Oscar Alonso Reyes Yañez_3w_1208_programa sobre si eres mayor de edad o no dependiendo tu edad")
print(" ")#sirve para dejar espacio a la hora de ejecutar
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

if __name__ == "__main__":
    nombre = input("Introduce el nombre de la persona: ")
    while True:
        try:
            edad = int(input("Introduce la edad de la persona: "))
            if edad >= 0:
                break
            else:
                print("La edad debe ser un número positivo. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un valor numérico para la edad.")
    
    persona = Persona(nombre, edad)

    persona.mostrar_datos()
    persona.es_mayor_de_edad()
print(" ")#sirve para dejar espacio a la hora de ejecutar