# valida dos dados
from dao import PessoaDao
from model import Pessoa

class PessoaController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and (idade > 0 and idade < 200) and len(cpf) == 11:
            try:
                PessoaDao.salvar(Pessoa(nome, idade, cpf))
                return True
            except:
                return False
        else:
            return False
        
PessoaController.cadastrar('Douglas', 32, '22222222222')