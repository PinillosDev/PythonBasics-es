"""
Lo primero que aprenderemos es a mostrar texto en la pantalla. Es decir, imprimir lo que queramos para poder
verlo.

Esto se hace a través de print(), la cuál es una función (hablaremos de ello más adelante) que nos permite
mostrar lo que queramos en nuestra pantalla. Su sintaxis es sencilla...

print('Hola Mundo')

- print: El nombre de la función
- (): Entre paréntesis va lo que queramos mostrar
- '': Entre comillas simples va el TEXTO que queramos mostrar

"""



# Este es tu primer hola mundo, juega con él y cambia el texto :)


print('Hola mundo!')


# _________________________________________________________________

"""
¿Qué más podemos hacer con print? ¿Se puede mostrar más que un texto?
Sí, se pueden hacer más cosas. Hay casos en los que no deben estar incluidas las comillas para mostrar algo.

En los casos en los que se deseen mostrar números, por ejemplo, las comillas no son necesarias
Por ejemplo, para mostrar una suma se hace: print(8+1)
"""

# ¿Cuál crees que sea la diferencia entre estas dos instrucciones? ¡Ejecuta el código!

print('5+4')
print(5+4)


"""
Exacto:
Todo lo que vaya entre comillas, sea número o lo que sea, será tomado como texto.
"""



# _________________________________________________________________

"""
¿Se puede mostrar texto y números a la vez?

Sí, en ese caso se usa la coma (,), la cual nos sirve para indicarle al computador que mostrará algo diferente.
"""

print('Esto es una suma:', 7+6)

# Podemos usar la coma cuantas veces queramos, aparte de que pueden ser diferentes operaciones, como restas

print('Una suma:', 6+2, 'una resta:', 9-2)



# _________________________________________________________________

"""
Una característica interesante es el new line (nueva línea). Nos permite mostrar varias instrucciones en una linea
Es decir, lo que hacíamos en dos líneas lo podemos hacer en una sola. Tomemos el ejemplo de arriba...

print('5+4')
print(5+4)

Si bien esto es correcto, podemos ahorrarnos tiempo con \n
La barra invertida (\) le indica al computador que el siguiente carácter es diferente y 'n' de new line
indica que lo que viene después debe mostrarse en una nueva línea.

IMPORTANTE: Debe ir con el texto. Es decir, dentro de las comillas.
"""
print('5+4\n', 5+4)

# Se muestra 5+4 y un espacio abajo 9