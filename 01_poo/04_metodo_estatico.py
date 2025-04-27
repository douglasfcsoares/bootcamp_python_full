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
    
    @staticmethod
    def e_adulto(idade):
        if idade > 18:
            return True
        return False