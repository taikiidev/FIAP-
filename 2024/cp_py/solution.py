def selec_solve(l):
    #definindo varíavel para contar as trocas
    count = 0
    #iterando a lista
    for i in range(len(l)):
        #definidindo variável 
        k = i
        #para cada iteração de i, itere a lista novamente com a variável j.
        for j in range(k+1,len(l)):
            #se o valor do elemento no indice j for menor que o elemento do indice k, altere o valor de k para j;
            if l[j] < l[k]:
                k = j
                count+=1

        l[i],l[k] = l[k],l[i]
    
    str = f"O total de alterações foi de {count}"

    return l,str

def insert_solve(l):

    #definindo varíavel para contar as trocas
    count = 0
    # iterar indexes lista 
    for i in range(1,len(l)):
        # criar chave para condicionais 
        key = l[i]
        # pegar elemento a esquerda da do indice i (ex: [1,4,5] -> na primeira iteração, i = 1 , j = 0)
        j = i-1 
        # verificar se valor esquerda ao indice é maior. Se sim, alterar os lugares
        while j >= 0 and l[j] > key:
            
            l[j+1] = l[j]
            j-=1
            count+=1
        l[j+1] = key 
        

    str = f"O total de alterações foi de {count}"

    return l,str

def bubble_solve(l):
    
    #definindo varíavel para contar as trocas
    count=0
    # iterando a lista 
    for i in range(len(l)):
        # para cada elemento iterado, itere a lista novamente, porém subtraindo 1
        for j in range(len(l)-1):
            # se o valor do elemento no indice j for maior do que o elemento do indice j+1, troque os valores
            if l[j] > l[j + 1]:
                #troca de valores
                l[j], l[j+1] = l[j+1], l[j]
                count+=1

    str = f"O total de alterações foi de {count}"

    return l,str

#inserir valores na lista para teste 
l = [4,3,6,5,2]

print(insert_solve(l))
# print(bubble_solve(l))
# print(selec_solve(l))


