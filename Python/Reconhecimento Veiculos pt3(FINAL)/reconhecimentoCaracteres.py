#importação de blibliotecas
from email.mime import image
from tkinter import image_names
import pytesseract
import cv2

#criar uma função
def reconhecer(imagem):
    pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe" 
    placalida = cv2.imread('placa1.jpg',0)

    # cv2.imshow("placa",placalida)
    # cv2.waitKey(0)
    texto =  pytesseract.image_to_string(imagem, config='-l eng --oem 3 --psm 6')

    print(texto)
 
    return texto

# reconhecer('placa1.jpg')
