# Nivel 1

import random

# Generar un ID de usuario aleatorio de 6 caracteres
def id_usuario_aleatorio():
    caracteres = 'Isaac5'
    id_generado = ''
    for _ in range(6):
        id_generado += random.choice(caracteres)
    return id_generado

# Generar múltiples IDs de usuario según la entrada del usuario
def generar_ids_usuario():
    caracteres = 'Isaac5'
    num_chars = int(input("Ingrese el número de caracteres: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    lista_ids = []
    for _ in range(num_ids):
        id_generado = ''
        for _ in range(num_chars):
            id_generado += random.choice(caracteres)
        lista_ids.append(id_generado)
    return lista_ids

# Generar un color RGB aleatorio
def color_rgb_aleatorio():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"

# Nivel 2

# Generar una lista de colores hexadecimales
def lista_colores_hexadecimales(n):
    caracteres = '0123456789abcdef'
    lista_colores = []
    for _ in range(n):
        color = '#'
        for _ in range(6):
            color += random.choice(caracteres)
        lista_colores.append(color)
    return lista_colores

# Generar una lista de colores RGB
def lista_colores_rgb(n):
    lista_colores = []
    for _ in range(n):
        lista_colores.append(color_rgb_aleatorio())
    return lista_colores

# Generar colores en formato hexadecimal o RGB
def generar_colores(tipo_color, n):
    if tipo_color == 'hexa':
        return lista_colores_hexadecimales(n)
    elif tipo_color == 'rgb':
        return lista_colores_rgb(n)
    else:
        return "Tipo de color no válido"

# Nivel 3

# Mezclar aleatoriamente los elementos de una lista
def mezclar_lista(lista):
    lista_mezclada = lista[:]
    random.shuffle(lista_mezclada)
    return lista_mezclada

# Generar una lista de 7 números aleatorios únicos en el rango de 0 a 9
def numeros_aleatorios_unicos():
    numeros = list(range(10))
    seleccionados = []
    for _ in range(7):
        numero = random.choice(numeros)
        numeros.remove(numero)
        seleccionados.append(numero)
    return seleccionados

# Filtrar solo los negativos y el cero en la lista
def filtrar_negativos_y_cero(numeros):
    resultado = []
    for num in numeros:
        if num <= 0:
            resultado.append(num)
    return resultado

# Aplanar una lista de listas de listas
def aplanar_lista(lista_anidada):
    resultado = []
    for sublista in lista_anidada:
        for inner_lista in sublista:
            for item in inner_lista:
                resultado.append(item)
    return resultado

# Crear una lista de tuplas siguiendo un patrón específico
def crear_tuplas():
    resultado = []
    for i in range(11):
        resultado.append((i, 1, i**1, i**2, i**3, i**4, i**5))
    return resultado

# Transformar una lista de países a una estructura específica
def transformar_paises(paises):
    resultado = []
    for sublista in paises:
        for pais, ciudad in sublista:
            resultado.append([pais.upper(), pais[:3].upper(), ciudad.upper()])
    return resultado

# Convertir una lista de países en una lista de diccionarios
def paises_a_diccionario(paises):
    resultado = []
    for sublista in paises:
        for pais, ciudad in sublista:
            resultado.append({'country': pais.upper(), 'city': ciudad.upper()})
    return resultado

# Convertir una lista de nombres en una lista de cadenas concatenadas
def nombres_a_cadenas(nombres):
    resultado = []
    for sublista in nombres:
        for nombre, apellido in sublista:
            resultado.append(nombre + " " + apellido)
    return resultado

# Función para calcular la pendiente de una ecuación lineal
def calcular_pendiente(x1, y1, x2, y2):
    if x2 != x1:
        return (y2 - y1) / (x2 - x1)
    else:
        return None