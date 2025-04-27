class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente

class Vendedor(Pessoa):
    def __init__(self, id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor

c1 = Cliente(2, 'Douglas Soares', '44444444444')
v1 = Vendedor(1, 'Camila Soares', '222222222')

print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)
print('==================================')

print(v1.id_vendedor)
print(v1.nome)
print(v1.cpf)
