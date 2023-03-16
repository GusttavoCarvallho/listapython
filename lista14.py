# etapa 1:
banda=[]
print('etapa 1:',banda)

#etapa 2
banda.append('john lennom')
banda.append('paul mccarteny')
banda.append('george herrison')
print('etapa2:', banda)

#etapa 3:
for menbers in range(2):
    banda.append(input('novo menbro'))
print('etapa 3:', banda)    

#etapa 4:

del banda[-1]
del banda[-1]
print('etapa4:', banda)
#etapa 5

banda.insert(0,'ringostarr')
print('etapa5:', banda)
print('the fab:',len(banda))