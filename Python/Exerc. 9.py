HT= float(input ("digite horas trabalhadas"))
S= float(input("receba salario minimo"))

SH = S/2
SB= HT*SH
imposto= SB*0.3
S= SB-imposto

print("salario igual a:", S)
