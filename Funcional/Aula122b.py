frase = 'pyPRO seja um profissional Python'
numeros = [1, 2, 3, 4, 5, 6, 7]

def meu_loop(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            break

meu_loop(frase)
meu_loop(numeros)

