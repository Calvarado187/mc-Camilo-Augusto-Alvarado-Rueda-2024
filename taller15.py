def gauss_jordan(matrix):
    n = len(matrix)

    for i in range(n):
        # Pivoteo parcial
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Verificar si el pivote es cero
        if matrix[i][i] == 0:
            return None  # El sistema tiene infinitas soluciones o no tiene solución única

        # Normalización del pivote
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        # Eliminación hacia adelante y hacia atrás
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    # Obtener las soluciones
    solutions = [row[-1] for row in matrix]
    return solutions


# Sistema de ecuaciones
system = [
    [2, 0, 2, 10],
    [3, 4, 3, 23],
    [4, 1, 0, 30]
]

solutions = gauss_jordan(system)
if solutions is None:
    print("El sistema tiene infinitas soluciones o no tiene solución única.")
else:
    print("Las soluciones son:")
    for i, solution in enumerate(solutions):
        print(f"x{i + 1} =", solution)
