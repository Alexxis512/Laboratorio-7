def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f
def combinacion(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

resultado = combinacion(5, 4)
print(resultado)