#Ejercicio 1 - Escribir una función que calcule el máximo común divisor entre dos números

def calcular_mcd(x, y): # mcd = maximo común divisor
    while y:
        x, y = y, x % y
    return x
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
mcd = calcular_mcd(num1, num2)
print(f"El Máximo Común Divisor de {num1} y {num2} es {mcd}")