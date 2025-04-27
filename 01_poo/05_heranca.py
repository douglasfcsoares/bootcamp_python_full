class Pessoa:
    def falar(self):
        print('Falando')
    def andar(self):
        print('andando')

# ao passarmos a classe Pessoa para a classe Cliente ela HERDA, todos os atributos e métodos da classe Pessoa.
class Cliente(Pessoa):
    def comprar(self):
        print('Comprando')

class Vendedor(Pessoa):
    def vender(self):
        print('Vendendo')

c1 = Cliente()
v1 = Vendedor()

# aqui verificamos que a instância de um cliente recebeu como herança os métodos e atributos da classe Pessoa.
c1.falar()
c1.andar()
c1.comprar()

v1.falar()
v1.andar()
v1.vender()
