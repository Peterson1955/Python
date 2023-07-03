altura = float(input("Entre com Altura:  "))
sexo = input("Qual seu Sexo  <F ou M>: ")

if (sexo == "M"):
   peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print(peso, "Este é seu peso ideal!")
