# Exercícios:
# Faça um programa que leia duas notas e imprima a média delas

while True:
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        break
    except ValueError:
        print("Nota inválida. Por favor, digite uma nota válida.")
media = (nota1 + nota2) / 2
print(f"A média das notas é {media:.2}")
