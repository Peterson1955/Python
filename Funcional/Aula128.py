def seja_esducado(funcao):
    def sendo():
        print ('Olá....')
        funcao()
        print ('Tenha um bom dia!')
    return sendo

def saudacao():
    print ('Seja bem vindo!')

# saudacao()
saudacao_melhorada = seja_esducado(saudacao)
saudacao_melhorada()

