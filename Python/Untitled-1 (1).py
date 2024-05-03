fim = int(input("Digite o último número de um intervalo para encontrar os primos: "))
n = 1

while n <= fim:
    primo = True  # Suponha que o número seja primo até prova em contrário
    divisor = 2

    # Verifique se o número é primo
    while divisor < n:
        if n % divisor == 0:
            primo = False  # Se o número for divisível por algum outro número, ele não é primo
            break  # Não é necessário continuar verificando os outros divisores
        divisor += 1

    # Se o número for primo, imprima-o
    if primo:
        print(n)

    n += 1
