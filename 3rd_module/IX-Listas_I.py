"""
Hasta ahora hemos visto cómo podemos guardar un valor en una variable.
Este tipo de variables donde solo se guarda un dato a la vez (ya sea int, str, etc) se llama escalar.

¿Te imaginas una tipo de dato donde puedas guardar más variables? Algo así como una variable donde
puedas guardar int, float, string y hasta otras variables.
Este tipo de dato existe y se llaman lista. Es como una variable, pero a la vez no, porque hace
cosas que una variable escalar no puede hacer. En resumen: las listas son un tipo de dato en la que puedes guardar
lo que quieras.
"""



# _______________________________________________________________________________



MyList = [123, 'string', 3.1416, 'a'] # Así se ven las listas

"""
Veamos su anatomía:
- MyList es el nombre
- [] Todo lo que va dentro de los corchetes son los elementos de la lista, los cuales
  deben ir separador por comas.
"""



# _______________________________________________________________________________



"""
¿Cómo podemos ver, editar y eliminar elementos dentro de una lista?

Antes de todo, debemos entender el concepto de índice.

Un índice es la manera en la que identificamos un elemento dentro de una lista.
Los índices son números, que empiezan desde cero.

           0       1        2     3
MyList = [123, 'string', 3.1415, 'a']

Y así sucesivamente con los demás elementos.
Cuando decimos el elemento #2, hacemos referencia a 3.1415.

"""



# _______________________________________________________________________________



# VER ELEMENTOS DE UNA LISTA

print(MyList[1]) # Con los índices podemos acceder a los elementos de una lista



# CAMBIAR ELEMENTOS DE UNA LISTA

MyList[0] = MyList[2] # Cambiar elementos por otros elementos de la misma lista

MyList[3] = 'b' # Cambiar elementos por otro dato que queramos



# ELIMINAR ELEMENTOS DE UNA LISTA

del MyList[2] # la instrucción 'del' es para eliminar un elemento de una lista con base en un índice



"""
NOTA:
- Cuando se dice 'espacio en memoria' se hace referencia al lugar donde en verdad se gurda algo.
  Una variable es una representación de ese espacio en memoria.

- Si a una variable se le asigna el nombre de una lista, no hace una copia de una lista,
  pero hace que las variable apunte a la misma lista en memoria. Es decir, si se le asigna
  a una variable una lista, tanto la lista como la variable apuntarán al mismo espacio en memoria.

- El nombre de la lista es una representación de un espacio en memoria.
  Es por eso mismo, que cuando haces variable = MyList y cambias el valor de 'variable', los cambios
  también se verán en 'MyList', porque ambas son representaciones diferentes del mismo espacio en memoria.

"""



# _______________________________________________________________________________


# FUNCIONES VS MÉTODOS

"""
Ya hemos visto qué es una función y hemos trabajado con ellas. Pero ahora se introducirá un concepto
que es muy importante, y es el de los métodos.

Una función es una estructura de código que produce o modifica algo. Sin embargo,
una función puede ser aplicable a todo el código es decir, puedes aplicar print() a números,
cadenas y listas. ¿Existe una función que solo sea aplicable a datos tipo int, por ejemplo?

Los métodos son como las funciones, pero solo se pueden aplicar a ciertos tipo de datos. Es decir,
hay métodos para listas, métodos para cadenas, métodos para enteros, etc. No se puede aplicar un método
de lista en un tipo de dato numérico.

Los métodos son importantes porque nos permiten tener mayor control en el flujo de los tipos de datos
y el cómo se comportan estos en nuestro programa.

Un método tiene la siguiente estructura:

data.method(argumento)

data: Es la variable a manipular, debe ser un tipo de datos específico.
method: El nombre del método

"""



# Veamos un ejemplo de método para un tipo de dato string



# NOTA: Las cadenas también tienen índices

saludo = 'Holaaa'
print(saludo[2]) # Salida: 'l'

saludo.count('a') # El método count cuenta las veces que un argumento está en una variable
# salida: 3

# Para más información acerca de métodos para strings:
# https://controlautomaticoeducacion.com/python-desde-cero/metodos-string-en-python/



"""
Espero que te hayan quedado claro los temas vistos en este capítulo:
- Diferencia entre una variable escalar y una lista
- Cómo crear y manipular básicamente una lista
- Diferencia entre función y método

¡En el siguiente capítulo aprenderás más cosas acerca de las listas! ;)

"""