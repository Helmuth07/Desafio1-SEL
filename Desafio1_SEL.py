import numpy as np

# Definir la matriz de coeficientes (porcentajes de arena, grano fino y grano grueso)
A = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])

# Definir el vector de requerimientos
b = np.array([4800, 5210, 5690])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)

# Mostrar los resultados
print("Las cantidades de metros cúbicos que se deben transportar desde cada cantera son:")
print(f"Cantera 1: {x[0]:.2f} m³")
print(f"Cantera 2: {x[1]:.2f} m³")
print(f"Cantera 3: {x[2]:.2f} m³")
