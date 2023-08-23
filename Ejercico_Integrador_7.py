class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Métodos getters y setters de Persona...

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, valor):
        if isinstance(valor, Persona):
            self._titular = valor
        else:
            print("El titular debe ser una instancia de Persona.")
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print("Titular:", self.titular._nombre)
        print("Cantidad:", self.cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self._cantidad -= cantidad

# Solicitar y validar datos al usuario para el titular de la cuenta
nombre_titular = input("Ingrese el nombre del titular: ")
edad_titular = int(input("Ingrese la edad del titular: "))
dni_titular = input("Ingrese el DNI del titular: ")

titular_persona = Persona(nombre_titular, edad_titular, dni_titular)

# Solicitar datos al usuario para la cuenta
cantidad_inicial = float(input("Ingrese la cantidad inicial en la cuenta: "))

# Crear una instancia de Cuenta
cuenta1 = Cuenta(titular_persona, cantidad_inicial)

# Mostrar datos iniciales
cuenta1.mostrar()

# Ingresar dinero
cantidad_ingresar = float(input("Ingrese la cantidad a ingresar: "))
cuenta1.ingresar(cantidad_ingresar)
cuenta1.mostrar()

# Retirar dinero
cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
cuenta1.retirar(cantidad_retirar)
cuenta1.mostrar()
