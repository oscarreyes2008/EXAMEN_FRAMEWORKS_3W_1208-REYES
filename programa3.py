print(" ")#sirve para dejar espacio a la hora de ejecutar
print("Oscar Alonso Reyes Yañez_3w_1208_triangulos")
print(" ")#sirve para dejar espacio a la hora de ejecutar

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

triangulo = Triangulo(lado1, lado2, lado3)

print(f"Lado mayor: {triangulo.lado_mayor()}")
print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")


