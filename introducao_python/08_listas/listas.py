# Listas em Python
# Listas são coleções de dados que podem ser mutáveis, ou seja, podem ser alteradas
# Apresentam um índice, ou seja, podem ser acessadas por meio de um

# ìndice    0         1         2         3          4
nomes= ['douglas', 'camila', 'maria', 'damares', 'vitor']

print(type(nomes))
print(nomes)
print(nomes[0])

print('===============================================================')

# a função len me retorna o tamanho da minha lista ou do meu iterável
print(len(nomes))

# Método append adiciona um elemento no final da lista
nomes.append('iago')

# print(nomes)

# print('===============================================================')
# O método insert adiciona um elemento na posição que eu quiser
nomes.insert(1, 'Camila Soares')
# print(nomes)

# print('===============================================================')
# O método pop remove um elemento do final da lista se não informar qual posição deseja remover
nomes.pop()
# print(nomes)
# O método pop também pode remover um elemento da lista especificando a posição
nomes.pop(2)
# print(nomes)

print('===============================================================')
# O método remove remove um elemento da lista especificando o valor
# O remove remove apenas o primeiro valor encontrado na lista.
nomes.remove('maria')
print(nomes)
print('===============================================================')
# o método index me retorna a posição do elemento que eu quiser
# o método index retorna apenas o primeiro valor encontrado
print(nomes.index('damares'))