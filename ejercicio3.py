# Ejercicio 3: Constructores
# Objetivo: Utilizar constructores para inicializar objetos.

class Coche:
    """Clase Coche para practicar el uso de constructores."""
    
    # El constructor permite darle valores a los atributos desde el inicio
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    # Método que imprime la información del vehículo
    def describir(self):
        print(f"Información del vehículo: {self.__marca} {self.__modelo}, Año: {self.__anio}")

# --- Creación de varios objetos usando diferentes parámetros ---

# El taller pide crear varios objetos utilizando diferentes datos en el constructor
coche1 = Coche("Volkswagen", "Tiguan", 2014)
coche2 = Coche("Toyota", "Corolla", 2022)
coche3 = Coche("Mazda", "2", 2020)

# --- Mostramos la información de cada uno ---

# Se muestra por pantalla la información de los objetos creados
coche1.describir()
coche2.describir()
coche3.describir()