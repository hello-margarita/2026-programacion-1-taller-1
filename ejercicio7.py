# Ejercicio 7: Clases Abstractas
# Objetivo: Entender la abstracción y las clases abstractas.

from abc import ABC, abstractmethod

# 1. Clase Abstracta: Define la "regla", pero no hace nada por sí sola.
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacerSonido(self):
        # Usamos 'pass' porque no sabemos qué sonido hace un "Animal" genérico.
        pass

# 2. Clases Concretas: Aquí es donde SÍ ponemos los print.
class Perro(Animal):
    def hacerSonido(self):
        print(f"El perro {self.nombre} hace el sonido: ¡Guau guau!")

class Gato(Animal):
    def hacerSonido(self):
        print(f"El gato {self.nombre} hace el sonido: ¡Miau!")

class Leon(Animal):
    def hacerSonido(self):
        print(f"El león {self.nombre} hace el sonido: ¡Roooar!")

class Pato(Animal):
    def hacerSonido(self):
        print(f"El pato {self.nombre} hace el sonido: ¡Cuac cuac!")

# --- Implementación de la lista ---

# 3. Creamos la lista de objetos con sus nombres
lista_animales = [
    Perro("Travis"), 
    Gato("Mourinho"), 
    Leon("Lorenzo"), 
    Pato("Lukas")
]

# 4. El ciclo recorre la lista y ejecuta el print que está dentro de cada clase.
print("--- Iniciando el concierto de sonidos de animales ---")
for animal in lista_animales:
    animal.hacerSonido()