# Receba um número e exiba se ele é positivo ou negativo.

n1 = float(input('Digite um número: '))
if n1 > 0:
    print(f'O número {n1} é positivo.')
elif n1 < 0:
    print(f'o número {n1} é negativo.')
else:
    print(f'o número é {n1} é neutro.')  # ou zero.  # ou igual a zero.