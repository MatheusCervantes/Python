idade = 0
sexo = ""
idade_media = 0.0
qtd_mulheres = 0
qtd_maiores = 0
soma_idades = 0	

for contador in range(0,20,1):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M ou F): ")
    
    if(sexo.upper() == "F"):
        qtd_mulheres += 1
    
    if (idade >= 18):
        qtd_maiores += 1
    
    soma_idades += idade


idade_media = soma_idades / 20

print(f"A turma está lotada.")
print (f"A média de idade dos inscritos é de: {idade_media}")
print (f"A quantidade de mulheres inscritas é: {qtd_mulheres}")
print (f"A quantidade de alunos maiores de idade é: {qtd_maiores}")