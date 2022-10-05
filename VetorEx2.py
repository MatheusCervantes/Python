for cont in range(6):
   vet[cont] = int(input(f"Informe o número da posição {cont}: "))

for cont in range(6):
    if vet[cont] < 0:
        print (vet[cont] * -1)
    elif vet[cont] > 10:
        num2 = int(input('Digite outro valor: '))
        print (vet[cont] - num2)
    else:
        print (vet[cont]/5.0)