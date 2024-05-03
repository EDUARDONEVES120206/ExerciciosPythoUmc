import os
os.system('cls')
opc_enquete=""
qtd=0
total=0
votos={
    1:qtd,
    2:qtd,
    3:qtd,
    4:qtd,
    5:qtd,
    6:qtd
       }
nome_sistema={
1:"Windoes",
2: "Unix",
3: "Linux",
4: "Netware",
5: "Mac OS",
6: "Outro"
}
while True:
    opc_enquete=int(input('''Qual o melhor Sistema Operacional para uso em servidores?
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro'''
))
    if opc_enquete==0:
        break
    elif 1<=opc_enquete<=6:
        votos[opc_enquete]+=1
        total+=1
    else:
        print("Numero Invalido")

print("Sistema Operacional","Votos", "%" ,sep=" "*5)
for i in range(1,6):
    print(f"{nome_sistema[i]:<18} {votos[i]:>10} {votos[i]/total:>9.1%}")