import matplotlib.pyplot as plt

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x = x0
    aproximaciones = [x0]

    for _ in range(max_iter):
        x_new = g(x)
        aproximaciones.append(x_new)

        if abs(x_new - x) < tol:
            break

        x = x_new

    plt.plot(aproximaciones, marker='o')
    plt.title("Convergencia - Punto Fijo")
    plt.xlabel("Iteración")
    plt.ylabel("Aproximación")
    plt.grid()
    plt.show()

    return aproximaciones[-1]
