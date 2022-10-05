inf = 1
filho = 0
qtdcad = 0
totalfilho = 0
qtd100 = 0
salario = 0.0
somasal = 0.0
mediasal = 0.0
mediafilho = 0.0
perc100 = 0.0
maiorsal = 0.0

while(inf == 1):
    print("Escolha uma opção:")
    print("1 - para cadastrar")
    print("2 - para sair")
    inf = int(input())
    
    if(inf == 1):
        salario = float(input("Informe o salário: "))
        filho = int(input("Informe o número de filhos: "))

        somasal += salario
        totalfilho += filho
        qtdcad += 1

        if(salario > maiorsal):
            maiorsal = salario
        
        if(salario <= 100):
            qtd100 += 1

mediasal = somasal/qtdcad
mediafilho = totalfilho/qtdcad
perc100 = qtd100/qtdcad*100

print(f"A média de salário é: {mediasal}")
print(f"A média de filhos é: {mediafilho}")
print(f"O maior salário é: {maiorsal}")
print(f"{perc100}% Recebem até R$ 100,00")