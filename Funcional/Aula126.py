# criar função fibonacci

def fibonacci(final):
    f = []
    a, b = 0, 1
    while len(f) < final:
        f.append(b)
        a, b = b, a + b
    return f

print(fibonacci(20))

def fibonacci_g(final):
    a, b, contador = 0, 1, 0
    while contador < final:
        a, b, = b, a + b
        yield a
        contador += 1

print(list(fibonacci_g(100)))