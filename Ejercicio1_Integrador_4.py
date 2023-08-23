def contar_frecuencia(cadena):
    palabras = cadena.split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(diccionario):
    palabra_mas_comun = max(diccionario, key=diccionario.get)
    frecuencia_mas_comun = diccionario[palabra_mas_comun]
    return palabra_mas_comun, frecuencia_mas_comun

cadena = input("Ingrese una cadena de caracteres: ")
resultado_frecuencia = contar_frecuencia(cadena)
palabra_repetida, frecuencia_repetida = palabra_mas_repetida(resultado_frecuencia)

print("Frecuencia de palabras:")
for palabra, frec in resultado_frecuencia.items():
    print(f"{palabra}: {frec}")

print(f"Palabra más repetida: {palabra_repetida} (Frecuencia: {frecuencia_repetida})")