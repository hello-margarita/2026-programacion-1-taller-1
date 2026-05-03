# Ejercicio 2: Encapsulamiento y Modificadores de Acceso
# Objetivo: Practicar el uso de atributos privados y métodos públicos (getter y setter).

class Coche:
    """Clase Coche con atributos privados."""
    
    # Definimos los atributos iniciales del vehículo (ahora con __ para que sean privados)
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    # --- Métodos para obtener la información (Getters) ---
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnio(self):
        return self.__anio

    # --- Métodos para modificar la información (Setters) ---
    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setAnio(self, anio):
        self.__anio = anio

    # Método que imprime la información del vehículo
    def describir(self):
        print(f"Información del vehículo: Marca {self.__marca}, Modelo {self.__modelo}, Año {self.__anio}")

# --- Creación de objetos (Instanciación) ---

# Creamos un objeto para probar el encapsulamiento
mi_coche = Coche("Volkswagen", "Tiguan", 2014)

# --- Uso de los nuevos métodos ---

# Mostramos la marca usando el método get
print(f"Marca obtenida: {mi_coche.getMarca()}")

# Cambiamos el modelo usando el método set
mi_coche.setModelo("Tiguan Trend & Fun")

# Se muestra por pantalla la información del objeto actualizado
mi_coche.describir()