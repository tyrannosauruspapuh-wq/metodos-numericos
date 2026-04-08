import matplotlib.pyplot as plt

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Intervalo inválido")

    aproximaciones = []

    for _ in range(max_iter):
        m = (a + b) / 2
        aproximaciones.append(m)

        if abs(f(m)) < tol:
            break

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    # Gráfica
    plt.plot(aproximaciones, marker='o')
    plt.title("Convergencia - Método de Bisección")
    plt.xlabel("Iteración")
    plt.ylabel("Aproximación")
    plt.grid()
    plt.show()

    return aproximaciones[-1]
