vet1=[0.0]*50
vet2=[0.0]*50

for cont in range(0,50,1):
   vet1[cont] = int(input(f"Informe o número da posição {cont}: "))
   if(cont % 2 == 0):
      vet2[cont] = vet1[cont] * 1.02
   else:
      vet2[cont] = vet1[cont] * 1.05

print("=====Mostrando o Vetor original=====")
for cont in range(0,50,1):
   print(f"{vet1[cont]:.2f} ", end=' ')

print()
print("=====Mostrando o Vetor resposta=====")
for cont in range(0,50,1):
   print(f"{vet2[cont]:.2f} ", end=' ')