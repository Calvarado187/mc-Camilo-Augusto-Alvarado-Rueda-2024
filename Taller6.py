import math

def calcular_coseno_aproximado(x, epsilon_s):
    resultado_aproximado = 1.0
    termino_actual = 1.0
    n = 2
    iteraciones = 0

    while abs(termino_actual) >= epsilon_s:
        termino_actual = (-1) ** (n // 2) * (x ** n) / math.factorial(n)
        resultado_aproximado += termino_actual
        n += 2
        iteraciones += 1

    error_aproximado = abs(termino_actual / resultado_aproximado) * 100

    return resultado_aproximado, error_aproximado, iteraciones

def main():
    x = float(input("Ingrese el valor en radianes: "))
    epsilon_s = float(input("Ingrese el criterio de error esperado (εs): "))

    resultado, error, iteraciones = calcular_coseno_aproximado(x, epsilon_s)

    print("\nResultado estimado:", resultado)
    print("Error aproximado relativo porcentual:", error, "%")
    print("Número de iteraciones realizadas:", iteraciones)

if __name__ == "__main__":
    main()
