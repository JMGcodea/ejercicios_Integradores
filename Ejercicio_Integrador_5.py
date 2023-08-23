# Forma Iterativa
def get_int_iterative():
    while True:
        try:
            num = int(input("Ingrese un valor entero: "))
            return num
        except ValueError:
            print("Valor incorrecto. Intente otro.")

numero_entero = get_int_iterative()
print(f"Ha ingresado el número entero: {numero_entero}")

#Forma Recursiva
def get_int_recursive():
    try:
        num = int(input("Ingrese un valor entero: "))
        return num
    except ValueError:
        print("Valor incorrecto. Intente otro.")
        return get_int_recursive()

numero_entero = get_int_recursive()
print(f"Ha ingresado el número entero: {numero_entero}")
