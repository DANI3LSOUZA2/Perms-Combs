from itertools import product

POSICOES = 4
comb = 0


def permutar(n):
    posicao_atual = POSICOES
    comb = 0
    permsTotal = []

    for x in range(POSICOES):
        comb = n ** posicao_atual + comb
        permsList = list(product(List, repeat=posicao_atual))
        posicao_atual -= 1
        permsTotal.append(permsList)

    for x in permsTotal:
        for i in x:
            print(i)

    print("Total de combinações: {}".format(comb))
    return permsTotal


List_adc = 0
List = []

List.append(input("Digite uma palavra: "))

# n = quantidade de elementos

n = len(List)

permsTotal = permutar(n)

while True:

    escolha = input("Deseja adicionar mais variáveis ?(s ou n) ")

    if escolha == "s":
        List.append(input("O que deseja adicionar ? "))

        # List.append(List_adc)
        # POSICOES = len(List)
        n = len(List)

        permsTotal = permutar(n)

        continue

    else:
        break


# comb = número de combinações

# Mostrar cada combinação em forma de matriz no terminal


