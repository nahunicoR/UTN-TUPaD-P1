import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

print('\n')
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene
numero = input("ingrese por favor un número: ")
print(f'El número es de: {len(numero)} dígitos')
print('\n')
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese por favor el primer número: "))
num2 = int(input("Ingrese por favor el segundo número: "))
sumatoria = 0

for i in range(num1 + 1,num2):
    sumatoria += i
print(f'La sumatoria total de los números comprendidos entre: {num1} y {num2} es de: {sumatoria}')
print('\n')

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
sumatoria = 0
opcion = 1
while opcion != 0:
    print('Ingrese 0, si desea salir.')
    opcion = int(input("Por favor ingrese un numero: "))
    sumatoria += opcion

print(f'La sumatoria total es de los números ingresados es de: {sumatoria}')
print('\n')

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
num_aleatorio = random.randint(0,9)
intentos = 0
num_usuario = 112
while num_usuario != num_aleatorio:
    num_usuario = int(input("Por favor ingresa un número entre 0 y 9 para adivinar: "))
    intentos += 1

print(f'Fueron necesarios {intentos}, para adivinar el resultado!!')
print('\n')

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, -1,-2) :
    print(i)
print('\n')

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
sumatoria = 0
numero_usuario = int(input('Por favor ingrese un número entero postivo: '))
for i in range(0, num_usuario + 1):
    sumatoria += i
print(f'La sumatoria de 0 a {numero_usuario} es de: {sumatoria}')
print('\n')

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
positivos = 0
negativos = 0
impares = 0
pares = 0
for i in range(100):
    num = int(input("Por favor ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1


    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(f'Conseguimos un total de: {pares} pares, {impares} impares, {positivos} positivos, {negativos} negativos') 
print('\n')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
for i in range(100):
    num = int(input("por favor ingrese un número: "))

promedio = num / 100
print(f'El promedio de los números ingresados es de: {promedio}')
print('\n')

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input('Ingresa un número por favor: ')
print((numero[::-1]))