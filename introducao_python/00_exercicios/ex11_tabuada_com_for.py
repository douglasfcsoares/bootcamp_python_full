# Receba um número e mostre a tabuada completa dele usando o laço for.

num = int(input("Digite um número: "))

for i in  range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("Fim da tabuada")