# Ejercicio 6: Polimorfismo
# Objetivo: Aplicar polimorfismo en el uso de clases y métodos mediante listas.

class Vehiculo:
    def __init__(self, velocidad_inicial=0):
        self.velocidad = velocidad_inicial

    def acelerar(self):
        self.velocidad += 10
        print(f"El vehículo genérico acelera. Velocidad: {self.velocidad} km/h")

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__()
        self.marca = marca
        self.modelo = modelo

    # Sobreescritura para el coche
    def acelerar(self):
        self.velocidad += 20
        print(f"El vehículo {self.marca} {self.modelo} sube a: {self.velocidad} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo

    # Sobreescritura para la bicicleta
    def acelerar(self):
        self.velocidad += 5
        print(f"La bicicleta tipo {self.tipo} pedalea a: {self.velocidad} km/h")

# --- Pruebas de Polimorfismo con Listas ---

# Creamos una lista que contiene diferentes tipos de objetos (Coche y Bicicleta)
mis_vehiculos = [
    Coche("Volkswagen", "Tiguan"),
    Bicicleta("Montaña"),
    Coche("Mazda", "2"),
    Bicicleta("Urbana")
]

# Recorremos la lista e invocamos el método acelerar() en cada uno
print("--- Iniciando recorrido de la lista de vehículos ---")
for v in mis_vehiculos:
    v.acelerar()