from functions import *

# criando listas de referência

sorted_list_decresc = [10,9,8,7,6,2]
lista = [7,3,9,12,4,2]
sorted_list_cresc = [1,2,3,4,5,6]

# realizando calculos de quantidade de trocas, com as funções importadas

trocas_bubble_decrescente = bubble_solve(sorted_list_decresc)
trocas_bubble_crescente = bubble_solve(sorted_list_cresc)
trocas_bubble = bubble_solve(lista)

