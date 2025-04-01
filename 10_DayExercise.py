# Nivel 1

# Iterar de 0 a 10 usando for y while
print("Iteración con for:")
for i in range(11):
    print(i)

print("Iteración con while:")
i = 0
while i <= 10:
    print(i)
    i = i + 1

# Iterar de 10 a 0 usando for y while
print("Iteración inversa con for:")
for i in range(10, -1, -1):
    print(i)

print("Iteración inversa con while:")
i = 10
while i >= 0:
    print(i)
    i = i - 1

# Imprimir un triángulo de 7 niveles
print("Triángulo:")
nivel = 1
while nivel <= 7:
    print("#" * nivel)
    nivel = nivel + 1

# Imprimir un patrón de 8x8
print("Patrón de 8x8:")
contador = 0
while contador < 8:
    print("# # # # # # # #")
    contador = contador + 1

# Imprimir una tabla de multiplicación
print("Tabla de multiplicación:")
numero = 0
while numero <= 10:
    print(numero, "x", numero, "=", numero * numero)
    numero = numero + 1

# Iterar sobre una lista e imprimir sus elementos
frutas = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("Lista de elementos:")
indice = 0
while indice < len(frutas):
    print(frutas[indice])
    indice = indice + 1

# Imprimir números pares del 0 al 100
print("Números pares:")
n = 0
while n <= 100:
    print(n)
    n = n + 2

# Imprimir números impares del 0 al 100
print("Números impares:")
n = 1
while n <= 100:
    print(n)
    n = n + 2

# Nivel 2

# Sumar todos los números del 0 al 100
suma_total = 0
numero = 0
while numero <= 100:
    suma_total = suma_total + numero
    numero = numero + 1
print("La suma de todos los números es:", suma_total)

# Sumar los números pares e impares del 0 al 100
suma_pares = 0
suma_impares = 0
numero = 0
while numero <= 100:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
    numero = numero + 1
print("La suma de los pares es:", suma_pares, "y la suma de los impares es:", suma_impares)

# Nivel 3

# Extraer países que contengan la palabra "tierra"
paises = ['Argentina', 'Australia', 'Bolivia', 'Colombia', 'Tierra del Fuego', 'Finlandia', 'Groenlandia']
paises_con_tierra = []
indice = 0
while indice < len(paises):
    if "tierra" in paises[indice].lower():
        paises_con_tierra.append(paises[indice])
    indice = indice + 1
print("Países con 'tierra':", paises_con_tierra)

# Invertir una lista de frutas
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas_invertidas = []
indice = len(frutas) - 1
while indice >= 0:
    frutas_invertidas.append(frutas[indice])
    indice = indice - 1
print("Lista de frutas invertida:", frutas_invertidas)

# Contar el número total de idiomas en una lista de datos ficticia
idiomas = ['Inglés', 'Español', 'Francés', 'Inglés', 'Alemán', 'Chino', 'Español', 'Portugués']
idiomas_unicos = []
for idioma in idiomas:
    if idioma not in idiomas_unicos:
        idiomas_unicos.append(idioma)
print("Número total de idiomas:", len(idiomas_unicos))

# Encontrar los 10 idiomas más hablados (datos ficticios)
idiomas_mas_hablados = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Arabe': 600, 'Hindi': 800, 'Portugués': 220, 'Bengalí': 270, 'Ruso': 260, 'Japonés': 125}
idiomas_ordenados = list(idiomas_mas_hablados.items())
idiomas_ordenados.sort(key=lambda x: x[1], reverse=True)
print("Los 10 idiomas más hablados:", idiomas_ordenados[:10])

# Encontrar los 10 países más poblados (datos ficticios)
poblacion_paises = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Pakistán': 220, 'Brasil': 212, 'Nigeria': 206, 'Bangladesh': 165, 'Rusia': 144, 'México': 126}
paises_ordenados = list(poblacion_paises.items())
paises_ordenados.sort(key=lambda x: x[1], reverse=True)
print("Los 10 países más poblados:", paises_ordenados[:10])