def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f
def combinacion(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

resultado = combinacion(10, 3)
print(resultado)