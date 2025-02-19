import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def factorial(n):
    if n < 0:
        return "Error: Factorial de número negativo"
    return math.factorial(n)

def potencia(base, exponente):
    return base ** exponente

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Suma de 5 y 3:", suma(5, 3))
    print("Resta de 10 y 4:", resta(10, 4))
    print("Multiplicación de 7 y 6:", multiplicacion(7, 6))
    print("División de 8 entre 2:", division(8, 2))
    print("Factorial de 5:", factorial(5))
    print("2 elevado a la 3:", potencia(2, 3))
    print("¿Es 17 un número primo?", es_primo(17))
<<<<<<< HEAD
Sexo o nel?
=======


""" 
Hola soy pakito kabeza :v 
"""
>>>>>>> 678c6b96e0bc27dae7c859775d292090135a091c

"""
Quien mierda esta modificando?
"""
