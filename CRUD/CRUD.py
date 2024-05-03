#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

#Pré Projeto Crud em Python
import os
import sqlite3
import pwinput
from datetime import datetime

estrato = []
os.system('cls')

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criando a tabela de usuários se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    saldo INTEGER
                )''')

conn.commit()


def extrato():
    arquivo_estrato = open("CRUD\estrato.txt", "w")
    arquivo_estrato.write(f"{'EXTRATO':^50}\n")
    arquivo_estrato.write(f"{username:^50}\n")
    for i, (usuario, hora, relatorio) in enumerate(estrato):
        arquivo_estrato.write(f"{relatorio} {hora} \n")
    conn.close()


def Cadastro_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return "\033[91mNome de usuário já existe. Por favor, escolha outro.\033[0m"
    elif username == password:
        return "\033[91mUsuario e senhas iguais, tente novamente\033[0m"
    elif username != '' and password != "":
        cursor.execute("INSERT INTO usuarios (username, password, saldo) VALUES (?, ?, ?)", (username, password, 0))
        conn.commit()
        return "\033[92mCadastro realizado com sucesso!\033[0m"
    else:
        return "\033[91mUsuário ou senha vazio\033[0m"


def Login_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return user
    else:
        return None


def horario():
    hora = datetime.now()
    hora = hora.strftime("%d/%m/%Y %H:%M")
    return hora

def opcoes_banco(username, saldo):
    while True:
        print("=" * 33)
        print("\033[94mDIGITE A OPERAÇÃO DESEJADA\033[0m")
        print("\033[94m1) Consultar saldo\033[0m")
        print("\033[94m2) Saque\033[0m")
        print("\033[94m3) Depositar\033[0m")
        print("\033[94m4) Deletar conta\033[0m")
        print("\033[94m5) Pesquisar conta\033[0m")
        print("\033[94m0) Encerrar sessão\033[0m")
        print("=" * 33)
        opc1 = input()
        if opc1 == "1":
            print("Seu saldo é de R$", saldo)
        elif opc1 == "2":
            try:
                saque = float(input("Qual valor você deseja sacar? "))
                
            except ValueError:
                print("\033[91mDigite um valor válido\033[0m")
            else:
                if saldo < saque:
                    print("\033[91mValor insuficiente\033[0m")
                else:
                    saldo -= saque
                    cursor.execute("UPDATE usuarios SET saldo = ? WHERE username = ?", (saldo, username))
                    conn.commit()
                    relato_saque = f"Saque de R$ {saque:.2f} realizado com sucesso."
                    print("\033[92m" + relato_saque + "\033[0m")
                    estrato.append([username, relato_saque, horario()])
            
        elif opc1 == "3":
            try:
                deposito = float(input("Qual valor que deseja depositar? "))
            except ValueError:
                print("\033[91mDigite um valor válido\033[0m")
            else:
                saldo += deposito
                cursor.execute("UPDATE usuarios SET saldo = ? WHERE username = ?", (saldo, username))
                conn.commit()
                relato_deposito = f"Depósito de R$ {deposito} realizado."
                print("\033[92m" + relato_deposito + "\033[0m")
                estrato.append([username, relato_deposito, horario()])
        elif opc1 == "4":
            deletar_conta = input("Deseja deletar sua conta? (S/N)")
            if deletar_conta.lower() == "s":
                cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
                conn.commit()
                print("\033[92mConta deletada.\033[0m")
                return
        elif opc1 == '5':
            pesquisa = input("digite nome do usuário ")
            cursor.execute("SELECT username FROM usuarios WHERE username= ?", (pesquisa,))
            pesquisa = cursor.fetchone()
            if pesquisa:
                print("\033[92mUsuário {} encontrado\033[0m".format(pesquisa[0]))
            else:
                print("\033[91mNão encontrado\033[0m")
        elif opc1 == "0":
            print("\033[92mEncerrando sessão...\033[0m")
            return
        else:
            print("\033[91mOpção inválida.\033[0m")


while True:
    print("=" * 33)
    print("\033[94m1. Cadastrar\033[0m")
    print("\033[94m2. Login\033[0m")
    print("\033[94m3. Sair\033[0m")
    print("=" * 33)

    opc = input("Escolha uma opção: ")

    if opc == "1":
        username = input("Digite um nome de usuário: ")
        password = pwinput.pwinput("Digite uma senha: ", mask="*")
        print(Cadastro_usuario(username, password))
    elif opc == "2":
        username = input("Digite seu nome de usuário: ")
        password = pwinput.pwinput("Digite sua senha: ", mask="*")
        user = Login_usuario(username, password)
        if user:
            print("\033[92mLogin bem-sucedido!\033[0m")
            opcoes_banco(username, user[2])  # Passa o username e o saldo do usuário
        else:
            print("\033[91mNome de usuário ou senha incorretos. Tente novamente.\033[0m")
    elif opc == "3":
        print("\033[92mSaindo...\033[0m")
        break
    else:
        print("\033[91mOpção inválida. Por favor, escolha novamente.\033[0m")

extrato()
