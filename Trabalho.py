import os
os.system("clear||cls")  
#variáveis
opcao = 0
quantidade = 0
quanta = 0
quantpl = 0
quantp = 0
quantq = 0
totala = 0.0
totalpl = 0.0
totalp = 0.0
totalq = 0.0
ta = 0.0
tpl = 0.0
tp = 0.0
tq = 0.0

while opcao != 5:
    print ("------------------------------------------")
    print ("1 - Açougue            - unidade - 25,00")
    print ("2 - Produto de Limpeza - unidade - 18,00")
    print ("3 - Padaria            - unidade - 10,00")
    print ("4 - Quitanda           - unidade - 12,00")
    print ("------------------------------------------")
    print ("Toda compra acima de 5 unidades receberá 5% de desconto.")
    print ("Digite 5 para terminar sua compra.\n")
    opcao = int(input("Digite a opção que quer comprar: "))
    print ("\n")
    if opcao == 1:
        quantidade = int(input("Digite a quantidade desejada: "))
        quanta = quanta + quantidade
        if quantidade > 5:
            totala = 25*quantidade
            totala = totala - (totala*0.05)
            ta = ta + totala
        else:
            totala = 25*quantidade
            ta = ta + totala        
    elif opcao == 2:
        quantidade = int(input("Digite a quantidade desejada: "))
        quantpl = quantpl + quantidade
        if quantidade > 5:
            totalpl = 18*quantidade
            totalpl = totalpl - (totalpl*0.05)
            tpl = tpl + totalpl 
        else:
            totalpl = 18*quantidade   
            tpl = tpl + totalpl 
    elif opcao == 3:
        quantidade = int(input("Digite a quantidade desejada: "))
        quantp = quantp + quantidade
        if quantidade > 5:
            totalp = 10*quantidade
            totalp = totalp - (totalp*0.05)
            tp = tp + totalp
        else:
            totalp = 10*quantidade
            tp = tp + totalp   
    elif opcao == 4:
        quantidade = int(input("Digite a quantidade desejada: "))
        quantq = quantq + quantidade
        if quantidade > 5:
            totalq = 12*quantidade
            totalq = totalq - (totalq*0.05)
            tq = tq + totalq
        else:
            totalq = 12*quantidade   
            tq = tq + totalq
    os.system("clear||cls")           

print ("---------------------------------------------------------------------------------------") 
if totala != 0:
    print("1 - Açougue            - Quantidade comprada: ", quanta, " - Valor total: ", ta)
if totalpl != 0:
    print("2 - Produto de limpeza - Quantidade comprada: ", quantpl, " - Valor total: ", tpl)
if totalp != 0:
    print("3 - Padaria            - Quantidade comprada: ", quantp, " - Valor total: ", tp) 
if totalq != 0:
    print("4 - Quitanda           - Quantidade comprada: ", quantq, " - Valor total: ", tq)
print ("---------------------------------------------------------------------------------------") 
print ("Valor total da compra foi de: ", ta + tpl + tp + tq)
print ("---------------------------------------------------------------------------------------\n")  
