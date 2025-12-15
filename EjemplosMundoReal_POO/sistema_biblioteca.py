"""
Caso del Mundo Real:
Sistema de Reservas de una Biblioteca
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def reservar_libro(self, libro):
        print(f"{self.nombre} intenta reservar '{libro.titulo}'")
        libro.prestar()

    def devolver_libro(self, libro):
        print(f"{self.nombre} devuelve '{libro.titulo}'")
        libro.devolver()


libro1 = Libro("Introducción a Python", "Guido van Rossum")
usuario1 = Usuario("Ana")

usuario1.reservar_libro(libro1)
usuario1.devolver_libro(libro1)

