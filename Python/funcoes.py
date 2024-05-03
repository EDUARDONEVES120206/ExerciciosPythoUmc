import random, locale,datetime
from itertools import permutations

#1)
def imprimi (numero):
    for i in range(1,numero+1):
        print(f"{i} "*i)
n=int(input("digite numero"))
imprimi(n)

#2) ajuda do gpt, minha soluçao tinha lista
# def imprimi (numero):
#     for i in range(1,numero+1):  
#         linha=""
#         for j in range(1,i+1):
#             linha+= str(j)+" "    
#         print(linha)
# n=int(input("digite numero"))
# imprimi(n)

#3)
# def soma(n1,n2,n3):
#     result=n1+n2+n3
#     return result

# n1=int(input("digite"))
# n2=int(input("digite"))
# n3=int(input("digite"))
# print("o resultado ",soma(n1,n2,n3))

# melhor jeito

# lista=[]
# for i in range(3):
#     numero=int(input("digite "))
#     lista.append(numero)
# print(sum(lista))

#4)
# def positivo(numero):
#     if numero>=0:
#         return "P"
#     else:
#         return "N"
# numero=int(input("digite"))
# print(positivo(numero))

#5)


#8)
# def qtd(n):
#     nstring=str(n)
#     print(len(nstring))
# n=int(input("di "))

# qtd(n)
#9)

# lista=[]
# def inverter(numero):
#     print(numero[::-1])  
# nume=input("digite numero")
# inverter(nume)

#10)
# def craps():
#     while True:
#         input("pressione enter pra iniciar")
#         ponto=random.randint(2,12)
#         print("jogador 1 arremessa e tira ",ponto)
#         if ponto==7 or ponto==11:
#             print("ganhou!!")
#             break
#         elif ponto in [2,3,12]:
#             print("perdeu!!!")
#             break
#         else:
#             ponto2=0
#             while ponto!=ponto2:
#                 ponto2=random.randint(2,12)
#                 print("arremessou de novo e tirou ",ponto2)
#                 if ponto2==7:
#                     print("perdeu!!")
#                     break
#                 elif ponto2==ponto:
#                     print("ganhouu")
#                     break
# craps()

#11)
# locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
# dia=int(input("digite o dia "))
# mes=int(input("digite o mes "))
# ano=int(input("digite o ano "))
# try:
#     data=datetime.datetime(ano,mes,dia)
#     print(data.strftime("%d/%m/%Y"))
#     print(data.strftime("%B de %Y"))
# except ValueError:
#     print("Data inexistente")

#12)
# import random
# def funcao_anagrama(palavra):
#     letras = list(palavra)
#     anagrama = ''

#     while letras:
#         indice = random.randint(0, len(letras) - 1)
#         anagrama += letras.pop(indice)

#     print("Anagrama:", anagrama.lower())
# palavra = input("Digite a palavra para criar um anagrama: ")
# funcao_anagrama(palavra)

#13) 
# espaco=" "
# preench="+"
# def retangulo(linhas,colunas):
#     if 20<linhas<1 and 20<colunas<1:
#        linhas=20
#        colunas=18
#     print("-"*colunas)
#     print(f"|{preench*(colunas-2)}|\n"*linhas)
#     print("-"*colunas)   
# l=int(input("digite qtd linhas "))
# col=int(input("digite qtd colunas "))
# retangulo(l,col)

#14)
quadrado=[1,2,3,4,5,6,7,8,9]
quadrados=[]
soma=0
#n
# 1 2 3
# 4 5 6
# 7 8 9

#i
# 0 1 2
# 3 4 5
# 6 7 8

# def is_magic_square(square):
#     row_sum = square[0] + square[1] + square[2]
#     if (square[3] + square[4] + square[5] != row_sum or
#         square[6] + square[7] + square[8] != row_sum):
#         return False
    
#     col_sum = square[0] + square[3] + square[6]
#     if (square[1] + square[4] + square[7] != col_sum or
#         square[2] + square[5] + square[8] != col_sum):
#         return False
    
#     if square[0] + square[4] + square[8] != row_sum or square[2] + square[4] + square[6] != row_sum:
#         return False
    
#     return True

# def find_magic_squares():
#     squares = []
#     numbers = list(range(1, 10))
    
#     for perm in permutations(numbers):
#         if is_magic_square(perm):
#             squares.append(perm)
    
#     return squares

# def print_magic_squares():
#     magic_squares = find_magic_squares()
#     for square in magic_squares:
#         print(square[0], square[1], square[2])
#         print(square[3], square[4], square[5])
#         print(square[6], square[7], square[8])
#         print()

# print_magic_squares()



