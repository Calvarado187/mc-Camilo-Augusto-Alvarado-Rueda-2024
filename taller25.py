import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Datos de los puntos (x, f(x))
x = np.array([1, 2, 3, 4, 5, 6, 7])
fx = np.array([1, 5, 4, 4, -2, 2, 9])

# Punto donde se desea estimar f(x)
x_estimate = 3.55

# Polinomio de interpolación de Lagrange
lagrange_poly = lagrange(x, fx)

# Trazadores cúbicos
cubic_spline = CubicSpline(x, fx)

# Estimación de f(3.55) usando el polinomio de interpolación de Lagrange
fx_estimate_lagrange = lagrange_poly(x_estimate)

# Estimación de f(3.55) usando trazadores cúbicos
fx_estimate_cubic_spline = cubic_spline(x_estimate)

# Puntos para graficar
x_values = np.linspace(min(x), max(x), 100)
lagrange_values = lagrange_poly(x_values)
cubic_spline_values = cubic_spline(x_values)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, fx, 'ro', label='Datos')
plt.plot(x_values, lagrange_values, label='Interpolación de Lagrange')
plt.plot(x_values, cubic_spline_values, label='Trazadores Cúbicos')
plt.axvline(x=x_estimate, color='g', linestyle='--', label='Estimación (x=3.55)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Lagrange vs Trazadores Cúbicos')
plt.legend()
plt.grid(True)
plt.show()

print("Polinomio de Interpolación de Lagrange:")
print("Coeficientes del polinomio:", lagrange_poly.coefficients)
print("Estimación de f(3.55):", fx_estimate_lagrange)

print("\nTrazadores Cúbicos:")
print("Coeficientes de los trazadores cúbicos:", cubic_spline.c)
print("Estimación de f(3.55):", fx_estimate_cubic_spline)
