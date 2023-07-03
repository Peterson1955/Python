numero = int(input(" Entre com numero inteiro positivo:  "))
fatorial = 1
if numero < 0:
    print(" Fatorial não existe!")
elif numero == 0:
    print(" Fatorial de 0 é igual a 1")
else:
    for i in range(1, numero+1):
        fatorial = fatorial * i
    print(f"Fatorial de {numero} é igual a  {fatorial}.")


