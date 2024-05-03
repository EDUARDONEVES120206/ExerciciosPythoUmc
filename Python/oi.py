#1)
#funcao criada usuario
n1=0
# n2=0
# def Somando(n1,n2):
#     n1=int(input("digite numero"))
#     n2=int(input("digite numero"))
#     soma=n1+n2
#     print("result",soma)
# Somando(n1,n2)
#2)
lista={}
cont=0
nome=""
while nome!="fim":
    nome=input("digite o nome ")
    nota=int(input("digite a nota "))
    lista[cont]=[nome,nota]
    cont+=1
for i in lista:
    media=sum(lista/len(lista))
    print(media)
    maximo=max(lista)
    minimo=min(lista)
    print(max, min)

