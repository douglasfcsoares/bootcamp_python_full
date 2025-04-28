from model import Pessoa

class PessoaDao:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + ' ' + str(pessoa.idade) + ' ' + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = 'Douglas'
        idade = 32
        cpf = '1231234321413413'
        return Pessoa(nome, idade, cpf)
    
# p1 = Pessoa('Douglas Soares', 32, '5555555555')
# PessoaDao.salvar(p1)
# print(PessoaDao.ler().nome)