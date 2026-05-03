# Ejercicio 5: Sobreescritura de Métodos
# Objetivo: Implementar la sobreescritura de métodos en clases derivadas.

class Vehiculo:
    def __init__(self, velocidad_inicial=0):
        self.velocidad = velocidad_inicial

    def acelerar(self):
        self.velocidad += 10
        print(f"El vehículo ha acelerado. Velocidad actual: {self.velocidad} km/h")

# Clase Coche (Hereda de Vehiculo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_inicial=0):
        super().__init__(velocidad_inicial)
        self.marca = marca
        self.modelo = modelo

    # Sobreescritura: Personalizamos cómo acelera el coche
    def acelerar(self):
        self.velocidad += 20
        print(f"El vehículo {self.marca} {self.modelo} aumenta su velocidad a: {self.velocidad} km/h")

# Clase Bicicleta (Hereda de Vehiculo)
class Bicicleta(Vehiculo):
    def __init__(self, tipo, velocidad_inicial=0):
        super().__init__(velocidad_inicial)
        self.tipo = tipo

    # Sobreescritura: Personalizamos cómo acelera la bicicleta
    def acelerar(self):
        self.velocidad += 5
        print(f"Pedaleas rápido en la bicicleta de {self.tipo}. Nueva velocidad: {self.velocidad} km/h")

# --- Pruebas de Sobreescritura (Polimorfismo) ---

mi_carro = Coche("Volkswagen", "Tiguan")
mi_bici = Bicicleta("Montaña")

# Mostramos cómo se comporta cada clase con su propia versión de acelerar()
mi_carro.acelerar()
mi_bici.acelerar()