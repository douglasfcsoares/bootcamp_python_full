# Receba M para Masculino e F para Feminino.

sexo = input('Digite F para Feminino ou M para Masculino: ').lower()

if sexo == 'm':
    print(f' {sexo} é Masculino')
elif sexo == 'f':
    print(f' {sexo} é Feminino')
else:
    print(f' {sexo} é Sexo inválido')  # Caso o usuário digite algo diferente de 