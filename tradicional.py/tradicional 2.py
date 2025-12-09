"""
TAREA: Comparación de Programación Tradicional y POO en Python
SOLUCIÓN: Programación Tradicional
OBJETIVO: Calcular el promedio semanal de temperaturas usando funciones.
"""

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de 7 días
    y retorna una lista con los valores ingresados.
    """
    temperaturas = []
    print("=== Ingreso de temperaturas (Programación Tradicional) ===")
    
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    """
    Ejecuta la lógica general del programa usando programación tradicional.
    """
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal es: {promedio:.2f}°C")

# Llamada al programa principal
main()