# Conjuntos tipo set()

x = {1, 2, 3, 4, 5, 6}
y = {5, 6, 7, 8, 9, 10}

t = x.union(y)
print(type(x))
print(t)
x = x.difference(y)
print(x)

x = x.intersection(y)
print(x)