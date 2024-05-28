
import sys
from PyQt6.QtWidgets import *
import informacoes
import reconhecimentoCaracteres
import cv2

# print(informacoes.dadosVeiculos())

# C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR

dadosPessoais = informacoes.dadosVeiculos()

def verificar():
    verificacao = reconhecimentoCaracteres.reconhecer('placa1.jpg')
    print(verificacao)

def abrirCamera():
    camera = cv2.VideoCapture(0)

    while True:
    
        Sucesso, frame = camera.read()
        cv2.imshow("imagem",frame)
        cv2.imwrite('placa1.png',frame)

        #utilizar o arquivo de reconhecimento
        placaReconhecida = reconhecimentoCaracteres.reconhecer('placa1.png')
        for p in dadosPessoais:
            if p in placaReconhecida:
                print(dadosPessoais[p][0])
                inputNome.setText(dadosPessoais[p][0])
                inputModelo.setText(dadosPessoais[p][1])
                inputPlaca.setText(p)
                inputCor.setText(dadosPessoais[p][2])
                nomeTextoImagem = (dadosPessoais[p][3])
                foto = cv2.imread(nomeTextoImagem, 0)
                cv2.imshow('foto',foto)
                
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

    camera.release()
    cv2.destroyAllWindows()




#construir interface
dimensaobotao = 60
app = QApplication(sys.argv)
janela = QWidget() # Cria uma janela 
janela.resize(600,500)
janela.setWindowTitle(' Monitoramento Veicular ') # define um titulo para a janela 


with open('style.css','r') as style_file:
    styles = style_file.read()

janela.setStyleSheet(styles)

inputNome = QLineEdit('',janela)
inputNome.resize(270,40)
inputNome.move(280,120)
# inputNome.setReadOnly(True)

inputModelo = QLineEdit('',janela)
inputModelo.resize(270,40)
inputModelo.move(280,200)
# inputModelo.setReadOnly(True)

inputPlaca = QLineEdit('',janela)
inputPlaca.resize(270,40)
inputPlaca.move(280,280)
# inputPlaca.setReadOnly(True)

inputCor = QLineEdit('',janela)
inputCor.resize(270,40)
inputCor.move(280,360)
# inputCor.setReadOnly(True)

titulo = QLabel('Monitoramento Veicular',janela)
titulo.setObjectName('MonitoramentoVeicular')
titulo.move(155,45)

nome = QLabel('Nome',janela)
nome.setObjectName('nome')
nome.move(108,120)

model = QLabel('Modelo',janela)
model.setObjectName('modelo')
model.move(105,200)

placa = QLabel('Placa',janela)
placa.setObjectName('placa')
placa.move(115,280)

cor = QLabel('Cor',janela)
cor.setObjectName('cor')
cor.move(122,360)

botaoVerificar = QPushButton('Verificar',janela)
botaoVerificar.setGeometry(225,415,150,60 )
# botaoVerificar.setObjectName('verificar')
botaoVerificar.clicked.connect(abrirCamera)



janela.show()
sys.exit ((app.exec()))













