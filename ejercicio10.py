# Ejercicio 10: Manejo de excepciones y clases personalizadas.
# Objetivo: Introducir el manejo de excepciones y la creación de excepciones personalizadas.

# 1. Definimos la Excepción Personalizada
class ExcesoVelocidadException(Exception):
    """Excepción lanzada cuando el coche supera el límite permitido."""
    def __init__(self, velocidad, mensaje="¡Cuidado! Has superado el límite de 200 km/h"):
        self.velocidad = velocidad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# 2. Clase Coche con lógica de control
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def incrementarVelocidad(self, incremento):
        nueva_velocidad = self.velocidad + incremento
        
        if nueva_velocidad > 200:
            # Lanzamos nuestra excepción personalizada
            raise ExcesoVelocidadException(nueva_velocidad)
        
        self.velocidad = nueva_velocidad
        print(f"El {self.marca} acelera a {self.velocidad} km/h. Todo bajo control.")

# --- Programa Principal (Manejo de la Excepción) ---

mi_coche = Coche("Mazda", "3")

print(f"--- Probando los límites del {mi_coche.marca} ---")

try:
    # Intento 1: Aceleración normal
    mi_coche.incrementarVelocidad(120)
    
    # Intento 2: Aceleración que causará el error
    print("Pisando el acelerador a fondo...")
    mi_coche.incrementarVelocidad(100) 

except ExcesoVelocidadException as e:
    # Aquí "atrapamos" el error y decidimos qué hacer sin que el programa muera
    print(f"ERROR DETECTADO: {e.mensaje}")
    print(f"Intentaste ir a {e.velocidad} km/h. El motor ha entrado en modo seguridad.")

print("\nLa excepción fue capturada. El sistema permanece estable y operativo.")