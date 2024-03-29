# -*- coding: utf-8 -*-
"""Taller1_Camilo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H9HhYttCsz6UAXLF3_JQACUbYxCyRvL8
"""

Conjunto_A = int(input("Número de elementos del conjunto A: "))

A = set()
for i in range(Conjunto_A):
    elemento = float(input("Elemento " + str(i + 1) + ": "))
    A.add(elemento)

print("A =", A)

Conjunto_B = int(input("Número de elementos del conjunto B: "))

B = set()
for i in range(Conjunto_B):
    elemento_2 = float(input("Elemento " + str(i + 1) + ": "))
    B.add(elemento_2)

print("B =", B)
print("1 = Unión")
print("2 = Intersección")
print("3 = Diferencia")
print("4 = Diferencia Simétrica")

operacion = int(input("¿Qué operación desea realizar? "))

if operacion == 1:
    union = A | B
    print("Unión:", union)
    print("Cardinalidad:", len(union))
elif operacion == 2:
    interseccion = A & B
    print("Intersección:", interseccion)
    print("Cardinalidad:", len(interseccion))
elif operacion == 3:
    diferencia = A - B
    print("Diferencia:", diferencia)
    print("Cardinalidad:", len(diferencia))
elif operacion == 4:
    diferencia_simetrica = A ^ B
    print("Diferencia Simétrica:", diferencia_simetrica)
    print("Cardinalidad:", len(diferencia_simetrica))
else:
    print("Operación no válida.")