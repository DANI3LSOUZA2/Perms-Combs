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

    converter_list_perms()
    print("Total de combinações: {}".format(comb))

    return permsTotal


# Função para mandar as combinações ao arquivo txt
def converter_list_perms():
    new_list = []
    list_all = show_file('combinacoes.txt')
    cont_comb = 1
    if list_all is None:
        print("O arquivo está vazio, adicione []")
    else:
        for y in list_all:
            cont_comb = y['id']

            tupla_comb = tuple(y['comb'])

            new_list.append(tupla_comb)
        for x in old_list:
            if x not in new_list:
                new_list.append(x)
                tupla = tuple(x)

                y = "".join(tupla)

                list_txt = {
                    'id': cont_comb,
                    'comb': y
                }
                cont_comb += 1
                insert_file(list_txt, 'combinacoes.txt')
        print(old_list)

        for comb in new_list:
            if comb in old_list:
                if comb not in new_list:
                    x = "".join(comb)
                    cont_comb += 1

                    list_txt = {
                        'id': cont_comb,
                        'comb': x
                    }

                    insert_file(list_txt, 'combinacoes.txt')


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
