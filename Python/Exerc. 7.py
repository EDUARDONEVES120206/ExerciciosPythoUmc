S=int(input("digite o tempo em segundos"))
M= S//60
R= (S%60)*60
H= M + R

print("tempo é de", M ," minutos e ", R," segundos" )