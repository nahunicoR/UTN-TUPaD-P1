from math import pi
from collections import deque

# 1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


# 2) Siguiendo con el diccionario precios_frutas
# que resulta luego de ejecutar el código desarrollado en el punto anterior,
# actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1500
precios_frutas['Melón'] = 2800

# 3) Siguiendo con el diccionario precios_frutas
# que resulta luego de ejecutar el código desarrollado en el punto anterior,
# crear una lista que contenga únicamente las frutas sin los precios.
lista_frutas = []
for item in precios_frutas:
    lista_frutas.append(item)

print(lista_frutas)


# 4) Crear una clase llamada Persona
# que contenga un método __init__
# con los atributos nombre,
# pais y edad y el método saludar.
# El método saludar debe imprimir por pantalla
# un mensaje de salud que siga la estructura
# "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

persona = Persona('Nahuel', 'Argentina', 30)
persona.saludar()

# 5) Crear una clase llamada Circulo que contenga el atributo radio
# y los métodos calcular_area y calcular_perimetro. 
# Dichos métodos deben calcular el parámetro correspondiente.
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        resultado = round(pi * (self.radio **2), 2)
        print(resultado)

    def calcular_perimetro(self):
        resultado = round(pi * self.radio * self.radio, 2)
        print(resultado)

circulo = Circulo(5)
circulo.calcular_area()
circulo.calcular_perimetro()


# 6) Dado un string con paréntesis "()", "{}", "[]",
#  verifica si están correctamente balanceados usando una pila.
def str_balanceados(str):
    pila = []
    pares = {')': '(', '}':'{', ']': '['}

    for char in str:
        if char in '({[':
            pila.append(char)
        elif char in ')}]':
            if not pila:
                return False
            
            ultimo = pila.pop()

            if ultimo != pares[char]:
                return False
    return len(pila) == 0


# 7) Usa una cola para simular un sistema de turnos en un banco.
#  La cola debe permitir: ● Agregar clientes (encolar).
#  ● Atender clientes (desencolar).
#  ● Mostrar el siguiente cliente en la fila.

class Cola:

    def __init__(self):
        self.items = deque()

    def queue(self, val):
        return self.items.append(val)
    
    def dequeue(self):
        return self.items.pop()
    
    def show_next(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    

# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_inicio(self,valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end='->')
            actual = actual.siguiente
        print('None')

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        
        self.cabeza = anterior
