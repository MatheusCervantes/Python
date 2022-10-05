#cont = 0
vet=[0]*5

for cont in range(0,5,1):
   vet[cont] = int(input(f"Informe o número da posição {cont}: "))

print("=====Mostrando o Vetor=====")
for cont in range(0,5,1):
   print(f"{vet[cont]} ", end=' ')