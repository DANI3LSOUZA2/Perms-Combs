from itertools import product
from simplejson_functions import *
from Teste import transferir_old_list

import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('emails_table')

POSICOES = 4
comb = 0
old_list = transferir_old_list()
list_txt = {}
new_list = []


def put_email(email):
    table.put_item(
        Item={
            'id': email
        }
    )


def permutar(n):
    list_all = show_file('combinacoes.txt')
    posicao_atual = POSICOES
    comb = 0
    permsTotal = []

    if not list_all:
        cont_comb = 0
    else:
        for y in list_all:
            cont_comb = y['id']

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
                # transformar i em um dicionário para enviar ao arquivo teste

                new_list.append(i)  # new_list corresponde às novas combinações

                # pegar o id da combinação e a combinação no arquivo teste.txt
                tupla = tuple(i)

                y = "".join(tupla)
                cont_comb += 1
                comb_teste = {
                    'id': cont_comb,
                    'comb': y
                }

                put_email(y)

                insert_file(comb_teste, 'combinacoes.txt')

    print("Total de combinações: {}\n".format(comb))
    id_variavel['combs'] = comb
    edit_file('id', 0, id_variavel_antigo, 'quant_var.txt')

    return permsTotal


id_variavel = find_file("id", 0, "quant_var.txt")
id_variavel_antigo = id_variavel

List = id_variavel['variaveis']

# List.append(input("Digite a(s) variavel(eis): "))

# n = quantidade de elementos

# n = len(List)

# permsTotal = permutar(n)

while True:

    print("Variáveis já existentes: {}".format(id_variavel['variaveis']))
    escolha = input("Deseja adicionar mais variáveis ?(s ou n) ")
    variaveis = id_variavel['variaveis']

    if escolha == "s":
        var = input("O que deseja adicionar ?")

        if var in variaveis:
            print("Essa variável ja existe")
        else:
            List.append(var)

            n = len(List)

            id_variavel['variaveis'] = List
            id_variavel['quant'] = n
            # List.append(List_adc)
            # POSICOES = len(List)

            edit_file("id", 0, id_variavel, 'quant_var.txt')

            permsTotal = permutar(n)
            old_list = transferir_old_list()
            continue

    else:
        break


