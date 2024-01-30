cadena = "Hola, mundo!"
# Indexing: Es extaraer un caracter de una cadena de texto
print(cadena[0]) # El primer caracter de la cadena es el 0 y así sucesivamente
print(cadena[-1]) # Se puede extraer el último caracter de la cadena con -1


# Slicing: Es extraer un fragmento de una cadena de texto:

print(cadena[0:4]) # [x:y-1] Extrae desde la posicion 0(H) hasta la posicion 3(a) (4 no se incluye)
print(cadena[:4]) # Es lo mismo que [0:4]

print(cadena[6:11]) # Extraer la cadena "mundo"
print(cadena[6:-1]) # Extraer la cadena "mundo", -1 indica que no se incluye el último caracter y así sucesivamente
print(cadena[6:]) # Extrae desde la posicion 6 hasta el final de la cadena

# extraer toda la cadena (desde la posicion 0 hasta el final) 
print(cadena[0:])
print(cadena[:])

print(cadena[:-1]) # Extrae desde la posicion 0 hasta la penultima posicion, -1 indica que no se incluye el último caracter y así sucesivamente

# Slicing negativo:
print(cadena[-6:-1]) # Extrae la cadena "mundo"

# Slicing con saltos:
print(cadena[0::2]) # Extrae desde la posicion 0 hasta el final de la cadena con saltos de 2 en 2
print(cadena[::2]) # Es lo mismo que [0::2]


# SLICING Ejercicios:
telefono="9-8-7-6-5-4-3-2-1"
print(telefono[::2]) # Se extrae solo los numeros 

telefono2="-9-8-7-6-5-4-3-2-1"
print(telefono2[1::2]) # se extrae solo los guiones

cadena2="sucre"
print(cadena2[::-1]) # Se invierte la cadena gracias al salto negativo