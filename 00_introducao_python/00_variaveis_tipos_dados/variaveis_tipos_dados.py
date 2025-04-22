# Variáveis e tipos de dados.

# em computação são utilizados principalmente os seguintes processos.
# -> Receber dados
# -> Armazenar dados
# -> Processar dados
# -> Exibir dados

# Variáveis
# São espaços reservados na memória do computador para armazenar dados.
idade = 32

# Constantes
# em python não há uma definição explícita de constantes, por isso é comum usar letras maiúsculas para indicar que é uma constante.
# essa é uma convenção da linguagem.
IDADE = 32

# Tipos de Dados
# -> int (Inteiro) 1, 2, 3, 10, -10, 0, -1, 100, 1279782
num_int = 10 # esse é um exemplo de um número inteiro

# -> float (Ponto Flutuante) 3.14, 0.1, 10.0, -0.1,
num_float = 10.5 # esse é um exemplo de um número ponto flutuante

# -> str (String) uma cadeia de caracteres. "Olá, Mundo!", 'Olá, Mundo!', "Olá, Mundo!", 'Ol' 
# a cadeia de caracteres pode ser delimitada por aspas simples ou duplas.
nome = "Douglas" # esse é um exemplo de uma string
nome2 = 'Douglas' # esse é outro exemplo de uma string

# -> bool (Booleano) True, False
verdadeiro = True # esse é um exemplo de um booleano
falso = False # esse é outro exemplo de um booleano

# -> list (Lista) uma coleção de dados que podem ser do tipo int, float, str, bool, etc. e é definida por colchetes. [1, 2, 3, 4, 5]
lista = [1, 2, 3, 4, 5] # esse é um exemplo de uma lista

# -> tuple (Tupla) uma coleção de dados que podem ser do tipo int, float, str, bool, etc. e é definida por parênteses. (1, 2, 3)
tupla = (1, 2, 3) # esse é um exemplo de uma tupla

# -> dict (Dicionário) uma coleção de dados que são representados por chaves e valores. {chave: valor} 
dicionario = {"nome": "Douglas", "idade": 32} # esse é um exemplo de um dicionário.


# -> set (Conjunto) uma coleção de dados que não podem ser repetidos. {1, 2, 3}.
conjunto = {1, 2, 3} # esse é um exemplo de um conjunto


# -> NoneType (Nulo) é um tipo de dado que representa a ausência de valor. None
nulo = None # esse é um exemplo de um nulo


# -> range (Intervalo) é um tipo de dado que representa uma sequência de números. range(10) é igual a 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
intervalo = range(10) # esse é um exemplo de um intervalo
print(intervalo) # imprime o intervalo