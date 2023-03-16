#criando uma lista de numeros 
numeros = [10, 20, 30, 40, 50]

#Inicializando a variavel que ira armazenar o mair número 

maior_numero = numeros[0]

# usando um loop for para percorrer a lista e encontrar o maior numero 
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
        
        # Iprimindo o resultado 
        print("o maior numero na lista é:", maior_numero)