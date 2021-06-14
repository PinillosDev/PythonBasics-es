"""
¿Hay una manera de realizar operaciones lógicas a nivel individual,
es decir, no evaluar una condición sino un bit?

Esto se logra através de los operadores bitwise. Con los operadores bitwise
podemos tratar los bits como condiciones de manera individual.

0 = False
1 = True

"""



# _____________________________________________________________________


"""
A diferencia de los operadores lógicos que usamos (and, or y not) para la lógica,
en operadores Bitwise se usan signos:

- & (ampersand) El equivalente a 'and'
- | (barra vertical) El equivalente a 'or'
- ~ (tilde) Equivale a 'not'

Además de estos signos, tenemos ^. Este símbolo se llama 'xor' y es un signo
de intercalación a nivel de bits.

La siguiente es la tabla de verdades de xor
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

NOTA:
- Los argumentos DEBEN ser de tipo int
"""



# _____________________________________________________________________


# Se crean las variables 'a' y 'b' que serán números binarios
a = 101
b = 101110

c = a & b # Salida: 100

"""
Esta salida sucede por lo siguiente:
Se completan los valores con 0 para que ambas variables tengan el mismo número de bits
101    = 000101
101110 = 101110

& es de conjunción, ambas deben ser True para resultar True
1 & 0 = False
1 & 1 = True

*Se evalúa de arriba a abajo
101    = 000101
101110 = 101110
       = 000100
"""



# _____________________________________________________________________


# Para realizar otros ejercicios solo será necesario cambiar el operador

d = a | b
print(d)

"""
| es de disyunción, al menos una debe ser True para resultar True
1 | 0 = True
1 | 1 = True
0 | 0 = False

*Se evalúa de arriba a abajo
101    = 000101
101110 = 101110
       = 101111
"""



# _____________________________________________________________________


"""
SHIFTING
El shifting o desplazamiento de Bits es una operación de bits individuales

Cuando hablamos de desplazar un bit, decimos que lo movemos a la izquierda
(multiplicar por dos) y desplazar un bit a la derecha es dividirlo entre dos.

Dos porque es la potencia base de los números binarios.

NOTA:
- Solo aplica para int
"""

# Para desplazar bits se usa > ó <
derecha = a >> b
izquierda = a << b