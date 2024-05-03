import re
#binario

# num1=input("digite um numero ")
# padrao= r'\d+'
# soma1=0
# numeros=re.findall(padrao,num1)
# for i in range(len(numeros)):
#     soma1+=int(numeros[i])
# lista=[]
# bi={0:1,
#     1:2,
#     2:4,
#     3:8,
#     4:16,
#     5:32,
#     6:64,
#     7:128
#     }
# binario=str(soma1)[::-1]
# soma=0
# for i in range(len(binario)):
#     lista.append(int(binario[i])) 
#     if lista[i]==1:
#         soma+=bi[i]
#     elif lista[i]>1:
#         for i in range(len(numeros)):
#             soma+=int(numeros[i])
#         break
# print(f"resultado de {num1} = {soma}")

#melhorar o codigo
# soma=0
# soma2=0
# binario=1
# def verifica_binario(binar):
#     binar=list(binar)
#     for i,num in enumerate(list(binar)):
#         if num=='1' or num=='0':
#             pass
#         else:
#             return False
#     return True
# num1=input("")
# padrao= r'\d+'
# numeros=re.findall(padrao,num1)

# for i in range(len(numeros)):
#     soma+=int(numeros[i])

# binar=str(soma)[::-1]
# if verifica_binario(binar):
#     for i, num in enumerate(list(binar)):
#         if num=='1':
#             soma2+=binario
#             binario*=2
#         elif num=='0':
#             binario*=2
# else:
#     soma2=soma
# print(soma2)

#nao entendi bulhufas desse
# while True:
#     try:
#         a, b = [int(x) for x in input().strip().split(' ')]
#         print(a ^ b)
#     except EOFError:
#         break
lista=[]
num=int(input)
for i in range(num):
    lista.append(i)
while len(lista)>1:
    