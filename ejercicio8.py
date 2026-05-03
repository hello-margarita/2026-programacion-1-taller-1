# Ejercicio 8: Interfaces
# Objetivo: Implementar el uso de interfaces para definir comportamiento común.

from abc import ABC, abstractmethod

# 1. Definimos la "Interfaz" Volador
class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

# 2. Clase Pájaro: Un volador biológico (animal)
class Pajaro(Volador):
    def __init__(self, especie):
        self.especie = especie

    def volar(self):
        print(f"El {self.especie} agita sus alas velozmente y despega del nido. ¡Cuidado con las estatuas!")

# 3. Clase Avión: Un volador mecánico (objeto)
class Avion(Volador):
    def __init__(self, modelo):
        self.modelo = modelo

    def volar(self):
        print(f"El {self.modelo} enciende sus turbinas, alcanza velocidad de crucero y sirve café caro a los pasajeros.")

# --- Implementación del comportamiento común ---

# Creamos la lista de "Cosas que vuelan"
objetos_voladores = [
    Pajaro("Colibrí"),
    Avion("Boeing 747"),
    Pajaro("Águila"),
    Avion("Airbus A320")
]

print("--- Torre de control, estamos listos para despegar! ---")
for objeto in objetos_voladores:
    objeto.volar()