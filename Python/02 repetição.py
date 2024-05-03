import os  
#1)
# for n in range(10,0,-1):
#     print("numeros de 10 a 1", n)

#2)
# n=int(input("digite um numero"))
# i=1
# while i<n:
#     print(i)
#     i+=1

#3)
# n=int(input("digite um numero "))
# for i in  range(11):
#     print(i*n)

#4)
# nome=input("digite nome ")
# senha=input("digite senha ")
# while senha==nome:
#     print("erro, nome e senha iguais")
#     nome=input("digite nome ")
#     senha=input("digite senha ")
# print("bem vindo",nome)

#5) 
# numero=int(input("digite um numero "))
# result=0
# for i in range(numero,1,-1):
#     numero*=i
# print(numero)

#6)
# os.system('clear')
# fibonnaci=int(input("digite o ultimo numero de fibonnaci"))
# anterior=1
# proximo=1
# print("1º termo= ",anterior)
# print("2º termo= ",proximo)
# contador=3
# for i in range(fibonnaci-2):
#     proximo+=anterior  
#     print("%iº termo = %i" %(contador,proximo))
#     anterior=proximo-anterior
#     contador+=1
#7)
# os.system('cls')
# opc=1
# while opc==True:
#     idade=int(input("digite sua idade para ver desconto, ou 9999 para finalizar "))
#     if idade==9999:
#         break
#     elif idade<6 or idade>=60:
#         print("tem direito")
#     elif idade==9999:
#         break
#     else:
#         print("nao tem direito ")
    
#8)
# numero1=int(input("digite o primeiro numero"))
# numero2=int(input("digite o segundo numero"))
# opcao=0
# while opcao!=4:
#('cls')
#     opcao=int(input("digite a opcao, 1 soma, 2 subtracao, 3 multiplicacao, 4 sair "))
#     if opcao==1:
#        soma=numero1+numero2
#        print("a soma dos dois numeros é ",soma )
#     elif opcao==2:
#         subtracao=numero1-numero2
#         print("a subtração dos dois numero é igual a", subtracao)
#     elif opcao==3:
#         multiplicacao=numero1*numero2
#         print("a multiplicacao dos dois numeros é", subtracao)

#9) 
# resultado=0
# todos_numeros=[]
# opcao=0
# while opcao!=5:
#     opcao=int(input('''escolha uma opção
#                     1) Ler um novo numero e o adicionar a somatoria
#                     2) Exibir o valor atual da somatoria
#                     3) Exibir a quantidade de numeros digitados ate o momento
#                     4) Mostrar a media dos numeros digitados ate o momento
#                     5) Sair
#                     '''))
#     if opcao==1:
#         numero=int(input("digite um novo numero "))
#         resultado+=numero
#         todos_numeros.append(numero)
#     elif opcao==2:
#         print("o valor da somatoria é igual a",resultado)
#     elif opcao==3:
#         contador=len(todos_numeros)
#         print(contador)
#     elif opcao==4:
#         media=resultado/contador
#         print("a media de numeros digitados é igual a", media) 

#10)
# opcao=0
# lista=[]
# while opcao!=5:
#     opcao=int(input('''Escolha 
#             1)Relatório com os itens da lista
#             2)Incluir item na lista
#             3)Alterção de item
#             4)Exclusão de item
#             5)fim'''))
#     if opcao==1:
#         print("aqui os itens da lista",lista)
#     if opcao==2:
#         novo=input("digite novo item ")
#         if not novo=="":
#             lista.append(novo)
#             print("Valor adcionado")
#         else:
#             print("valor nao definido")
#     if opcao==3:
#         alterar=input("digite qual valor deseja alterar ") 
#         alterarnovo=input("digite qual valor deseja colocar ") 
#         if not alterar == "" and  alterar in lista:
#             i=lista.index(alterar)
#             if not alterarnovo == "":
#                 lista[i]=alterarnovo 
#                 print("Valor alterado")
#             else:
#                 print("valor nao definido")
#         else: 
#             print("Valor nao encontrado ")
        
           
#     if opcao==4:
#         deleta=input("digite qual deseja deletar")
#         if not deleta ==  "" and deleta in lista:
#             i=lista.index(deleta)
#             del lista[i]
#             print("Valor deletado")
#         else:
#             print("Digite o valor corretamente ")
# print("operações terminadas")

