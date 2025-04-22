# Receba uma temperatura em Farenheite exiba em graus celsius.
# Formula c= 5 * f -32/9

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 * ((fahrenheit - 32) / 9)
    return celsius


fahrenheit = float(input("Digite a temperatura em Farenheite: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Farenheite é igual a {celsius} Celsius")
print(f"{fahrenheit} Farenheite é igual a {celsius:.3f}")
