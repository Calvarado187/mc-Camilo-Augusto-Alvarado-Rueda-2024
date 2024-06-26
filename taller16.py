# -*- coding: utf-8 -*-
"""Taller16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10dKJVMIxFNED3rHRAiThWuxA4y2Wx4i1
"""

def gauss_jordan_inversa(matriz):
    n = len(matriz)


    identidad = [[0] * n for _ in range(n)]
    for i in range(n):
        identidad[i][i] = 1


    for i in range(n):
        fila = matriz[i]
        for j in range(n):
            fila.append(identidad[i][j])


    for i in range(n):
        divisor = matriz[i][i]
        for j in range(n*2):
            matriz[i][j] /= divisor
        for k in range(n):
            if i != k:
                factor = matriz[k][i]
                for j in range(n*2):
                    matriz[k][j] -= factor * matriz[i][j]


    inversa = []
    for i in range(n):
        fila_inversa = []
        for j in range(n, n*2):
            fila_inversa.append(matriz[i][j])
        inversa.append(fila_inversa)

    return inversa


matriz_A = [
    [3, 2, 2],
    [3, 1, -3],
    [1, 0, -2]
]


matriz_B = [
    [1, 2, 0, 4],
    [2, 0, -1, -2],
    [1, 1, -1, 0],
    [0, 4, 1, 0]
]

inversa_A = gauss_jordan_inversa(matriz_A)
inversa_B = gauss_jordan_inversa(matriz_B)


print("Inversa de A:")
for fila in inversa_A:
    print(fila)

print("\nInversa de B:")
for fila in inversa_B:
    print(fila)