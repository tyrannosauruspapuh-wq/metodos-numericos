import matplotlib.pyplot as plt

def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Intervalo inválido")

    aproximaciones = []

    for _ in range(max_iter):
        m = b - f(b) * (b - a) / (f(b) - f(a))
        aproximaciones.append(m)

        if abs(f(m)) < tol:
            break

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    plt.plot(aproximaciones, marker='o')
    plt.title("Convergencia - Falsa Posición")
    plt.xlabel("Iteración")
    plt.ylabel("Aproximación")
    plt.grid()
    plt.show()

    return aproximaciones[-1]
