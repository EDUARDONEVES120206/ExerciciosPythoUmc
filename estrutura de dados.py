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
# import math
# lista={}
# cont=0
# nome=""
# while nome!="fim":
#     nome=input("digite o nome ")
#     nota=int(input("digite a nota "))
#     lista[nome]=nota
# total=(len(lista))
# soma=sum(lista.values())
# media=(soma/total)
# print(media)
# maximo=max(lista.values())
# minimo=min(lista.values())
# print(maximo, minimo)

# print("tabuada")
# numero=int(input("digite o valor "))
# for i in range(1,11):
#     multiplicacao=numero*i
#     print("a tabuada é ", multiplicacao)

# lista=[] 
# numero=0
# while numero!=4:
#     numero=int(input("digite um numero, 4 pra finalizar"))
#     lista.append(numero)
# lista.sort()
# print("crescente ",lista)
# lista.sort(reverse=True)
# print("decrescente ",  lista)
# soma=sum(lista)
# media=soma/len(lista)
# print(f"a soma é {soma} a media é {media}")

#3)
matriz=[]
l1=[]
l2=[]
l3=[]
for i in range(1,4):
        numero=int(input("digite um numero "))
        l1.append(numero)
for i in range(1,4):
        numero=int(input("digite um numero "))
        l2.append(numero)
for i in range(1,4):
        numero=int(input("digite um numero "))
        l3.append(numero)
matriz.append(l1)  
matriz.append(l2)  
matriz.append(l3)  
soma=(matriz[0][0]*matriz[1][1]*matriz[2][2]+matriz[0][1]*matriz[1][2]*matriz[2][0]+matriz[0][2]*matriz[1][0]*matriz[2][1])-(matriz[0][1]*matriz[1][1]*matriz[2][0]+matriz[0][0]*matriz[1][2]*matriz[2][1]+matriz[0][1]*matriz[1][0]*matriz[2][2])
print(soma)
#testando git
