x = 2
y = x
y = 3
print(f'x = {x}')
print(f'y = {y}')

a = [1,2,3]
b = a
c = a.copy()

print('Perceba que a e b tem o mesmo endereço de memória')
print(hex(id(a)))
print(hex(id(b)))
print('enquanto c aponta para um endereço de memória diferente')
print(hex(id(c)))