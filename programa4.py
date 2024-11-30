print(" ")#sirve para dejar espacio a la hora de ejecutar
print("Oscar Alonso Reyes Yañez_3w_1208_calculadora")
print(" ")#sirve para dejar espacio a la hora de ejecutar

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero."

try:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))

    calculadora = Calculadora(num1, num2)

    print(f"Suma: {calculadora.suma()}")
    print(f"Resta: {calculadora.resta()}")
    print(f"Multiplicación: {calculadora.multiplicacion()}")
    print(f"División: {calculadora.division()}")

except ValueError:
    print("Por favor, ingresa solo números enteros.")
