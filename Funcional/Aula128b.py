def seja_educado(funcao):
    def sendo():
        print ('Olá....')
        funcao()
        print ('Tenha um bom dia!')
    return sendo

@seja_educado
def saudacao():
    print ('Seja bem vindo!')


saudacao()

