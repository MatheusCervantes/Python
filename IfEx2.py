tc = ""
ct = 0
valor_litro = 0.0
valor_tanque = 0.0

#programa
tc = input("Digite o tipo de carro: G - Gasolina ou A - Álcool: ")
ct = int(input("Digite o volume do tanque do carro: "))

if(tc == "A"):
    print(f"Você escolheu um veículo Gasolina!!!")
else:
    print(f"Você escolheu um veículo Álcool!!!")

valor_litro = float(input("Informe o valor do litro: "))

valor_tanque = ct * valor_litro

print(f"O valor gasto para encher o tanque será: R${valor_tanque:,.2f}")