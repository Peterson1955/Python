def fatorial(n):
   return ( n * fatorial(n-1)) if n > 1 else 1

print(fatorial(5))
print(fatorial(10))


