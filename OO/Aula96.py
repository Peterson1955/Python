class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"
    def indentificador(self):
        return self.__cpf


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, codigo):
        super().__init__(nome, sobrenome, cpf)
        self.__codigo = codigo

    def indentificacao(self):
        return self.__codigo


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def identificacao(self):
        return self.__matricula

cliente1 = Cliente('Jose', 'Silva', '123.567.789-00', 'xxxx-09')
funcionario1 = Funcionario('Pedro', 'Bernardes', '000.000.123-09', '786-09')

print(cliente1.nome_completo())
print(cliente1.indentificacao())
print("_________________________________")
print(funcionario1.nome_completo())
print(funcionario1.identificacao())




