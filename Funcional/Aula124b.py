def notas_musicais():
    yield 'DO'
    yield 'RE'
    yield 'MI'
    yield 'FA'
    yield 'SOL'
    yield 'LA'
    yield 'SI'



gen = notas_musicais()
print(gen)


print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

