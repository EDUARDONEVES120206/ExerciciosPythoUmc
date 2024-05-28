import cv2

#criar uma variavel para capturar o video ou a camera
 
#leitaura do video
camera = cv2.VideoCapture('videoJoSoares.mp4')

#leitra da camera
# camera = cv2.VideoCapture(0)


while True:
    
    sucesso, frame = camera.read()
    cv2.imshow("meu video",frame)


    if cv2.waitKey(1) & 0xFF == ord("s"):
        break



camera.release()
cv2.destroyAllWindows()