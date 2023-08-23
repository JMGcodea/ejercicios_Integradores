class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if valor.strip() != "":
            self._nombre = valor
        else:
            print("El nombre no puede ser vacío.")
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self._edad = valor
        else:
            print("La edad debe ser un valor positivo.")
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, valor):
        if len(valor) == 8:  # Validación simple de longitud de DNI
            self._dni = valor
        else:
            print("El DNI debe tener 8 dígitos.")
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Solicitar y validar datos al usuario
nombre_valido = False
while not nombre_valido:
    nombre = input("Ingrese su nombre: ")
    if nombre.strip() != "":
        nombre_valido = True
    else:
        print("El nombre no puede estar vacío.")

edad_mayor = False
while not edad_mayor:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad >= 0:
            edad_mayor = True if edad >= 18 else False
        else:
            print("La edad debe ser un valor positivo.")
    except ValueError:
        print("Ingrese una edad válida.")

dni_valido = False
while not dni_valido:
    dni = input("Ingrese su DNI: ")
    if len(dni) == 8:
        dni_valido = True
    else:
        print("El DNI debe tener 8 dígitos.")

# Crear una instancia de Persona
persona1 = Persona(nombre, edad, dni)

persona1.mostrar()
if edad_mayor:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
