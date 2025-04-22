# Laço de repetição While (Enquanto)
num = 0
while num < 20:
    if num % 2 == 0:
        print(f'{num} o número é par')
        num += 1
        continue
    if num == 15:
        print('Saindo do laço')
        break
    num += 1