import re
#1)
# numeros=''
# ips=[]
# ip_invalido=[]
# with open(r'Exercicios_Diversos\A parte\ip.txt','r') as arquivo:
#     for i in arquivo:
#         ips.append(i.split())
#     padrao= r'\d+'
#     for i,ip in enumerate(ips):
#         ip=str(ip)
#         numeros=re.findall(padrao,ip)
#         for _, n in enumerate(numeros):
#                 n=int(n)
#                 print(n)
#                 if n>255:
#                     ip_invalido.append(ips.pop(i))
# with open(r'Exercicios_Diversos\A parte\ip_formatado.txt','w') as arquivo:
#     arquivo.write('IP VALIDO')
#     for i,_ in enumerate(ips):
#         arquivo.write(' '.join(ips[i])+'\n')
#     arquivo.write("\nIP INVALIDO\n")
#     for i,_ in enumerate(ips):
#         arquivo.write(' '.join(ip_invalido[i]) + '\n')

#2)
# frase="ola penis"
# frase=(frase[:1].upper())+frase[1:]
# print(frase)
# print(len(frase))
# palavra=input("digite sua palavra ")
# if len(palavra)>=10:
#     print("palavrao")
# else:
#     print("palavrinha")

num1=input("digite um numero ")
padrao= r'\d+'
soma1=0
numeros=re.findall(padrao,num1)
for i in range(len(numeros)):
    soma1+=int(numeros[i])
lista=[]
bi={0:1,
    1:2,
    2:4,
    3:8,
    4:16,
    5:32,
    6:64,
    7:128
    }
binario=str(soma1)[::-1]
soma=0
for i in range(len(binario)):
    lista.append(int(binario[i])) 
    if lista[i]==1:
        soma+=bi[i]
    elif lista[i]>1:
        for i in range(len(numeros)):
            soma+=int(numeros[i])
        break
print(f"resultado de {num1} +  = {soma}")