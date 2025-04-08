class Mamifero:
    def __init__(self, pelo, mamas, idade):
        self.pelo = pelo
        self.mamas = mamas
        self.idade = idade
    def comunicar(self):
        pass

class Cachorro(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo):
        Mamifero.__init__(pelo, mamas, idade)
        self.rabo = rabo
    def latir(self):
        pass
class Gato(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo):
        super.__init__(pelo, mamas, idade):
        self.__rabo = rabo
    def miar(self):
        pass

