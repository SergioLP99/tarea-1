Tarea 1
Este repositorio contiene ejercicios prácticos de manipulación de estructuras de datos en Python, como parte de la asignatura de programación.

Contenido del Proyecto
El archivo principal es:

practica1.py: Contiene funciones para la manipulación de diccionarios, conjuntos y tuplas, así como ejemplos de uso de cada una de estas funciones.
Estructura de practica1.py
Funciones para Diccionarios
agregar_clave_valor(diccionario, clave, valor): Agrega una clave-valor.
eliminar_clave_valor(diccionario, clave): Elimina una clave-valor.
modificar_valor_clave(diccionario, clave, nuevo_valor): Modifica el valor de una clave.
combinar_diccionarios(dic1, dic2): Combina dos diccionarios.
imprimir_diccionario(diccionario): Imprime el diccionario.
Funciones para Conjuntos
agregar_elemento_conjunto(conjunto, elemento): Agrega un elemento.
eliminar_elemento_conjunto(conjunto, elemento): Elimina un elemento.
combinar_conjuntos(conjunto1, conjunto2): Combina dos conjuntos.
diferencia_conjuntos(conjunto1, conjunto2): Encuentra la diferencia entre dos conjuntos.
imprimir_conjunto(conjunto): Imprime el conjunto.
Funciones para Tuplas
agregar_elemento_tupla(tupla, elemento): Agrega un elemento.
eliminar_elemento_tupla(tupla, elemento): Elimina un elemento.
concatenar_tuplas(tupla1, tupla2): Concatena dos tuplas.
revertir_tupla(tupla): Revierte el orden de los elementos.
imprimir_tupla(tupla): Imprime la tupla.
Ejemplos de Uso
python
Copiar código
# Ejemplos de uso de funciones en practica1.py
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
Contribuciones
Las contribuciones son bienvenidas. Puedes hacer un fork del repositorio, hacer tus cambios y enviar un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más información.
