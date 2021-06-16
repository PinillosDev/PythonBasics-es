"""
DEFINICIÓN DE RECURSIVIDAD:
Es un concepto que se utiliza en programación para definir funciones que se expresan
con su misma definición. Es decir, funciones que se llaman a sí mismas.

Esto es muy útil, debido a que nos permite simplificar el código.

"""



# _______________________________________________________________________________



"""
El factorial de un entero positivo n se define en principio como el producto de
todos los números enteros positivos desde 1 hasta n. Por ejemplo: 5! = 1×2×3×4×5 = 120

Básicamente un factorial de n número, es el resultado de sus números anteriores multiplicados.


La siguiente es su representación a manera de función.

def factorial(n): 
    return n * factorial(n-1)
           |        |
          se      por el número anterior a n
      multiplica


"""



# _______________________________________________________________________________



def factorial(n): 
    return n * factorial(n-1)

factorial(800)



"""
Sin embargo, a la hora de ejecutarse aparece el siguiente error:
RecursionError: maximum recursion depth exceeded

El error sucede porque la función se llamó a sí misma infinitas veces.
Esto se debe a que se necesita un caso base. Un caso base en programación es aquella
condición que de cumplirse, la función toma una reacción diferente.

Nuestro caso base será: si n == 1, entonces deja de llamar la función.

"""


def factorial(n): 
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(800))