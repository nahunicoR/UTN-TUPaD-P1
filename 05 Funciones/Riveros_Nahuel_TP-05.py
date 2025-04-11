import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print('Hola Mundo!')

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return f'Hola {nombre}'

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre,apellido,edad,residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return round(math.pi * (radio ** 2),2)

def calcular_perimetro_circulo(radio):
    return round(2 * math.pi * radio,2)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.
def segundos_a_horas(segundos):
    return round(segundos / 3600,2)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.
def calcular_imc(peso,altura):
    return round(peso / ( altura ** 2), 2)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a,b,c):
    return round((a + b + c) / 3, 2)

def __main__():
    print('ejercicio 1')
    imprimir_hola_mundo()

    print('----------------------')
    print('ejercicio 2')
    nombre = input('Por favor ingrese su nombre para saludarlo: ')
    print(saludar_usuario(nombre))

    print('----------------------')
    print('ejercicio 3')
    nombre = input('Por favor ingrese su nombre: ')
    apellido = input('Por favor agregue su apellido: ')
    edad = int(input('Por favor agregue su edad: '))
    residencia = input('Por favor agregue su residencia: ')
    informacion_personal(nombre,apellido,edad,residencia)

    print('----------------------')
    print('ejercicio 4')
    radio = float(input("Por favor ingrese el valor del radio: "))
    print(f'El valor del área del círculo es de: {calcular_area_circulo(radio)}')
    print(f'El valor del perímetro del círculo es de: {calcular_perimetro_circulo(radio)}')
    
    print('----------------------')
    print('ejercicio 5')
    segundos = int(input('Por favor ingrese la cantidad de segundos: '))
    print(f'La cantidad de {segundos}, corresponde a {segundos_a_horas(segundos)} horas')

    print('----------------------')
    print('ejercicio 6')
    numero = int(input('Por favor ingrese el número para la tabla de multiplicar: '))
    tabla_multiplicar(numero)

    print('----------------------')
    print('ejercicio 7')
    num1 = int(input('Por favor ingrese el primer número: '))
    num2 = int(input('Por favor ingrese el segundo número: '))
    resultado = operaciones_basicas(num1,num2)
    print(f'El resultado de la suma es de: {resultado[0]}')
    print(f'El resultado de la resta es de: {resultado[1]}')
    print(f'El resultado de la multiplicación es de: {resultado[2]}')
    print(f'El resultado de la división es de: {resultado[3]}')

    print('----------------------')
    print('ejercicio 8')
    peso = float(input('Por favor ingrese su peso en kg: '))
    altura = float(input('Por favor ingrese su altura en metros: '))
    print(f'Su índice IMC es de: {calcular_imc(peso, altura)}')

    print('----------------------')
    print('ejercicio 9')
    celsius = float(input('Por favor ingrese los grados que quiera pasar: '))
    print(celsius_a_fahrenheit(celsius))

    print('----------------------')
    print('ejercicio 10')
    print('Vamos a calcular el promedio')
    n1= int(input('Por favor ingrese el valor del primer número: '))
    n2= int(input('Por favor ingrese el valor del segundo número: '))
    n3= int(input('Por favor ingrese el valor del tercer número: '))
    print(f'El valor promedio total es de: {calcular_promedio(n1,n2,n3)}')

    print('Gracias por utilizar el servicio de LockNCode Incorporated.')

__main__()