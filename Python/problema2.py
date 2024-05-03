#UMC ADS - 1°D
#Nomes: Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

# CALCULA A QUANTIDADE DE LATAS A SEREM USADAS PARA PINTAR UMA AREA E O PREÇO DAS VERSOES DAS LATAS DE 18 E 3,6 LITROS
TA=float(input("Digite a área em metros quadrados a ser pintada: "))
TA=TA*1.10
TIN=TA/6
QT1=TIN/18
QT1R=TIN//18
QT2=TIN/3.6
QT2R=TIN//3.6
AR2=QT2-QT2R
AR1=QT1-QT1R
SOM1=1-AR1
SOM2=1-AR2
QT1=QT1+SOM1
QT2=QT2+SOM2

P1=QT1*80
P2=QT2*25
print ("A quantidade de tinta utilizada será de ",QT1," latas de 18, e ",QT2," de 3,6 \n"
      "O preço com as latas de 18 será R$",P1 ,"\n e de latas de 3,6 de R$",P2)