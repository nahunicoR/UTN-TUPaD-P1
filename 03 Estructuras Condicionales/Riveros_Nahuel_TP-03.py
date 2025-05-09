from statistics import mode, median, mean
import random

# # 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# # deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if(edad > 18):
    print("Es mayor de edad")


# # 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# # mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# # mensaje “Desaprobado”.
nota = int(input("Ingrese por favor, su nota: "))
if(nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")


# # 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# # número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# # contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# # operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("Ingrese un número por favor: "))
if(num % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# # 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# # siguientes categorías pertenece:
# # ● Niño/a: menor de 12 años.
# # ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# # ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# # ● Adulto/a: mayor o igual que 30 años.
edad_persona = int(input("Por favor ingrese su edad: "))
if(edad_persona < 12):
    print("Usted es un Niño")
elif(edad_persona <= 18 and edad_persona >= 12):
    print("Usted es un Adolescente")
elif(edad_persona >= 18 and edad_persona <=30):
    print("USted es un Adulto joven")
elif(edad_persona >= 30):
    print("Usted es un Adulto")
else:
    pass


# # 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# # (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# # pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# # pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# # de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# # como una lista o un string.
password = input("Ingrese una contraseña, debe tener entre 8 y 14 caracteres: ")
if(len(password) >= 8 and len(password) <= 14):
    print("Ha ingresado una contraseña correcta!")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# # 6) Escribir un programa que tome la lista
# # numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# # hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
media = median(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if( media > mediana and mediana > moda):
    print("Hay sesgo positivo")
elif( moda > mediana and mediana > media):
    print("Hay sesgo negativo")
elif(moda == mediana and mediana == media):
    print("No hay sesgo")
else:
    pass


# # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# # termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# # pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# # pantalla.
palabra = input("Ingrese una palabra o una frase por favor: ")
ultima_letra = palabra[-1].lower()
if(ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u"):
    print(f'{palabra}!')
else:
    print(palabra)


# # 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# # dependiendo de la opción que desee:
# # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# # El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# # usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# # lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input('Por favor ingrese su nombre: ')
opcion = int(input("""
Ingrese un numero entre 1,2 y 3 para seleccionar la opcion:\n
- 1 Si quiere su nombre en mayúsculas.\n
- 2 Si quiere su nombre en minúsculas.\n
- 3 Si quiere su nombre con la primer letra mayúscula
  """))
if(opcion == 1):
    print(nombre.upper())
elif(opcion == 2):
    print(nombre.lower())
elif(opcion == 3):
    print(nombre.title())
else:
#     pass


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# # ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

 magnitud = int(input("Por favor ingrese la magnitud del terremoto: "))

if(magnitud < 3):
    print(f'Muy leve (imperceptible)')
elif(magnitud == 3):
    print(f'Leve (ligeramente perceptible)')
elif( magnitud == 4):
    print(f'Moderado (sentido por personas, pero generalmente no causa daños)')
elif( magnitud == 5):
    print(f'Fuerte (puede causar daños en estructuras débiles)')
elif(magnitud == 6):
    print(f'Muy Fuerte (puede causar daños significativos)')
else:
    print(f'Extremo (puede causar  graves daños a gran escala)')


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentr (N/S), que mes del año es y que dia es. El programa deberá utilizar esa informacion para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("Ingrese el hemisferio donde se encuentra (N/S): ")
hemisferio = hemisferio.lower()

mes = int(input("Por favor ingrese el mes del año en números: "))
dia = int(input("Por favor ingrese el dia del mes en números: "))

if hemisferio == 's':
    if(mes == 12 and dia >= 21 ) or (mes in (1,2)) or (mes == 3 and dia <= 20) :
        print("Verano")
    elif (mes == 4 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 7 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("Primavera")
elif hemisferio == 'n':
    if(mes == 12 and dia >= 21 ) or (mes in (1,2)) or (mes == 3 and dia <= 20) :
        print("Invierno")
    elif (mes == 4 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 7 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("Otoño")