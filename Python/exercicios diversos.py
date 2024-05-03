import random
import math
#alguns exercicios de 

# ver qual numero é maior

# n1=int(input("digite um numero"))
# n2=int(input("digite outro numero"))
# if n1>n2 :
#     print(n1, "é maior que ",n2)
# elif n2>n1 :
#     print(n2, " é maior que ", n1)
# else :
#     print("iguais")

#ver se é par

# p1=float(input("digite um numero "))
# p2=p1%2
# if p2==0:
#     print(p1, " é par")
# else:
#     (p1," é impar")

#vogal ou consoante 
# l=input("digite uma letra ")
# if l=="a"or"e"or"i"or"o"or"u":
#     print("vogal")
# else:
#     ("consoante")

#compras frutas

# maca=float(input("digite quantos kilos de maca "))
# morango=float(input("digite quantos kilos de morango "))
# totalk=maca+morango
# if maca <=5  :
#     pmaca=maca*1.80
# else:
#         pmaca=maca*1.50
# if morango<=5:
#     pmorango=morango*2.50
# else:
#      pmorango=morango*2.20
# total=pmorango+pmaca
# if totalk>8 :
#      total=total*0.90
#      print("Desconto de 10%%, valor pago de R$%.2f por %.2f quilos de fruta" % (total, totalk))
# else:
#      print("valor pago de R$%.2f" % total)

#compras carne
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# tipocarne=int(input("digite qual carne você quer dentre as seguintes opções: \n"
#                 +"0. file duplo \n"
#                 +"1. alcatra \n"
#                 +"2. picanha"))
# pag=int(input("digite a forma de pagamento, 1 para cartao, 2 para dinheiro "))
# qtd=float(input("digite a quantidade em kilos: "))
# if tipocarne==0:
#     if qtd<=5:
#         preco=qtd*4.9
#     else:
#         preco=qtd*5.8
# if tipocarne==2:
#     if qtd<=5:
#         preco=qtd*5.9
#     else:
#         preco=qtd*6.8
# if tipocarne==3:
#     if qtd<=5:
#         preco=qtd*6.9
#     else:
#         preco=qtd*7.8
# else:
#     print("opção inválida")
# if pag==1:
#     desconto=preco*0.05
#     pag="cartão da loja"
# else:
#     desconto=0.0
#     pag="dinheiro"
# preco=preco-desconto

# print("CUPOM FISCAL \n "
#       +"Tipo de carne: %s \n"%["file duplo","alcatra", "picanha"] [tipocarne]
#       +"Quantidade: %.2f kilos \n" %qtd
#       +"Pagamento: %s \n" %pag
#       +"Desconto de: %.2f \n" %desconto
#        +"Preço total R$%.2f" %preco)


#numeros de um intervalo
# n1=int(input("digite o primeiro numero do intervalo "))
# n2=int(input("digite o ultimo numero do intervalo "))
# while n1<=n2:
#     print(n1," " )
#     n1+=1

#compras lanchonete
# enc="N"
# total=0
# while enc=="N":
    
#     cod=int(input('''digite o codigo do pedido, sendo:
#     Especificação   Código  Preço
#     Cachorro Quente 100     R$ 1,20
#     Bauru Simples   101     R$ 1,30
#     Bauru com ovo   102     R$ 1,50
#     Hambúrguer      103     R$ 1,20
#     Cheeseburguer   104     R$ 1,30
#     Refrigerante    105     R$ 1,00
#     '''))
#     if 100<=cod>=105:
#         qtd=int(input("digite a quantidade do item selecionado anteriormente: "))
#         precos={
#         100:(1.20,"Cachorro quente"),
#         101:(1.30, "Bauru Simples"),
#         102:(1.50, "Bauru com ovo"),
#         103:(1.20, "Hambúrguer"),
#         104:(1.30, "Cheeseburguer"),
#         105:(1.00, "Refrigerante")
#         }  
#         preco, nome=precos[cod]
#         valor=preco*qtd
#         total+=valor
#         print("O pedido de %i %s deu R$%.2f " %(qtd,nome,valor))
#         enc=input("encerrar pedido? S/N \n").upper()
#     else:
#         print("codigo inválido, digite novamente\n")
# print("total R$%.2f" %total)


# nome=input("digite o nome do atleta: ")
# menor=10
# maior=0
# media=0
# notas=[]
# for i in range(7):
#     nota=float(input("digite a nota do jurado %i "%i))
#     if nota>maior:
#         maior=nota
#     if nota<menor:
#         menor=nota
#     media+=nota
#     notas.append(nota)
# media=media/7
# # Converter todas as notas para strings formatadas
# notas_formatadas = '\n'.join(['Nota: %.2f' % nota for nota in notas])

# # Imprimir todas as notas
# print('''Atleta: %s
# %s

# Resultado final:
# Atleta: %s
# Melhor nota: %.2f
# Pior nota: %.2f
# Média: %.2f''' % (nome, notas_formatadas, nome, maior, menor, media))

# numeros primos
# fim=int(input("digite o ultimo numero de um intervalo para dizer primos "))
# n1=1

# divisor=2
# primo=True
# while n1<=fim:
    
#     while divisor>n1:
#         if  n1%divisor==0:
#           primo=False
#           break
        
#     divisor+=1
  
#     if primo==True:
#         print(n1)
#     n1+=1

#impar
# n=1
# while n<=50:
#     if n%2==0:
#         impar=False
#     else:
#         impar=True
#     if impar:
#         print(n)
#     n+=1

# n=int(input("digite um numero "))
# divisor=2

# while divisor<n:
#     primo=False
#     if n%divisor==0:
#         primo=False
#         continue
#     else:
#         primo=True
#         divisor+=1
# if primo:
#     print("e primo")
# else:
#     print("nao primo")


# i=True
# while i:
#     nome=input("digite um nome com mais de 3 letras ")
#     qtd=len(nome)
#     if qtd<=3:
#         print("nome curto ")
#         continue
#     idade=int(input("idade entre 0 e 150 "))
#     if idade<0 or idade>150:
#         continue
#     salario=float(input("salario "))
#     if salario<=0:
#         continue
#     sexo=input("digite o sexo, F/M").upper()
#     if sexo=="F" or sexo=="M":
#          i=False
#          print("dados validados")
#     else:
#         continue

#calculo de uma serie de numeros
# i=1
# n1=1
# n2=1
# soma=0
# for i in range (500):
#     S=n1/n2
#     soma=soma+S
#     n1+=1
#     n2+=2
# print(soma)

#um ao 20
# n1=1
# n2=1
# for n1 in range(1,21):
#     print(n1)
# for n2 in range(1,21):
#     print(n2,end=" ")

    
# print(random.randint(1,51))

# n=int(input("digite n "))
# i=1
# S=0
# while i<=n:
#     D=1/i
#     S=S+D
#     i+=1
# print(S)

