# Escreva um programa que receba notas de um aluno (0 - 10), caso a nota digitada
# Esteja fora desse intervalo, peça ao professor para digitar a nota novamente.

nota = 0

while True:
    nota = float(input('Digite a nota do aluno: '))
    while nota >= 0 and nota <= 10:
        print(f'a nota salva com sucesso {nota}')
        break
    print('Nota inválida, por favor digite novamente')