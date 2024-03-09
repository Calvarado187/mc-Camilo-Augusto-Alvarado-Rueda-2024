import math

def calcular_seno_aproximado(x, es):
    x = x % (2 * math.pi)  
    seno_aproximado = 0.0
    termino_actual = x
    iteraciones = 0
    ea = float('inf')  

    while abs(ea) > es:
        seno_aproximado += termino_actual
        iteraciones += 1

        
        termino_actual = (-1) * termino_actual * x**2 / ((2 * iteraciones + 1) * (2 * iteraciones))

        
        ea = termino_actual / seno_aproximado * 100

    return seno_aproximado, ea, iteraciones


x = float(input("Ingrese el valor en radianes: "))
es = float(input("Ingrese el criterio de error esperado (en porcentaje): "))


es /= 100.0


resultado, error_rel_porcentual, num_iteraciones = calcular_seno_aproximado(x, es)


print(f"\nResultado estimado del seno({x}): {resultado:.8f}")
print(f"Error aproximado relativo porcentual: {error_rel_porcentual:.8f}%")
print(f"Número de iteraciones realizadas: {num_iteraciones}")

