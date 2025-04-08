produtos = [('tv', 2500), ('fogão', 1240), ('radio', 234)]
# novo preco  = preco * 1.05

novo_preco = lambda produto: (produto[0], produto[1] * 1.05)

print(list(map(novo_preco, produtos)))
