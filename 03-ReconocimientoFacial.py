import cv2
import os
import numpy as np
from subprocess import check_output

dataPath = 'E:/autoestudio/ComputerVision y MachineLearning Python/InterfacesProyectoFinal_UAO/graficos/Fase01_ProyectoFinal/Data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)
face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# Leyendo el modelo
face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
#face_recognizer.read('modeloLBPHFace.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture('DemostracionDeteccion.mp4')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
listaReconocidos = []
while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)

    
    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        
        # EigenFaces
        if result[1] < 5700:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            listaReconocidos.append(imagePaths[result[0]])
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        '''
        # FisherFace
        if result[1] < 500:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        # LBPHFace
        if result[1] < 70:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        '''
    
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

listaReconocidos = np.array(listaReconocidos)
listaReconocidos = np.unique(listaReconocidos)


print('Persona reconocida',listaReconocidos)

for i in range(len(listaReconocidos)):
    if listaReconocidos[i]=='1-Jose':
        #comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"text=Alerta!!! Persona detectada: José Alfredo Torres\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendMessage\""
        comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"text=Alerta!!! Persona detectada: Jose Alfredo Torres\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendMessage\""
        check_output(comando, shell=True)
    
        #imageFile='https://i.ibb.co/SmqdK2p/Jose-Torres-Mask.png'
        #!curl -k -L --data chat_id=-529659222 --data-urlencode "photo=$imageFile" "https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendPhoto"
        comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"photo=https://i.ibb.co/SmqdK2p/Jose-Torres-Mask.png\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendPhoto\""
        check_output(comando, shell=True)
    if listaReconocidos[i]=='2-Camilo':
        comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"text=Alerta!!! Persona detectada: Juan Camilo Arenas\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendMessage\""
        check_output(comando, shell=True)
        
        #imageFile2='https://i.ibb.co/zSpfJXF/Juan-Camilo.png'
        comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"photo=https://i.ibb.co/yYHK4Qh/Juan-Camilo-Mask.png\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendPhoto\""
        check_output(comando, shell=True)


    if listaReconocidos[i]=='3-Gerardo':
        comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"text=Alerta!!! Persona detectada: Gerardo Castro Tamayo\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendMessage\""
        check_output(comando, shell=True)
    
        #imageFile2='https://i.ibb.co/FxBJW0C/GerardoC.png'
        comando = "curl -k -L --data chat_id=-529659222 --data-urlencode \"photo=https://i.ibb.co/fvNMKyG/Gerardo-Castro-Mask.png\" \"https://api.telegram.org/bot1684004042:AAHwM3-pZGn4_JUyo2veBveM6WvpuJF1FVw/sendPhoto\""
        check_output(comando, shell=True)

    


cap.release()
cv2.destroyAllWindows()