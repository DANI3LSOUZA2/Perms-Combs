from itertools import product
from simplejson_functions import *

POSICOES = 4
comb = 0
old_list = []
list_txt = {}


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

            if i in old_list:
                continue

            else:
                print(i)
                old_list.append(i)  # Old_list corresponde às combinações que não se repetem

    print("Total de combinações: {}".format(comb))

    return permsTotal


# Função para mandar as combinações ao arquivo txt
def converter_list_perms():

    list_all = show_file('combinacoes.txt')

    if list_all is None:
        cont_comb = 1
    else:
        for y in list_all:
            cont_comb = y['id']

        print(cont_comb)

    for comb in old_list:
        x = "".join(comb)

        list_txt = {
            cont_comb: x
        }

        insert_file(list_txt, 'combinacoes.txt')

        cont_comb += 1


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
