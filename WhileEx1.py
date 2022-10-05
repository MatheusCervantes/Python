numero = 0
maior = 0
menor = 0
flag = True

numero = int(input("Informe o número: "))
maior = numero
menor = numero
while(numero != 0):
    if(numero > maior):
        maior = numero
    
    if(numero < menor) and (numero != 0):
        menor = numero
    
    numero = int(input("Informe o número: "))

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")