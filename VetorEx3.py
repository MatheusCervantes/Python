vet = [0]*5
i = 0

for i in range(0,5,1):
    vet[i] = int(input('Digite um valor: '))

print ("Antes da troca:", vet)

for i in range(5):
    if vet[i] >= 0:
        vet[i] = 1
    else:
        vet[i] = 0

print ("Após troca:" , vet)