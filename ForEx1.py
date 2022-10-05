numero = 0

numero = int(input("Informe um número: "))

for contador in range(1,11,1):
    print(f"{numero} X {contador} = {numero * contador}")