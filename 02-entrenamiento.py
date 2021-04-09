import cv2
#from cv2 import EigenFaceRecognizer
import os
import numpy as np 
import imutils
from PIL import Image


dataPath = 'E:/autoestudio\ComputerVision y MachineLearning Python/InterfacesProyectoFinal_UAO/graficos/Fase01_ProyectoFinal/Data'

peopleList = os.listdir(dataPath)

print('Lista de personas: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Leyendo las imagenes')

    for fileName in os.listdir(personPath):
        print('Rostros: ',nameDir+'/'+fileName)
        labels.append(label)
        # Conviernte en escalade grises : 
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
    label = label + 1

print('Labels= ',labels)

#print('Numero de etiquetas 0:',np.count_nonzero(np.array(labels)==0))

#print(cv2.__version__ )
face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.EigenFaceRecognizer_reate()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()

#face_recognizer = cv2.face.E
#print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))
face_recognizer.write('modeloEigenFace.xml')
print("Modelo almacenado...")