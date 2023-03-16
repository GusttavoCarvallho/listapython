minha_lista=[17,8,10,6,2,4] # lista para ordenar 
trocado = True # precisamos dele para entyrar no loop while 

while trocado:
    trocado = False #sem trocas ate agora
    for i in range(len(minha_lista) -1):
        if minha_lista[i] > minha_lista[i + 1]:
           trocado = True # occoreu uma troca 
           minha_lista[i], minha_lista[i + 1] =minha_lista[i +1], minha_lista[i]
print(minha_lista)           