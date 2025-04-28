# interface, recebe da controller a resposta dos dados.
from controller import PessoaController

while True:
    decisao = int(input('Digite 1 pra salvar, 2 para ver e 3 pra sair '))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('nome = ')
        idade = int(input('idade = '))
        cpf = input('cpf = ')
        if PessoaController.cadastrar(nome, idade, cpf):
            print('cadastrado com sucesso')
        else:
            print('Falha')