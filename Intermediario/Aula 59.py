try:
    num = int(input('informe um numero:  '))
except:
    print("Valor incorreto!")
else:
    print(f"Voce digitou  {num} ")
finally:
    print("Fim da execução do programa!!")


