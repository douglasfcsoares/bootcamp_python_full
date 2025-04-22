# Armazenamento persistente dos dados
# arquivo = open('pessoas.txt', 'a')
# arquivo = open('pessoas.txt', 'r')

# i = 0
# while True:
#     if i > 2:
#         break
#     arquivo.write(input('Digite um nome: ') + ' ' + input('Digite a idade: ') + '\n')
#     i += 1

# resultados = arquivo.readlines()
# x = []
# for i in resultados:
#     x.append(i.split())
# print(x[1][0])
# arquivo.close()

# Usando o construtor with, onde ao sair do contexto do with ele automaticamente fecha o nosso arquivo:

with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)

print('Fora do contexto do with, arquivo fechado!')