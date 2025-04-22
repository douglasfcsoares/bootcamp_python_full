# modelagem da classe de uma pessoa

class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.nome} está logando no sistema ')

p1 = Pessoas('Douglas Soares', 32, '12345678900')
p2 = Pessoas('Camila Soares', 32, '12345678900')

p1.logar_sistema()
p2.logar_sistema()