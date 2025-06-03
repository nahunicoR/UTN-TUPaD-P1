# 1) Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Melón = 2800

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

nombres_frutas = []
for fruta in precios_frutas.keys():
    nombres_frutas.append(fruta)

print(nombres_frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre_contacto = input("Ingrese el nombre de su contacto: ")
    tel_contacto = input("Ingrese el número telefónico de su contacto: ")
    contactos[nombre_contacto] = tel_contacto

consulta_nombre = input("Ingrese el nombre del contacto que desee encontrar: ")
if consulta_nombre in contactos.keys():
    print(contactos[consulta_nombre])
else: 
    print('Nombre no encontrado.')


# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input('Ingrese una frase por favor: ')
palabras_unicas = set(frase)
recuento = {}

for palabra in frase:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(palabras_unicas)
print(recuento)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}
notas = []
for i in range(3):
    nombre_alumno = input('Ingrese el nombre del alumno: ')
    for j in range(3):
        nota = int(input('Ingrese la nota por favor: '))
        notas.append(nota)
    
    alumnos[nombre_alumno] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f'{nombre}: {promedio:.2f}')