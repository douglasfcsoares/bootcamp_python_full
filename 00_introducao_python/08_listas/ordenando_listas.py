nomes= ['douglas', 'camila', 'maria', 'damares', 'vitor']
# o método sort realiza a ordenação da lista, seja ela por ordem alfabética ou numérica
nomes.sort()
print(nomes)

num = [5,8,3,0,2,3,1,6,3,7]
# num.sort()
print(num)

# o método reverse inverte a ordem da lista
# num.sort(reverse=True)
# print('Reverse ')
# print(num)

# o método sort altera a lista original, para boas práticas é recomendado criar uma cópia da lista antes de ordenar
# ou usar a unção sorted que retorna uma nova lista ordenada

num_ordenados = sorted(num)
print('Nova variável com a lista ordenada sem alterar a original')
print(num_ordenados)
print('aqui exibimos a lista original')
print(num)

print('a função sorted também pode receber o parâmetro reverse')
num_ordenados = sorted(num, reverse=True)
print(num_ordenados)

