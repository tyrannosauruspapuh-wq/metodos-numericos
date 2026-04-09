import time
import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# Función del ejercicio
# ---------------------------------------------------------
def f(x):
    return -0.4*x**2 + 2.3*x + 2.2

def df(x):
    return -0.8*x + 2.3

# Punto fijo: despeje estable
def g(x):
    return (0.4*x*x - 2.2) / 2.3


# ---------------------------------------------------------
# Métodos
# ---------------------------------------------------------

def biseccion(f, a, b, tol, max_iter=50):
    inicio = time.time()
    iteraciones = 0

    while iteraciones < max_iter:
        iteraciones += 1
        m = (a + b) / 2

        if abs(b - a) < tol:
            break

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    tiempo = time.time() - inicio
    return m, iteraciones, tiempo


def falsa_posicion(f, a, b, tol, max_iter=50):
    inicio = time.time()
    iteraciones = 0

    while iteraciones < max_iter:
        iteraciones += 1
        m = b - f(b) * (b - a) / (f(b) - f(a))

        if abs(f(m)) < tol:
            break

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    tiempo = time.time() - inicio
    return m, iteraciones, tiempo


def newton(f, df, x0, tol, max_iter=50):
    inicio = time.time()
    iteraciones = 0
    x = x0

    while iteraciones < max_iter:
        iteraciones += 1

        if df(x) == 0:
            raise ValueError("Derivada cero, cambia x0")

        x_new = x - f(x) / df(x)

        if abs(x_new - x) < tol:
            x = x_new
            break

        x = x_new

    tiempo = time.time() - inicio
    return x, iteraciones, tiempo


def secante(f, x0, x1, tol, max_iter=50):
    inicio = time.time()
    iteraciones = 0

    while iteraciones < max_iter:
        iteraciones += 1

        if f(x1) - f(x0) == 0:
            raise ValueError("División por cero en secante")

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        if abs(x2 - x1) < tol:
            x1 = x2
            break

        x0, x1 = x1, x2

    tiempo = time.time() - inicio
    return x1, iteraciones, tiempo


def punto_fijo(g, x0, tol, max_iter=50):
    inicio = time.time()
    iteraciones = 0
    x = x0

    while iteraciones < max_iter:
        iteraciones += 1
        x_new = g(x)

        if abs(x_new - x) < tol:
            x = x_new
            break

        x = x_new

    tiempo = time.time() - inicio
    return x, iteraciones, tiempo


# ---------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ---------------------------------------------------------

a, b = 5, 8
tol = 0.03
x0 = 0
x1 = 3

# Métodos
rb, ib, tb = biseccion(f, a, b, tol)
rf, iff, tf = falsa_posicion(f, a, b, tol)
rn, inn, tn = newton(f, df, x0, tol)
rs, iss, ts = secante(f, x0, x1, tol)
rp, ip, tp = punto_fijo(g, x0, tol)


# ---------------------------------------------------------
# RESULTADOS
# ---------------------------------------------------------

print("\nRESULTADOS DEL EJERCICIO\n")

print(f"Bisección:       raíz={rb:.6f}, iteraciones={ib}, tiempo={tb:.6f} s")
print(f"Falsa Posición:  raíz={rf:.6f}, iteraciones={iff}, tiempo={tf:.6f} s")
print(f"Newton-Raphson:  raíz={rn:.6f}, iteraciones={inn}, tiempo={tn:.6f} s")
print(f"Secante:         raíz={rs:.6f}, iteraciones={iss}, tiempo={ts:.6f} s")
print(f"Punto Fijo:      raíz={rp:.6f}, iteraciones={ip}, tiempo={tp:.6f} s")


# ---------------------------------------------------------
# GRÁFICA DE LA FUNCIÓN
# ---------------------------------------------------------

X = np.linspace(a, b, 200)
Y = [f(x) for x in X]

plt.plot(X, Y, label="f(x) = -0.4x² + 2.3x + 2.2")
plt.axhline(0, color='black', linewidth=1)
plt.title("Gráfica de la Función en [5,8]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()
