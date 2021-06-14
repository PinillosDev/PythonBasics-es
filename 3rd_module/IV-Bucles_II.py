"""
El ciclo for es un bucle el cual contiene más funcionalidades que el ciclo while, ya que tiene una particularidad:
el ciclo for puede 'explorar' grandes cantidades de elementos. La siguiente es su estructura:

for i in variable:

Veamos algunas generalidades:

. for es la palabra reservada, indica que se hará un bucle tipo for

- No hay condiciones después de la palabra reservada for. No hay que pensar en condiciones, se evalúan
  internamente.

- La variable de control (i, en este caso) va después de la palabra for. Se suma automáticamente por cada vuelta
  que da en el ciclo.

- La palabra reservada 'in' introduce el elemento a recorrer, en este caso 'variable'.

"""


palabra = 'hola'

for i in palabra:
    print(i)


"""
DATO IMPORTANTE:
En programación se empieza a contar desde el cero, por lo que el primer elemento de algo es el elemento
número 0.

La variable de control 'i' recorrerá la variable palabra. Empezará desde el primer elemento, que es la h.
Cada giro que se hace en el bucle, i obtiene un nuevo valor. En este caso, el valor lo da la variable a recorrer.
En el segundo giro; i valdrá 'o', en el tercer 'l' y en el cuarto 'a'.

También se puede hacer:

for i in 'hola':
    print(i)

En resumen, i es la variable de control, se actualiza automáticamente y recorre elemento por elemento lo que le
indiquemos después de la palabra reservada in.

"""



# __________________________________________________________________________________________


"""
¿Qué pasa si quisiéramos recorrer una cantidad de números o indicar cuántas veces tiene que girar
el bucle? Esto parece complicado, porque como se dijo antes, se recorre elemento por elemento.
Si se pone 'for i in 8:', ¿se ejecutará ocho veces o una?

Para poder manejar números, usamos la función range(). Con range() le indicamos al programa hasta dónde
debe contar. for i in range(8) contará hasta 8.

La función range() tiene otras propiedades, si le ponemos range(1, 8) comenzará en 1 y terminará en 8.
por defecto empieza en 0.

Si se pone range(1, 8, 2) empezará en 1, terminará en 8 e irá contando de dos en dos.

En resumen: for i in range(1, 100, 10) contará desde 1 hasta 100 de 10 en 10. Primero, i valdrá 1,
luego tendrá como valor 10, luego 20 y así sucesivamente.

"""


# Aquí un ejemplo de un ciclo for

for i in range(20, 50, 2):
    print(i)



# __________________________________________________________________________________________


"""
NOTAS:

- El número fin, que es al que se llegará, no se cuenta. Es decir, si se pone 20 se contará hasta
  el 19. Llegado al 20, se sale del bucle.

- Si por ejemplo i equivale a 18 y se tiene que llegar hasta 20, pero tiene paso con 3;
  se cierra el bucle. Esto, debido a que 21 sobrepasa el rango.

"""