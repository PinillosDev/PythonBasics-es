"""
Cualquier tipo de computadora entiende un solo idioma, el cual conocemos como numeración binaria.
Los números binarios no son más que un sistema numérico que usa el dos como base,
a diferencia de nuestro sistema numérico tradicional que usa el 10 como base.

Para representar números binarios solo tenemos que contar hasta 1,
empezando por el 0 y agregar 1 y 0 cada vez que necesitemos.


1 -> 1
2 -> 10
3 -> 11
4 -> 100
5 -> 101
6 -> 110
7 -> 111
8 -> 1000
9 -> 1001
10 -> 1010


Sin embargo, hay una manera más fácil de convertir un número de base 10 a un número
de base 2. Esto se logra mediante la siguiente tabla.


|---|---|---|---|---|---|---|---|
|128|64 |32 |16 |8  |4  |2  |1  |


La anterior tabla representa un concepto sumamente importante en informática:
el concepto de bit y byte. Básicamente un bit es un espacio en memoria, es una casilla.
Literal puede ser una de las casillas de la tabla anterior, como 32 o 8.
Por otro lado, un byte son ocho bits.

Un Byte es un espacio en memoria donde podemos guardar cosas ;)
"""



# _____________________________________________________________________


"""
Podemos pasar números decimales a binarios de la siguiente forma

|---|---|---|---|---|---|---|
|64 |32 |16 |8  |4  |2  |1  |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 1 |

El anterior ejercicio surgió de convertir 5 a binario
5 = 101


|---|---|---|---|---|---|---|
|64 |32 |16 |8  |4  |2  |1  |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |

46 = 101110

"""