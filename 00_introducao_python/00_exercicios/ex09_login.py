# Defina um usuário e senha e depois verifique se login e senha á válido

USUARIO = 'douglas'
SENHA = '123'

while True:
    user_login = input('usuário: ')
    pass_login = input('senha: ')

    if user_login == USUARIO and pass_login == SENHA:
        print('Login válido')
        break
    else:
        print('Login inválido') 