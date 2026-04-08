import matplotlib.pyplot as plt

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    aproximaciones = [x0, x1]

    for _ in range(max_iter):
        if f(x1) - f(x0) == 0:
            raise ValueError("División por cero")

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        aproximaciones.append(x2)

        if abs(x2 - x1) < tol:
            break

        x0, x1 = x1, x2

    plt.plot(aproximaciones, marker='o')
    plt.title("Convergencia - Secante")
    plt.xlabel("Iteración")
    plt.ylabel("Aproximación")
    plt.grid()
    plt.show()

    return aproximaciones[-1]
