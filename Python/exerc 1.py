import math
#exercicio 1
n1=float(input("digite um numero real "))
n2=float(input("digite outro numero real "))
n3=n1+n2
print("resultado da soma é " ,n3)

#exercicio 2
n1=float(input("digite um numero real "))
n2=float(input("digite outro numero real "))
n3=n1*n2
print("resultado da multiplicação é " ,n3)
#exercicio 3
L=float(input("digite largura do retangulo "))
A=float(input("digite altura do retangulo "))
P=L*2+A*2
Area=L*A
print("sua area é %f e seu perimetro é %f" %(Area,P))
#exercicio 4
Raio=float(input("digite o raio da circuferencia "))
Area=math.pi*Raio**2
Perimetro=2*math.pi*Raio
print("A area do circulo é %f e seu perimetro é %f " %(Area,Perimetro))
#exercicio 5
Parede=float(input("digite a area da parede "))
Azulejo=float(input("digite a area do azulejo "))
Necess=round(Parede/Azulejo)+0.5
print("será necessario %f azulejos "%(Necess))

#exercicio 13
TE=int(input("digite o total do estoque "))
TV=int(input("digite o total vendido "))
TV