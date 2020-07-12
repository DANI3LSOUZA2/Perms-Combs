from itertools import product

List = input("Digite N's separado por espaços: ")
List = List.split(" ")

# n = quantidade de elementos
n = len(List)

# POSICOES = número de posições / ex: POSICOES = 1 (A), (B), (C), (D) / POSICOES = 2 (AA), (BB), (CC) , (...), (NN)
p = int(input("Até quantas posições deseja armazenar? "))


# Calculando o número total de combinações
# comb = número de combinações
comb = 0
permsTotal = []
for x in range(p):
    comb = n ** p + comb
    permsList = list(product(List, repeat=p))
    p -= 1
    permsTotal.append(permsList)

# Total de combinações concluído

# Mostrar cada combinação em forma de matriz no terminal
cont = 0
#for x in permsTotal:
    #for i in x:
        #print(i)
print("Total de combinações: {}".format(comb))
