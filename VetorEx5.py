vet1=[0]*6
aux = 0

for cont in range(0,6,1):
   vet1[cont] = int(input(f"Informe o número da posição {cont}: "))

print("=====Mostrando o Vetor original=====")
for cont in range(0,6,1):
   print(f"{vet1[cont]} ", end=' ')

for cont in range(0,3,1):
   aux = vet1[cont]
   vet1[cont] = vet1[5-cont]
   vet1[5-cont] = aux

print()
print("=====Mostrando o Vetor Invertido=====")
for cont in range(0,6,1):
   print(f"{vet1[cont]} ", end=' ')