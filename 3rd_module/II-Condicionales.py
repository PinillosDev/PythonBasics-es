"""
Cuando está lloviendo, ¿sales a trotar? ¿Sí o no? Esta misma lógica es la que se tratará en este apartado.

Una condicional es el flujo que seguirá el programa conforme el estado de una variable. Es decir, el clima es una
variable. La condicional es si hace buen clima. Si hace buen clima, saldremos a caminar. De lo contrario
nos quedamos en casa. Una condicional no es más que el cómo decide nuestro programa qué hacer o qué no hacer.

Una condicional se ve así:

si clima == soleado:
    salimos a trotar
sino:
    nos quedamos en casa

Veámos un ejemplo más realista...

"""



clima = input('¿Hace buen clima?  (s/n)') # le indicamos al usuario que ingrese 's' o 'n' dependiendo del clima

if clima == 'n': # Si el clima es malo, entonces...
    print('Día de películas') # No salimos
else: # Si no, entonces...
    print('¡Vamos a trotar!') # Salimos


"""
La variable clima contendrá un valor el cual el usuario le dará valor, ya sea 's' o 'n'.
Depende de lo que ingrese el usuario, se ejecutará la instrucción de la línea 24 o la instrucción
de la línea 26.
"""



# _______________________________________________________________________________________________


"""
Hagámos un ejemplo aún más realista. Se nos pide hacer un programa que reciba un número como
entrada y determine si es mayor que 20 o no. Si es mayor que 20, mostrará un mensaje indicando
que el número es mayor que 20. De lo contrario, se debe mostrar en la pantalla un mensaje que
indique que el número es menor que 20.

"""



numberUser = int(input("Ingresa un número mayor a 0..."))

if numberUser > 20:
    print('El número es mayor que 20')
else:
    print('El número es menor que 20')



# _______________________________________________________________________________________________


"""
NOTAS:

- Siempre, después de la condicional debe ir dos puntos, esto indica que la instrucción
  que evalúa la condicional ha terminado y lo siguiente es el cuerpo.

- Si se entra a una rama if, no se entrará a las ramas elif o else. El flujo siempre va de arriba
  a abajo. Una vez se entre a un else, no se puede subir a un if o elif. En resumen, solo se puede
  entrar a una rama por condición.

- A la parte de la instrucción que se encuentra dentro del if o del else se le llama cuerpo

    if numberUser > 20:
        print('El número es mayor que 20') <- cuerpo del if
    else:
        print('El número es menor que 20') <- cuerpo del else

- En el cuerpo de una variable puede haber más que print; puede haber operacione matemáticas,
    creación de otras variables, operaciones con valores booleanos o incluso más condicionales.

"""



# _______________________________________________________________________________________________


"""
Ejemplo: se nos pide hacer un programa que determine si un número entero ingresado por el usuario
es menor o mayor que 20.

- Si es mayor que 20, se le debe sumar 10 y mostrar en pantalla un mensaje junto con su valor.
- Si es menor que 20, se le debe restar 5 y mostrar en pantalla un mensaje junto con su valor.

"""



number = int(input('Ingrese un número...'))

if number > 20: # Si el número es mayor que 20...
    number = number + 10 # Se le adiciona 10
    print('El valor actual es:', number)
else:
    number = number - 5 # Se le resta 5
    print('El valor actual es:', number)



"""
NOTAS:

- Se puede hacer un print para mostrar variables junto con texto más fácilmente, sin la necesidad de (,)
  Se hace así: print(f'Aquí se muestra el texto, junto con mi {variable}')
  Antes de poner las comillas, se pone una f y las variables deben ir dentro de corchetes ({}).

- Si el tema se te complica, te aconcejo que te pongas en el lugar del dato y te preguntes qué camino
  tomarás. De esa forma te acostumbrarás a trazar un camino imaginario por dónde fluirían los datos
  de acuerdo a su valor.

"""



# _______________________________________________________________________________________________


"""
Sin embargo, las condiciones de un programa no solo son cosa de if y else, también existe elif.
Son tres las condicionales: if, elif y else, a este orden se le denomina cascada.

elif viene a ser como la segunda opción verdadera. Veamos su papel...
"""



# Se crea un programa para evaluar si un número decimal es menor que diez, mayor o igual.
numeroDesconocido = float(input()) # Ojo, trabajaremos con un número float

if numeroDesconocido == 10.0:
    print('El número es 10.0')
elif numeroDesconocido > 10.0:
    print('El número es mayor que 10.0')
else:
    print('El número es menor que 10.0')



"""
NOTAS:

- SIEMPRE debe ir primero el if, luego el elif y por último el else.

- No debes usar un elif o else sin un if precedente.

- Puedes usar un elif cuantas veces quieras, siempre y cuando vaya después del if

"""



# Ahora intentalo tú, haz un programa que determine si dos números son iguales o diferentes. O lo que quieras, idk...