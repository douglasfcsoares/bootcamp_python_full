# list comprehension

x = [i for i in range(0, 10)]
print(x)

# Matriz em list comprehension

y = [[[h for h in range(0,3)] for y in range(0,3)] for i in range(0, 3)]
print(y)

# condições em list comprehension

z = [i for i in range(0, 10) if i > 4]
print(z)