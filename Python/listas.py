import random 
# a=[]
# for i in range(5):
#     b=int(input("digite n "))
#     a.append(b)
# print(a)
# a.reverse()
# print(a)
# m=0
# nota=[]
# for i in range(4):
#     n=int(input("nota "))
#     nota.append(n)
# for i in range(0,4):
#     m=m+nota[i]
# m=m/4
# print(m)

# l=[]
# qtd=0
# v=["a","e","i","o",'u']
# for i in range(10):
#     c=input("digite uma letra ")
#     l.append(c)
  
    
#     if l[i] in v:
#             print("vogal")
#     else:
#             print(l[i])
#             qtd+=1
# print(qtd," consoantes")

# n=[]
# par=[]
# impar=[]
# for i in range(10):
#     d=int(input("digite um numero "))
#     n.append(d)
#     if d%2==0:
#         par.append(d)
#     else:
#         impar.append(d)
# print(par)
# print(impar)
# print(n)
# altura=[]
# idade=[]
# for i in range(5):
#     a=float(input("digite a altura "))
#     id=float(input("digite a idade "))
#     altura.append(a)
#     idade.append(id)
# altura.reverse()
# idade.reverse()
# print("alturas ",altura," idades " ,idade)

# a=[]
# soma=0
# for i in range(10):
#     n=int(input("n "))
#     a.append(n)
#     soma=soma+(a[i]**2)
# print(soma)


# dado=[1,2,3,4,5,6]
# qtd=[]
# qtd1=[0]*6
# for _ in range(100):
#     d=random.randint(1,6)
#     qtd.append(d)
#     qtd1[d-1]+=1
# for i in range (6):
#     print(f"quantidade de {dado[i]} : {qtd1[i]}")

# funcionarios={
# 1:["alexandre",434.456123789],
# 2:['anderson',1245698456  ],
# 3:['antonio',123456456],
# 4:['carlos',91257581],
# 5:['cesar',987458],
# 6:['rosemary',789456125]
# }
# for d in range(1,7):
#     nome,espaco=funcionarios[d]
#     porcentagem=(espaco*100)/2581
#     print("%i   %s    %.2f MB   %.2f%%  " %(d,nome,espaco,porcentagem))
#marco

# respostas=[]
# perguntas=["Telefonou para a vítima?",
# "Esteve no local do crime?",
# "Mora perto da vítima?",
# "Devia para a vítima?",
# "Já trabalhou com a vítima?"]
# print("respomda as opções com S/N")
# for i in range(4):
#     print(perguntas[i])
#     resposta=input("")
#     if resposta=="S":
#         respostas.append(resposta)
# if respostas.count("S")==2:
#     print("suspeito")
# if respostas.count("S")==3 or respostas.count("S")==4:
#     print("cumplice")
# if respostas.count("S")==5:
#     print("assassino")
# lista=["ola"]
# for i in lista
# if "a" in lista:
#     print(lista)

# lista1=[]
# lista2=[]
# lista3=[]
# lista4=[]
# for i in range (5):
#     valor1=input("digite valor da primeira lista ")
#     valor2=input("digite valor da segunda lista ")
#     valor3=input("digite valor da terceira lista ")
#     lista1.append(valor1)
#     lista2.append(valor2)
#     lista3.append(valor3)

# for i in range(5):
#     lista4.append(lista1[i])
#     lista4.append(lista2[i])
#     lista4.append(lista3[i])

# print(lista1,lista2,lista3,lista4)
# media=0
# aluno=[]
# cont=0
# for i in range (10):
#     idade=int(input("digite a idade "))
#     altura = float(input('digite a altura '))
#     media+=altura
#     if idade>13:
#         aluno.append(altura)
# media=media/i
# for i in range(len(aluno)):
#     if aluno[i]<media:
#         cont+=1
# print(f'a média é {media:.2f} e tem {cont} alunos com 13 anos acima dela ')

