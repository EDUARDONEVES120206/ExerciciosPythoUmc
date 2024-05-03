def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(espaco_utilizado, espaco_total):
    return (espaco_utilizado / espaco_total) * 100

def main():
    usuarios = []
    espaco_total = 0

    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            usuario, espaco = linha.split()
            usuarios.append((usuario, int(espaco)))
            espaco_total += int(espaco)

    usuarios.sort(key=lambda x: x[1], reverse=True)

    with open("relatorio.txt", "w") as relatorio:
        relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        relatorio.write("------------------------------------------------------------------------\n")
        relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")
        
        for i, (usuario, espaco) in enumerate(usuarios, start=1):
            espaco_mb = bytes_para_mb(espaco)
            percentual = calcular_percentual(espaco, espaco_total)
            relatorio.write(f"{i:<5}{usuario:<15}{espaco_mb:>15.2f} MB{'':>10}{percentual:>10.2f}%\n")

        relatorio.write("\nEspaço total ocupado: {:.2f} MB\n".format(bytes_para_mb(espaco_total)))
        relatorio.write("Espaço médio ocupado: {:.2f} MB\n".format(bytes_para_mb(espaco_total) / len(usuarios)))

if __name__ == "__main__":
    main()
