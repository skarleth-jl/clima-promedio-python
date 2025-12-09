"""
TAREA: Comparación de Programación Tradicional y POO en Python
SOLUCIÓN: Programación Orientada a Objetos
OBJETIVO: Calcular el promedio semanal utilizando clases y métodos.
"""

class ClimaSemanal:
    """
    Clase que representa las temperaturas de una semana.
    Aplica encapsulamiento al mantener las temperaturas como atributo interno.
    """

    def __init__(self):
        # Lista que almacenará las temperaturas ingresadas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar temperaturas de 7 días.
        """
        print("=== Ingreso de temperaturas (POO) ===")
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula y retorna el promedio semanal.
        """
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa principal
def main():
    """
    Crea un objeto de la clase ClimaSemanal y ejecuta el proceso completo.
    """
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal es: {promedio:.2f}°C")

# Llamada al programa principal
main()