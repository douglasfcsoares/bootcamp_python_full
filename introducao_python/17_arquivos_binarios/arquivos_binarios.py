import pickle

x = [1,2,3,4]
# x = {'nome' : 'Douglas', 'idade': 32}

# string = pickle.dumps(x)
# print(string)
# print(type(pickle.loads(string)))
arq = open('arquivo.pkl', 'wb')
pickle.dump(x, arq)

arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)

print(retornou)