#receba um número do usuário e mostre a tabuada desse número.

num = int(input('Digite um número inteiro: '))
i = 1

while i <= 10:
    print(f'{num} x {i} = {num * i}')
    i += 1