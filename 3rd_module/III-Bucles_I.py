"""
La ejecución repetida de una determinada parte del código se denomina bucle.
Un bucle se repite hasta que se le indique lo contrario.

En Python, tenemos dos bucles con los que podemos trabajar: while y for. En este capítulo hablaremos
de while. El ciclo while repite una ejecución siempre que se evalúe como True.

Veamos un ejemplo de while.
"""

contador = 0

while contador < 10:
    contador += 1 # Esta expresión es igual a contador = contador + 1
    print(f'El valor del contador es {contador}\n')



"""
El anterior ciclo while se estructura así:

- while: Palabra reservada que indica que se hará un ciclo tipo while

- contador < 10: Condición a evaluar. Si contador es menor que 10, el cuerpo del bucle
   se ejecutará. Si contador es mayor que 10, el bucle se ignora. Recordemos que contador en un principio
   vale 0, por lo que al evaluar la condicional entra al bucle.

- contador += 1: Esta es una suma de la variable contador, que suma 1 cada vez que se ejecuta el cuerpo
  del bucle. De no realizar esta sumatoria, while sería un bucle infinito, ya que contador nunca
  sería mayor que 10. Es lo que se llama contador o variable de control, con la cual podemos entrar
  o salir del bucle dependiendo de su valor.

"""



while contador <= 20+2: # Se pueden hacer operaciones sobre la marcha de una instrucción
    contador *= 2 # Haz lo que quieras con el cuerpo, pero ten en cuenta la variable contador
    print(f'El valor del contador es {contador}\n')



"""
NOTAS:

- La variable contable es la que va inmediatamente después de la palabra reservada while. No tiene que
  llamarse contador, puede ser a, hola, unaVariable o el nombre que tú quieras.

- Si la condición es False, tan pronto como se compruebe por primera vez, el cuerpo no se ejecuta
  ni una sola vez.

- Puedes poner bloques de if dentro del while, while dentro de while, la imaginación es tu límite.

- Hacer 'while True:' hace que se entre obligatoriamente al bucle

- Se puede agregar un else, en caso de que la condicional resulte False.
  Aunque la verdad no es del todo necesario...

"""



# __________________________________________________________________________________________


# Veamos un ejemplo de cómo interactuar y decidir sobre un bucle while


sigueEnBucle = True # Variable que nos permitirá seguir o salir del bucle

numberSecret = 5 # Número que el usuario debe adivinar



while sigueEnBucle: # Al contener el valor True, se empieza a ejecutar el cuerpo del bucle
    numberUser = int(input('Adivina el número secreto...')) # Número del usuario

    if numberUser == numberSecret:
        print(f'\nFelicidades, {numberUser} es el número secreto') # Se muestra si el usuario acertó
        sigueEnBucle = False # La condición se volverá a evaluar y al ser False sale del bucle

    elif numberUser < numberSecret: # Si el número del usuario es menor al secreto...
        print(f'\nUh, casi. Intenta de nuevo')

    else:
        print(f'\nLo siento, {numberUser} no es el número secreto')
else:
    print('Esto sobra :)')



# __________________________________________________________________________________________


# Es tu turno, intenta hacer ciclos while. ¡Diviértete!