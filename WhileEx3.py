idade = 0
t_apto = 0
t_n_apto = 0
continuar = ""
nome = ""
sexo = ""
saude = ""

continuar = "S"

while(continuar.upper() == "S"):
    nome = input("Informe o Nome: ")
    sexo = input("Informe o Sexo M-Masculino | F-Feminino: ")
    idade = int(input("Informe a Idade: "))
    saude = input("Informe a Saúde B-Bom | R-Ruim: ")
    
    if(idade >= 18):
        if(saude.upper() == "B"):
            if(sexo.upper() == "M"):
                print(f"O candidato {nome}, é apto")
                t_apto += 1
            else:
                print(f"O candidato {nome} não é apto pois não é do sexo Masculino")
                t_n_apto += 1
        else:
            print(f"O candidato {nome} não é apto pois possui saúde RUIM")
            t_n_apto += 1
    else:
        print(f"O candidato {nome} não é apto pois não possui 18 anos")
        t_n_apto += 1
    
    continuar = input("Deseja informa os dados de outro candidato S-Sim N_Não: ")

print(f"O Total de Aptos é: {t_apto}")
print(f"O Total de NÃO Aptos é: {t_n_apto}")