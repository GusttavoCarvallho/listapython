# criando uma lista com elemntos duplicados 
lista_com_duplicados=[1,2,3,1,4,2,5,6,3,7,8,5,9]

# inicializanod uma lista  vazia para armazenar os elementos  unicos
lista_sem_duplicados =[]

# Utilizando um loop while para percorrer a lista e remover os elementos duplicados 
while lista_com_duplicados:
    elemento = lista_com_duplicados.pop(0)  # pop é usado para remover o elemento 
    if elemento not in lista_sem_duplicados:
        lista_sem_duplicados.append(elemento)
        
        #imprimindo resultado 
print("a lista sem duplicados é", lista_sem_duplicados)