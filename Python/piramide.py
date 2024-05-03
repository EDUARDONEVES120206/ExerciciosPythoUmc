espaco=" "
ponto="*"
d=55
for i in range (1,110,2):
    print(espaco*d,ponto*i,espaco*d)
    d-=1
d=0
for i in range(110,1,-2):
    print(espaco*d,ponto*i,espaco*d)
    d+=1
