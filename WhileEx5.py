c1 = 0
c2 = 0
c3 = 0
brancos = 0
eleitores = 0
nulos = 0
c_venc = 0
voto = 0
nome_c1 = ""
nome_c2 = ""
nome_c3 = ""
nome_ven = ""

print("Os candidatos são: 1,2 e 3")
nome_c1 = input("Informe o Nome do candidato de código 1: ")
nome_c2 = input("Informe o Nome do candidato de código 2: ")
nome_c3 = input("Informe o Nome do candidato de código 3: ")

print("Para votar em branco Digite: 0")
print("Para votar em nulo Digite: 4")
print("Para sair do Programa Digite: -1")
print("------------------------------")

while(voto != -1):
    voto = int(input("Informe o seu voto: "))
    if((voto >= 0) and (voto <= 4)):
        if(voto == 0):
            brancos += 1
        else:
            if(voto == 1):
                c1 += 1
            else:
                if(voto == 2):
                    c2 += 1
                else:
                    if(voto == 3):
                        c3 += 1
                    else:
                        nulos += 1
            eleitores += 1
    else:
        if(voto != -1):
            print("Candidato inválido")

if((c1 > c2) and (c1 > c3)):
    c_venc = 1
    nome_ven = nome_c1
else:
    if((c2 > c1) and (c2 > c3)):
        c_venc = 2
        nome_ven = nome_c2
    else:
        if((c3 > c1) and (c3 > c2)):
            c_venc = 3
            nome_ven = nome_c3
        else:
            if((c1 == c2) and (c2 == c3)):
                c_venc = 0
                nome_ven = "Ocorreu um empate entre os três candidatos"
            else:
                if(c1 == c2):
                    c_venc = 0
                    nome_ven = "Ocorreu um empate entre os candidatos 1 e 2"
                else:
                    if(c2 == c3):
                        c_venc = 0
                        nome_ven = "Ocorreu um empate entre os candidatos 2 e 3"
                    else:
                        c_venc = 0
                        nome_ven = "Ocorreu um empate entre os candidatos 1 e 3"

print("------------------------------")
print(f"Candidato Vencedor: Código: {c_venc} nome: {nome_ven}")
print(f"Votos Brancos: {brancos}")
print(f"Votos Nulos: {nulos}")
print(f"Número de eleitores: {eleitores}")