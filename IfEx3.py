agua = 0

agua = int(input("Digite a quantidade de pontos de água encontrado: "))

if(agua <= 10):
    print(f"O solo é rochoso!")
else:
    if((agua > 10) and (agua <= 40)):
        print(f"O solo é firme!")
    else:
        if((agua > 40) and (agua <=80)):
            print(f"O solo é pantanoso!")
        else:
            print(f"Quantidade de água inválida!")