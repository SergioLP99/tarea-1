# Función que recibe un diccionario y agrega una clave-valor
def agregar_clave_valor(diccionario, clave, valor):
    diccionario[clave] = valor
    print(f"Diccionario despues de agregar: {diccionario}")
    return diccionario

# Función que recibe un diccionario y elimina una clave-valor
def eliminar_clave_valor(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    print(f"Diccionario despues de eliminar: {diccionario}")
    return diccionario

# Función que recibe un diccionario y modifica el valor de una clave
def modificar_valor_clave(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        print(f"Diccionario despues de modificar: {diccionario}")
        return True
    else:
        print(f"Clave no encontrada en el diccionario: {diccionario}")
        return False

# Función que combina dos diccionarios
def combinar_diccionarios(dic1, dic2):
    diccionario_combinado = {**dic1, **dic2}
    print(f"Diccionario combinado: {diccionario_combinado}")
    return diccionario_combinado

# Función que agrega elementos a un conjunto
def agregar_elemento_conjunto(conjunto, elemento):
    if elemento not in conjunto:
        conjunto.add(elemento)
        print(f"Conjunto despues de agregar: {conjunto}")
        return True
    else:
        print(f"Elemento ya existe en el conjunto: {conjunto}")
        return False

# Función que elimina un elemento de un conjunto
def eliminar_elemento_conjunto(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        print(f"Conjunto despues de eliminar: {conjunto}")
        return True
    else:
        print(f"Elemento no encontrado en el conjunto: {conjunto}")
        return False

# Función que combina dos conjuntos
def combinar_conjuntos(conjunto1, conjunto2):
    conjunto_combinado = conjunto1.union(conjunto2)
    print(f"Conjunto combinado: {conjunto_combinado}")
    return conjunto_combinado

# Función que regresa la diferencia de dos conjuntos
def diferencia_conjuntos(conjunto1, conjunto2):
    diferencia = conjunto1.difference(conjunto2)
    print(f"Diferencia de conjuntos: {diferencia}")
    return diferencia

# Función que agrega un elemento a una tupla
def agregar_elemento_tupla(tupla, elemento):
    nueva_tupla = tupla + (elemento,)
    print(f"Tupla despues de agregar: {nueva_tupla}")
    return nueva_tupla

# Función que elimina un elemento de una tupla
def eliminar_elemento_tupla(tupla, elemento):
    lista = list(tupla)
    if elemento in lista:
        lista.remove(elemento)
        nueva_tupla = tuple(lista)
        print(f"Tupla despues de eliminar: {nueva_tupla}")
        return nueva_tupla
    else:
        print(f"Elemento no encontrado en la tupla: {tupla}")
        return tupla

# Función que concatena dos tuplas
def concatenar_tuplas(tupla1, tupla2):
    nueva_tupla = tupla1 + tupla2
    print(f"Tupla concatenada: {nueva_tupla}")
    return nueva_tupla

# Función que revierte el orden de una tupla
def revertir_tupla(tupla):
    nueva_tupla = tupla[::-1]
    print(f"Tupla revertida: {nueva_tupla}")
    return nueva_tupla

# Función que recibe un diccionario y lo imprime
def imprimir_diccionario(diccionario):
    print(f"Diccionario: {diccionario}")

# Función que recibe una tupla y la imprime
def imprimir_tupla(tupla):
    print(f"Tupla: {tupla}")

# Función que recibe un conjunto y lo imprime
def imprimir_conjunto(conjunto):
    print(f"Conjunto: {conjunto}")

# Ejemplos de uso
dic = {"a": 1, "b": 2}
dic = agregar_clave_valor(dic, "c", 3)
dic = eliminar_clave_valor(dic, "b")
modificado = modificar_valor_clave(dic, "a", 10)
dic2 = {"d": 4, "e": 5}
dic_combinado = combinar_diccionarios(dic, dic2)

conjunto = {1, 2, 3}
agregado = agregar_elemento_conjunto(conjunto, 4)
eliminado = eliminar_elemento_conjunto(conjunto, 2)
conjunto2 = {3, 4, 5}
conjunto_combinado = combinar_conjuntos(conjunto, conjunto2)
diferencia = diferencia_conjuntos(conjunto, conjunto2)

tupla = (1, 2, 3)
nueva_tupla = agregar_elemento_tupla(tupla, 4)
nueva_tupla = eliminar_elemento_tupla(nueva_tupla, 2)
tupla2 = (5, 6)
tupla_concatenada = concatenar_tuplas(nueva_tupla, tupla2)
tupla_revertida = revertir_tupla(tupla_concatenada)

imprimir_diccionario(dic)
imprimir_tupla(tupla_revertida)
imprimir_conjunto(conjunto_combinado)
