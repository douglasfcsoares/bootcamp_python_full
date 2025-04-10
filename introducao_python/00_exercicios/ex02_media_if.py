# Receba 4 notas de um aluno e exiba se ele foi aprovado (média maior ou igual a 6)
# Se ele ficou de recuperação (média maior ou igual a 4)
# Ou se ele foi reprovado (média menor que 4)



while True:
    nota1 = input('Digite a primeira nota: ')
    nota2 = input('Digite a segunda nota: ')
    nota3 = input('Digite a terceira nota: ')
    nota4 = input('Digite a quarta nota: ')
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        nota4 = float(nota4)
        break

    except ValueError:
        print('Nota digitada inválida. Por favor, digite um número.')

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'O aluno foi aprovado com a média {media:.2f}')
elif media >= 4:
    print(f'O aluno ficou de recuperação com a média {media:.2f}')
else:
    print(f'O aluno foi reprovado com a média {media:.2f}')