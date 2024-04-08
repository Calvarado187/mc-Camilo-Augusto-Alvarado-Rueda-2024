import math

def serie_taylor(x, n):
    resultado = 0
    for i in range(n+1):
        resultado += ((-1)**i) * (x - 0.5)**i / math.factorial(i)
    return resultado

def main():
    x = 0.505
    base_x = 0.5
    real_value = math.exp(-x)
    print("Valor real de la función en x = 0.505:", real_value)

    for n in range(16):
        estimacion = serie_taylor(x - base_x, n)
        error = abs((estimacion - real_value) / real_value) * 100
        print(f"Orden {n}: {estimacion: .8f} - Error Aproximado Relativo Porcentual= {error:.4f}%")

if __name__ == "__main__":
    main()
