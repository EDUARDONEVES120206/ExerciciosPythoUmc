import datetime, locale,random
#1)
# string1=input("digite ")
# string2=input("digite ")
# tamanho1=len(string1)
# tamanho2=len(string2)
# print(f"tamanho de {string1} = {tamanho1} caracteres")
# print(f"tamanho de {string2} = {tamanho2} caracteres")
# if tamanho1 ==  tamanho2:
#     print("tem o mesmo tamanho")
# else:
#     print("nao tem")
# if string1==string2:
#     print("sao iguais")

#2)
# nome=input("digite nome ")
# print(f"{nome.upper()[::-1]}")

#3)
# nome=input("digite nome ")
# for i in list(nome):
#     print (i)

#4)
# nome=input("digite nome ")
# for i in range(len(nome)+1):
#     print (f"{nome[:i]}")

#5)
# nome=input("digite nome ")
# for i in range(len(nome)+1):
#     print (f"{nome[i:]}")

#6)
# locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
# dia=int(input("digite dia"))
# mes=int(input("digite mes"))
# ano=int(input("digite ano"))
# data=datetime.datetime(ano,mes,dia)
# print(data.strftime("%d/%B/%Y"))

#7)
# espacos=0
# vogais=0
# frase=input("digite uma frase ")
# lista=list(frase)
# for i in lista:
#     if i in ['a','e','i','o','u']:
#         vogais+=1
#     if i==" ":
#         espacos+=1
# print(f'tem {espacos} espacos {vogais} vogais')

#8)
# frase=input("digite uma frase ")
# frase2=""
# lista=list(frase)
# for i in lista:
#     if i==" ":
#         lista.remove(i)
# if lista == lista[::-1]:
#     print(f"{frase} é um palindromo")
# else:
#     print(f"{frase} não é um palindromo")

#9)

# cpf=input('digite cpf no exato formato "xxx.xxx.xxx-xx"')
# cpf=list(cpf)
# if len(cpf)<14:
#     print("falta caracteres")
# if len(cpf)>14:
#     print("ultrapassou os caracteres")
# else:
#     if cpf[3]!="." and cpf[7]!="." and cpf[11]!=".":
#         print("coloque os pontos")

#10)

#11)
# forca=open(r"Exercicios_Diversos\A parte\forca.txt","r")
# palavras=[]
# palavra2=[]
# palavra3=[]
# palavra=()
# cont=5
# for i in forca:
#         palavras.append(i.split())
# forca.close()

# indice=random.randint(0,len(palavras)-1)
# palavra=list(palavras[indice][0])
# qtd=len(palavra)
# palavra3=palavra[:]
# while palavra3 and cont>0:
#     tentativa=input(f"advinhe uma letra{"_ "*qtd} ")
    
#     if tentativa in palavra:
#         index=palavra.index(tentativa)
#         palavra2.insert(index,tentativa)
#         palavra3.remove(tentativa)
#         print(palavra2)
#         print(palavra)
#     else:
#         cont-=1
#         print(f"vc tem {cont} tentativas restantes")
# print("vc ganhou!!")
    
# #ajuda do gpt


# with open(r"Exercicios_Diversos\A parte\forca.txt", "r") as forca:
#     palavras = [linha.strip() for linha in forca]

# palavra = random.choice(palavras)
# qtd = len(palavra)
# palavra3 = palavra[:]
# palavra2 = ['_'] * len(palavra)

# cont = 5
# while palavra3 and cont > 0:
#     tentativa = input(f"adivinhe uma letra {' '.join(palavra2)}: ")
    
#     if tentativa in palavra:
#         indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
#         for index in indices:
#             palavra2[index] = tentativa
#         palavra3 = palavra3.replace(tentativa, '_')
#         print(''.join(palavra2))
#     else:
#         cont -= 1
#         print(f"Você tem {cont} tentativas restantes.")

# if cont > 0:
#     print("Você ganhou!!")
# else:
#     print(f"Game over! A palavra era: {palavra}")

#12)

# telefone=input("digite numero de telefone ")
# if len(telefone)==7:
#     print("tem 7 digitos, adcionando o 3 ")
#     telefone="3"+telefone[:3]+"-"+telefone[3:]
#     print(telefone)

#13)
# cont=6
# def embaralhar(palavra):
#     embaralhado=""
#     palavra=list(palavra)
#     while palavra:
#         embaralhado+=palavra.pop(random.randint(0,len(palavra)-1))
#     return embaralhado
# with open(r"Exercicios_Diversos\A parte\anagramas.txt","r") as palavras:
#     palavras=[linha.strip() for linha in palavras]
# palavra=random.choice(palavras)
# embaralhado=embaralhar(palavra)
# while cont>0:
#     advinha=input(f"A palavra embaralhada é {embaralhado}, vc tem {cont} chanced de advinhar, qual é a palavra?")
#     if advinha == palavra:
#         print("Acertouuu")
#         break
#     else:
#         cont-=1
#         print(f"Errouuu, {cont} tentativas ")

#14)

# leet={
#     "a":'4',
#     "b":'13',
#     "c":'(',
#     "d":'[)',
#     "e":'3',
#     "f":'|',
#     "g":'6',
#     "h":'|-|',
#     "i":'|',
#     "j":']',
#     "k":'|<',
#     "l":'1',
#     "m":'|Y|',
#     "n":'/\/',
#     "o":'0',
#     "p":'|>',
#     "q":'0,',
#     "r":'|2',
#     "s":'5',
#     "t":'7',
#     "u":'[_]',
#     "v":'\/',
#     "w":'\v/',
#     "x":'}{',
#     "y":"'/",
#     "z":'2'
# }
# formatado=""
# palavra=input("digite a palavra")
# palavra=list(palavra)
# for i in range(0,len(palavra)):
#     formatado+=leet[palavra[i]]+" "
# print(formatado)