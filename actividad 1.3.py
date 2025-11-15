def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f
def a(n):
    resultado = factorial(n)/factorial(n-1)
    return resultado
b = a(6)
print(b)