"""
Ya hemos usado varias funciones, print(), range(), input() entre otras.

Todos estos elementos dentro de Python tienen algo en común: hacer más con menos.
Con la función len() podemos saber la longitud de una lista, algo que podríamos hacer
con un ciclo for.

Sin embargo, cada programa es diferente y debemos tener la forma de crear nuestras soluciones.
Es por esto que la mayoría de lenguajes nos permiten crear nuestras propias funciones.

Antes de crear una función, se tienen que cumplir las siguientes condiciones:

- Si un fragmento de código empieza a aparecer en más de una ocasión, considera aislarle
  en forma de una función.

- Si un fragmento de código se hace tan extenso que leerlo o entenderlo se hace complicado,
  considera dividirlo en varios problemas por separado e implementa cada uno de ellos
  como una función independiente.

"""



# _______________________________________________________________________________



# Tenemos una pieza de Software que toma un nombre como entrada e imprime el texto
# "mucho gusto" junto al nombre ingresado.


name = input('Por favor ingresa tu nombre...')

print(f'¡Mucho gusto, {name}!')


"""
Si tuviésemos que ejecutar una sola vez esta pieza estaría bien. Sin embargo, si el usuario
necesita usar varias veces esta pieza de código y en ocasiones distintas, lo mejor sería crear
una función. Esto, con el fin de implementarla las veces que queramos sin reescribirla.

"""


def saludo(name):
  print('\n\nEsta es la función que hemos creado\n')
  print(f'¡Mucho gusto, {name}!')


"""
def - Palabra reservada que indica que se creará una función, significa 'define'.

saludo - Es el nombre de la función, podemoso nombrarla como queramos.

(name) - Es el parámetro de la función, el valor que necesita para ejecutar la función.

De la siguiente manera se llama una función:
saludo('Juan')
  |      |
nombre  argumento
función

"""


# Para ver el resultado, debemos usar print(). Dentro o fuera de una función.
print(saludo('Juliana'))



# _______________________________________________________________________________



"""
ARGUMENTO vs PARÁMETRO

Los argumentos (como las variables en print()) son una sintaxis que nos permite pasarle
un valor a una función para que esta trabaje con base a ello.

Cuando nosotros creamos las funciones, tenemos acceso a los parámeteros. Un parámetro es
la definición de un argumento.


def MyFunction(valor):
                 |
             parámetro


MyFunction(valor)
             |
         argumemto


Los parámetros solo existen dentro de la definición de una función.

"""



# _______________________________________________________________________________



"""
NOTAS:
- No se debe invocar una función antes de que se haya definido.

- Una función y una variable no pueden compartir el mismo nombre.

- Los parámetros solo existen dentro de las funciones donde han sido definidos.

- Un parámetro puede usarse como una variable normal, pero solo dentro de la función.

def saludo(name):
  print(f'¡Mucho gusto, {name}!')

  (Nótese como 'name' es un parámetro que puede usarse como variable, SOLO DENTRO DE 'saludo')


- Cuando ejecutamos una función, podemos ver el resultado esperado y también 'None'.
  Esto no se tendrá en cuenta por ahora. Se hablará de ello luego.

- Las funciones no necesariamente necesitan un parámetro para funcionar.

"""



# _______________________________________________________________________________



"""
RESUMEN:

- Podemos crear nuestras propias funciones.

- Usamos def para crearlas. Luego el nombre, luego el parámetro (si se necesitan) y
  por último el cuerpo de la función.

- Hay una diferencia muy clara entre argumento y parámetro.

"""