"""
Hoy veremos dos instrucciones particulares. Es un tema muy fácil de entender y de aplicar, así que relax.

¿Qué podríamos hacer si queremos salir de un bucle en ejecución o ir al siguiente ciclo?
Estas acciones son posibles con las opciones break y continue.


break:
Con break, salimos inmediatamente de un ciclo, así esté en plena ejecución.

continue:
Con continue saltamos directamente al siguiente ciclo. La variable de control aumenta su valor automáticamente.

"""



for i in range(1, 11):
    if i == 8:
        break # Si i es 8 se sale del bucle
    elif i%2 == 0: # Si el residuo de i / 2...
        continue # ...es un número par, salta al siguiente ciclo
    else:
        print(i)