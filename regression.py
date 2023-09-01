import numpy as np

def calcular_regresion_lineal(pares_de_puntos):
    x = np.array([p[0] for p in pares_de_puntos])
    y = np.array([p[1] for p in pares_de_puntos])
    n = len(pares_de_puntos)

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x**2)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - m * sum_x) / n

    return m, b

def main():
    try:
        N = int(input("Ingrese el número de pares de puntos (N): "))
        pares_de_puntos = []
        for i in range(N):
            x, y = map(float, input(f"Ingrese el par de puntos {i + 1} (x, y): ").split())
            pares_de_puntos.append((x, y))

        m, b = calcular_regresion_lineal(pares_de_puntos)
        print(f"La pendiente (m) de la regresión lineal es: {m}")
        print(f"El intercepto (b) de la regresión lineal es: {b}")

    except ValueError:
        print("Error: Asegúrate de ingresar números válidos.")

if __name__ == "__main__":
    main()