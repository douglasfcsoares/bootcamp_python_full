class Pessoas:
    # o método __init__ é o quê permite receber os parâmetros para a minha classe
    def __init__(self, nome, idade, sexo):
        print(f'olá {nome} | {idade} | {sexo}')
    def logar_sistema(self):
        print('estou logando no sistema ')

# sempre que faço uma nova instância da minha classe o método init é chamado!
p1 = Pessoas('Douglas Soares', 32, 'M')
p2 = Pessoas('Camila Soares', 36, 'F')

# p1.logar_sistema()