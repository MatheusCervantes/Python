numero = 0
maior_a = 0
menor_a = 0

def f_maior(num, contador, maior):
    if(contador == 1):
        maior = num
    else:
        if(num >= maior):
            maior = num
    return maior
       
def f_menor(num, contador, menor):
    if(contador == 1):
        menor = num
    else:
        if(num <= menor):
            menor = num
    return menor

for cont in range(1,5,1):
    numero = int(input("Informe o número: "))
    maior_a = f_maior(numero, cont, maior_a)
    menor_a = f_menor(numero, cont, menor_a)

print(f"O maior é: {maior_a}")
print(f"O menor é: {menor_a}")