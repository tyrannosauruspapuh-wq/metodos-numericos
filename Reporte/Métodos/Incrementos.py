import matplotlib.pyplot as plt

def incrementos(f, x0, h=0.1, max_iter=1000):
    x_vals = [x0]
    x1 = x0

    for _ in range(max_iter):
        x2 = x1 + h
        x_vals.append(x2)

        if f(x1) * f(x2) < 0:
            break

        x1 = x2

    plt.plot(x_vals, marker='o')
    plt.title("Búsqueda por Incrementos")
    plt.xlabel("Iteración")
    plt.ylabel("x")
    plt.grid()
    plt.show()

    return x1, x2
