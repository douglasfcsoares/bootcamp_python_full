class Pessoas:
    # Atributos de classe ficam fora dos métodos e não precisam de inicialização de uma instância
    possui_olho = True
    possui_boca = True
    raca = 'ser humaninho'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def fala(self):
        print('está falando... ')

    # Método de classe, são métodos que não precisam de uma instância para ser chamado.
    # para identificarmos métodos de classe usamos o decorador @classmethod.
    @classmethod
    def andar(cls):
        # o atributo cls faz que o método de classe receba o estado da classe e pode criar novos atributos de classe
        # como o exemplo abaixo
        cls.pernas = 2
        # o atributo cls também pode alterar atributos da classe
        cls.possui_boca = False
        return None

# print(Pessoas.raca)

# Ao atribuirmos novos valores sem definir a estância os valores dos atributos da classe é alterado para todas as instâncias.
Pessoas.raca = 'ser humano'

p1 = Pessoas('Douglas Soares', 32)
p2 = Pessoas('Camila', 36)

# print(p1.raca)
# print(p2.raca)
print(Pessoas.possui_boca)
Pessoas.andar()
print(Pessoas.possui_boca)
print(Pessoas.pernas)

