# Ejercicio 4: Herencia
# Objetivo: Aplicar el concepto de herencia para extender una clase.

# Clase Padre (la base para los demás)
class Vehiculo:
    def __init__(self, velocidad_inicial=0):
        self.velocidad = velocidad_inicial

    def acelerar(self):
        self.velocidad += 10
        print(f"El vehículo ha acelerado. Velocidad actual: {self.velocidad} km/h")

# Clase Hija: Coche (Hereda de Vehiculo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_inicial=0):
        # Usamos super() para llamar al constructor del padre
        super().__init__(velocidad_inicial)
        self.marca = marca
        self.modelo = modelo

    def tocar_bocina(self):
        print("¡Beep beep! El vehículo está pitando.")

# Clase Hija: Bicicleta (Hereda de Vehiculo)
class Bicicleta(Vehiculo):
    def __init__(self, tipo, velocidad_inicial=0):
        super().__init__(velocidad_inicial)
        self.tipo = tipo # Ejemplo: Urbana, de Montaña

    def usar_timbre(self):
        print("¡Rin rin! La bicicleta está avisando.")

# --- Pruebas de Herencia ---

# Creamos un coche y una bicicleta
mi_carro = Coche("Volkswagen", "Tiguan")
mi_bici = Bicicleta("Montaña")

# Ambos pueden usar el método acelerar() porque lo heredaron del padre
mi_carro.acelerar()
mi_bici.acelerar()

# Cada uno usa su propio método especial
mi_carro.tocar_bocina()
mi_bici.usar_timbre()