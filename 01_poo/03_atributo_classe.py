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

print(Pessoas.raca)

# Ao atribuirmos novos valores sem definir a estância os valores dos atributos da classe é alterado para todas as instâncias.
Pessoas.raca = 'ser humano'

p1 = Pessoas('Douglas Soares', 32)
p2 = Pessoas('Camila', 36)

print(p1.raca)
print(p2.raca)

