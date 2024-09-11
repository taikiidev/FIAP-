from BUBBLE import *
from INSERT import *
from SELECT import *


# QUESTAO 1 - feito no arquivo functions.py , onde eu 
# criei as funcoes para cada algoritmo. 

# QUESTAO 2 - Foi feita nos 3 arquivos BUBBLE, INSERT e SELECT.abs

# QUESTAO 3 - Analisando aqui em baixo e comparando o numero de trocas

# Aqui eu vou analisar apenas o numero de trocas da lista desordenada e da ordenada decrescente, visto que a ordenada crescente ja esta ordenada

# Comecando pelas listas desordenadas:

hash_lista_desordenada = {}
hash_lista_ordenada = {}

hash_lista_desordenada["bubble"] = trocas_bubble
hash_lista_desordenada["insert"] = trocas_insert
hash_lista_desordenada["select"] = trocas_select

hash_lista_ordenada["bubble"] = trocas_bubble_decrescente
hash_lista_ordenada["insert"] = trocas_insert_decrescente
hash_lista_ordenada["select"] = trocas_select_decrescente

print(hash_lista_desordenada)
print(hash_lista_ordenada)



