from sys import getsizeof
def fibonacci(final):
    f = []
    a, b = 0, 1
    while len(f) < final:
        f.append(b)
        a, b = b, a + b
    return f

def fibonacci_g(final):
    a, b, contador = 0, 1, 0
    while contador < final:
        a, b, = b, a + b
        yield a
        contador += 1

gen = fibonacci_g(10000)
lis = fibonacci(10000)

print(f'Gen = {getsizeof(gen)}')
print(f'Lis = {getsizeof(lis)}')



