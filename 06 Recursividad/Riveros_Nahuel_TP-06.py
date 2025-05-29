# 1) Crea una función recursiva que calcule el factorial de un número.
#  Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n < 0 :
        print('No se puede calcular el factorial de un número menor que 1')
    if n == 0 :
        return 1
    else:
        print(f'{n} * {n - 1}')
        return factorial(n-1) * n
    
numero_factorial = int(input('Ingrese un numero para calcular el factorial: '))
print(factorial(numero_factorial))


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
#  Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)        
    
numero_fibonacci = int(input('Ingrese un número para calcular serie Fibonacci: '))

for i in range(numero_fibonacci):
    print(fibonacci(i))
  

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑚(𝑚−1).
#  Prueba esta función en un algoritmo general.

def potencia_num_base(exponente, base):
    if(exponente == 0):
        return 1
    else:
        return base * potencia_num_base(exponente-1,base)
    
numero_exponente = int(input('Ingresa el numero de exponente: '))
numero_base = int(input('Ingresa el numero de base: '))

print(potencia_num_base(numero_exponente, numero_base))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
#  y devuelva su representación en binario como una cadena de texto.

def decimal_binario_recursivo(num):
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    else:
        return decimal_binario_recursivo(num //2) + str(num % 2)


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.La solución debe ser recursiva.
#    No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])


def suma_digitos(n):
    if n < 10:
        return n
    else: 
        return (n % 10) + suma_digitos(n // 10)
    

# 6) Un niño está construyendo una pirámide con bloques.
#    En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#    Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
#    Ejemplos:
#    contar_bloques(1) → 1 (1)
#    contar_bloques(2) → 3 (2 + 1)
#    contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
print(contar_bloques(5))


# 7)  Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
#    Ejemplos:
#    contar_digito(12233421, 2) → 3
#    contar_digito(5555, 5) → 4

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        if ultimo_digito == digito :
            return 1 + contar_digito(resto_numero, digito)
        else: 
            return contar_digito(resto_numero,digito)