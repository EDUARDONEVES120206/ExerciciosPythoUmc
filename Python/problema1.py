#UMC ADS - 1°D
#Nomes: Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

# Calculo do salário liquido liquido depois dos descontos governamentais.
SH=float(input("Digite o salário por hora: "))
HT=float(input("Digite as horas trabalhadas no mês: "))
SB=SH*HT
IR=SB*0.11
INSS=SB*0.08
SIND=SB*0.05
SL=SB-(IR+INSS+SIND)
print("O salário bruto é R$" ,SB ,"\n"+
       "O INSS pago é de R$ ",INSS," \n"+
      "O valor pago ao sindicato é de R$ ",SIND," \n"+
      "O salário líquido é de R$",SL)
