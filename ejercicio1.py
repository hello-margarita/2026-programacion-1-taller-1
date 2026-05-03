# Ejercicio 1: Creación de una clase básica.
# Objetivo: Comprender la estructura básica de una clase y la creación de objetos.

class Coche:
    """Clase que representa la información básica de un automóvil."""
    
    # Definimos los atributos iniciales del vehículo.
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    # Método que imprime la información del vehículo.
    def describir(self):
        print(f"Información del vehículo: Marca {self.marca}, Modelo {self.modelo}, Año {self.anio}")

# --- Creación de objetos (Instanciación) ---

# Se crean varios objetos de la clase Coche con datos fijos.
coche1 = Coche("Volkswagen", "Tiguan", 2014)
coche2 = Coche("Renault", "Duster", 2021)
coche3 = Coche("Renault", "Clio", 2015)

# --- Uso del método describir() ---

# Se muestra por pantalla la información de los objetos creados.
coche1.describir()
coche2.describir()
coche3.describir()