print(" ")#sirve para dejar espacio a la hora de ejecutar
print("Oscar Alonso Reyes Yañez_3w_1208_Agendas")
print(" ")#sirve para dejar espacio a la hora de ejecutar

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        email = input("Introduce el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido exitosamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        nombre_buscar = input("Introduce el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_buscar.lower():
                print(contacto)
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el contacto con el nombre '{nombre_buscar}'.")

    def editar_contacto(self):
        nombre_editar = input("Introduce el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_editar.lower():
                print("Contacto encontrado. Introduce los nuevos datos:")
                contacto.nombre = input("Nuevo nombre (deja en blanco para mantener el mismo): ") or contacto.nombre
                contacto.telefono = input("Nuevo teléfono (deja en blanco para mantener el mismo): ") or contacto.telefono
                contacto.email = input("Nuevo email (deja en blanco para mantener el mismo): ") or contacto.email
                print("Contacto editado exitosamente.")
                return
        print(f"No se encontró el contacto con el nombre '{nombre_editar}'.")

    def mostrar_menu(self):
        while True:
            print("\nMenú de la Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            
            opcion = input("Elige una opción (1-5): ")
            
            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Cerrando la agenda...")
                break
            else:
                print("Opción no válida, por favor selecciona una opción entre 1 y 5.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.mostrar_menu()
