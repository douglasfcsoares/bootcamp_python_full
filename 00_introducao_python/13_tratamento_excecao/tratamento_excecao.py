# Tratamento de exceção

# n1 = int(input('digite um número: '))
# n2 = int(input('digite um número: '))

# try:
#     print(n1 / n2)
# except:
#     print('Não foi possível')
# finally: # Finally sempre será executado.
#     print('Finalizado!')

# tratando exceções específicas
# try:
#     x = int(input('Digite um número: '))
#     print(5/x)
# except ValueError:
#     print('Digite um número inteiro:')
# except ZeroDivisionError:
#     print('Não digite zero 0')

# Capturando a exceção que ocorreu
try:
    x = int(input('Digite um número: '))
    print(5/x)
except Exception as e:
    print(e)
