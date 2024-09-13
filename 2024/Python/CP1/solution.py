from __BUBBLE import *
from __INSERT import *
from __SELECT import *


# QUESTAO 1 - Resolvida no arquivo functions.py

# QUESTAO 2 - Foi feita nos 3 arquivos _BUBBLE, _INSERT e _SELECT.

# QUESTAO 3 - Analisando aqui em baixo e comparando o numero de trocas

# Criando hashmaps para iterar e devolver valor mais baixo (com menos trocas)

hash_lista_desordenada = {}
hash_lista_ordenada_crescente = {}
hash_lista_ordenada = {}

hash_lista_desordenada["bubble"] = trocas_bubble
hash_lista_desordenada["insert"] = trocas_insert
hash_lista_desordenada["select"] = trocas_select

hash_lista_ordenada["bubble"] = trocas_bubble_decrescente
hash_lista_ordenada["insert"] = trocas_insert_decrescente
hash_lista_ordenada["select"] = trocas_select_decrescente

hash_lista_ordenada_crescente["bubble"] = trocas_bubble_crescente
hash_lista_ordenada_crescente["insert"] = trocas_insert_crescente
hash_lista_ordenada_crescente["select"] = trocas_select_crescente

# print(hash_lista_desordenada)
# print(hash_lista_ordenada)
# print(hash_lista_ordenada_crescente)

print(f'Algoritmo com menor trocas na lista ordenada crescente: {encontrar_menor(hash_lista_ordenada_crescente)}')
print(f'Algoritmo com menor trocas na lista ordenada decrescente: {encontrar_menor(hash_lista_ordenada)}')
print(f'Algoritmo com menor trocas na lista desordenada: {encontrar_menor(hash_lista_desordenada)}')






