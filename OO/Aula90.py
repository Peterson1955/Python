class Automovel:
    def __init__(self,placa):
        self.placa = placa
    def get_placa(self):
        return self.placa
    def dirigir(self, velocidade):
        print(f"Estou dirigindo a {velocidade} km/h")

meu_carro = Automovel("FHI-3472")

print(meu_carro.get_placa())
meu_carro.dirigir(100)

