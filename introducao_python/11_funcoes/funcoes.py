# Funções
def minha_funcao():
    print('Hello World!!!')
minha_funcao()

# Funções com parâmetros de entrada.
def soma_numeros(n1, n2):
    print(n1 + n2)

soma_numeros(2, 3)
# Parâmetros nomeados
soma_numeros(n2 = 2, n1 = 5)
# Parâmetros *args retorna uma tupla com os parâmetros
def soma(*args):
    print(args)

soma(1, 2, 3, 4, 5, 6)

# Parâmetros **kwargs retorna um dicionário com os parâmetros
def soma2(**kwargs):
    # print(kwargs)
    x = kwargs.get('t5')
    if x:
        print('Argumento passado.')
    else:
        print('Argumento não foi passado.')

soma2(t1 = 1, t2 = 2, t3 = 3, t4 = 4, t5 = 5)

# retorno de funções

def soma3(n1, n2):
    return n1 + n2

y = soma3(2, 3)

print(f'O valor retornado da função foi = {y}')