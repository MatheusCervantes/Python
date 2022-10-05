sal = 0.0
novosal = 0.0
boni = 0.0
aux = 0.0

sal = float(input("Digite o salário do funcionário: "))

if(sal<=500):
    boni=sal*(5/100)
else:
    if((sal>500) and (sal<=1200)):
        boni=sal*(12/100)
    else:
        boni=0

if(sal<=600):
    aux=150
else:
    aux=100

novosal=sal+boni+aux

print(f"O valor do novo salário é:R${novosal:,.2f}")