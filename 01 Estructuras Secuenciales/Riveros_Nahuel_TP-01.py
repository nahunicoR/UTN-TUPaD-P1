# Trabajo Practico Secuenciales
# Alumno Nahuel Nicolás Riveros Valgañón
# Se actualiza repositorio y se sube a GitHub.


# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. 
name = input("Ingrese su nombre por favor:")
print(f'Hola {name}!')


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados.
name = input("Ingrese su nombre por favor:")
last_name = input("Ingrese su apellido por favor:")
age = int(input("Ingrese su edad por favor:"))
residence = input("Ingrese lugar de residencia por favor:")
print(f'Soy {name} {last_name}, tengo {age} anios y vivo en {residence}')


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radius = float(input("Ingrese el valor del radio"))
area = 3.14 * radius ** 2
perimeter =  2 * 3.14 * radius
print(f'El área del círculo es de: {area}, y su perimetro es de: {perimeter}')


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
seconds = int(input("Ingrese la cantidad de segundos por favor:"))
hours = round(seconds / 3600, 2)
print(f'{seconds} segundos equivalen a {hours} horas')


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
number = int(input("Ingrese un número por favor"))

for i in range(1, 11) :
    print(f'{i} x {number} = {i * number}') 


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
n1 = int(input("Ingrese un numero distinto de 0 por favor"))
n2 = int(input("Ingrese otro numero distinto de 0 por favor"))
print(f'La suma entre los numeros es: {n1 + n2}')
print(f'La resta entre los numeros es: {n1 - n2}')
print(f'La muultiplicacion entre los numeros es: {n1 * n2}')
print(f'La division entre los numeros es: {n1 / n2}')


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.weigth = float(input("Ingrese por favor su peso actual."))
height = float(input("Ingrese por favor su altura."))
weight = float(input("Ingrese por favor su peso."))
imc =round(weight / height ** 2, 2)
print(f'Su masa corporal es de: {imc}%')


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
temp = float(input('Ingrese por favor la temperatura en Celcius'))
fahrenheit = round((9/5) * temp + 32)
print(f'La temperatura en grados Celcius: {temp}°,es equivalente a: {fahrenheit} Fahrenheit')


# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
n1 = int(input("Ingrese por favor 3 numeros."))
n2 = int(input("Ingrese por favor 3 numeros."))
n3 = int(input("Ingrese por favor 3 numeros."))
total = (n1 + n2 + n3) / 3
print(f'El promedio de los 3 numeros es de: {total}')

