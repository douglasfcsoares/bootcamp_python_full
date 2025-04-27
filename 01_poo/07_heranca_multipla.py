class Animal:
    def andar(self):
        print('Animal andando')

class Felino(Animal):
    def felino(self):
        print('Felino')

class Canino():
    def canino(self):
        print('Canino')

# a classe gato recebe como Herança a classe Felino que recebe como Herança a classe Animal
# fazendo com que a classe Gato receba múltipla herança de Felino e Animal
class Gato(Felino):
    def miar(self):
        print('Gato miando')

class Cachorro(Canino, Animal):
    def latir(self):
        print('Latindo como cachorro')

g1 = Gato()
c1 = Cachorro()

g1.miar()
g1.felino()
g1.andar()

print('=============================')
c1.latir()
c1.canino()
c1.andar()