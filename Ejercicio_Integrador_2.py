def mcd(x, y): # mcd = maximo común divisor
    while y:
        x, y = y, x % y
    return x

def mcm(x, y): # mínimo común multiplo
    return (x * y) // mcd(x, y) 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = mcm(num1, num2)
print(f"El mínimo común múltiplo de {num1} y {num2} es {resultado}")