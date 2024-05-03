RK= float(input("receba razao em kilos "))
RG= RK*1000
C1= float(input("digite o consumo 1 em gramas "))
C2= float(input("digite o consumo 2 em gramas "))

CT= 5*(C1+C2)
R= RG-CT

print ("resto do consumo", R)
