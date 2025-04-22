# Dicionários
#formas de se criar um dicionário em python
# podemos criar usando dict()
x = dict(
    nome = 'Douglas com dict()',
    idade = 32
)
# ou abrindo e fechado chaves
y = {
    'nome' : 'Douglas com {}',
    'idade' : 32
}
# print(x)
# print(y)

pessoas = [
    {'nome' : 'Douglas', 'idade' : 32, 'altura': 178 },
    {'nome' : 'Camila', 'idade' : 35, 'altura': 158 },
    {'nome' : 'Vitor', 'idade' : 17, 'altura': 172 }
    ]

for pessoa in pessoas:
    # print(type(pessoa))
    print(pessoa['nome'])

# como adicionar novas chaves a um dicionário pré definido ou vazio com update
y.update({'altura': 178})
print(y)

# iteração de um dicionário
# iteração por valor
print(y.values())
# iteração por chaves
print(y.keys())
# iteração por chave e valor
print(y.items())

for i, j in y.items():
    print(f'chave = {i}, valor = {j}')
