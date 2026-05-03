# Ejercicio 9: Composición
# Objetivo: Comprender cómo una clase puede estar compuesta por otras clases.

# 1. La clase componente: El Motor
class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def obtener_detalles(self):
        return f"{self.tipo} de {self.potencia} CV"

# 2. La clase compuesta: El Coche
class Coche:
    def __init__(self, marca, modelo, potencia_motor, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        # Aquí ocurre la composición: El coche "tiene un" motor
        self.motor = Motor(potencia_motor, tipo_motor)

    def describir(self):
        detalles_motor = self.motor.obtener_detalles()
        print(f"Este {self.marca} {self.modelo} ruge con un motor {detalles_motor}.")
        
        # Comentarios y sugerencias según la potencia del motor
        if self.motor.potencia > 300:
            print("Cuidado: Este motor tiene tanta potencia que despeina hasta a los calvos.")
        else:
            print("Es un motor modesto, ideal para ir por el pan sin despertar a los vecinos.")

# --- Pruebas de Composición ---

# Creamos dos vehículos con diferentes configuraciones de motor
mi_deportivo = Coche("Ferrari", "F8", 720, "V8 Turbo")
mi_compacto = Coche("Renault", "Twingo", 75, "1.0 Atmosférico")

print("--- Revisión de Taller ---")
mi_deportivo.describir()
print("-" * 30)
mi_compacto.describir()