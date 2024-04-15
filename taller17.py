# -*- coding: utf-8 -*-
"""Taller17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PA84cFfvTMVKwwfO3zXnCnrrzHSnpgTU
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([9, 7, 8, 5, 6, 4.5, 4, 2, 5])


A = np.vstack([x, np.ones(len(x))]).T
m, b = np.linalg.lstsq(A, y, rcond=None)[0]


plt.scatter(x, y, label='Datos')
plt.plot(x, m*x + b, 'r', label='Línea de regresión')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal por Mínimos Cuadrados')
plt.legend()
plt.grid(True)
plt.show()


print(f"Ecuación de la línea de regresión: y = {m:.2f}x + {b:.2f}")