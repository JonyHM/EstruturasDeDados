# -*- coding: utf-8 -*-

import Merlim

def resposta():
        if casamento:
                print('Casamento possível')
        else:
                print('Casamento impossível!\nPreferências de ', end='')
                for d in impossiveis:
                        print(d,'- ', end='')
                print(' são insufucientes')

## Casamento ##
damas = {}
pretendentes = []
impossiveis = []
casamento = False
prefer = open("casamento no.txt", "r")

## Criando dicionário com nomes das damas relacionados aos nomes de suas preferências
for linha in prefer:
        nomes = linha.split()
        damas[nomes[0]] = nomes[1:]

## Criando lista de conjuntos de prentendentes preferidos e verificando se todas tem queridos
for nome in damas:
        if len(damas[nome]) < 1:
                casamento = False
                impossiveis.append(nome)
                
        pretendentes += damas[nome]

if len(damas) < len(set(pretendentes)):
        casamento = True

resposta()
#         if len(damas[nome]) < 1:
#                 casamento = False
#                 impossiveis.append(nome)
#         else:
#                 pretendentes.append(damas[nome])

# if not casamento:
#         resposta()
# else:
#         ## Caso o número de pretendentes for menor, que o número de damas, é impossível
#         for N in Merlim.enumerações(pretendentes):
#                 if len(N) >= len(pretendentes):
#                         casamento = True
#         resposta()

# ## Távola redonda ##
# listaAmizades = {}
# tavola = []
# amizades = open("cavaleiros.txt", "r")  

# for linha in amizades:
#         linha = linha.split()
#         listaAmizades[linha[0]] = linha[1:]

# for cavaleiro in listaAmizades:

#         for x in Merlim.permutações(listaAmizades[cavaleiro]):
#                 print(cavaleiro)
#                 print(x)
        
#         # print(cavaleiro)
#         # for nome in listaAmizades:
#         #         if cavaleiro == nome:
#         #                 continue
#         #         elif listaAmizades[nome]:
#         #                 print(nome + '2')

#         # print(listaAmizades[cavaleiro])