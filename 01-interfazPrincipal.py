from tkinter import *

# --- Video

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sqlite3

# Abrir cuadro de  dialogo para escoger el video de entrada

from PIL import Image
from PIL import ImageTk

import cv2
import imutils

import os

# --- Fin 



root = Tk()


root.title("Perfilizador")
root.iconbitmap('icono.ico')

mainFrame = Frame(root,width=800,height=800)
mainFrame.pack()


# ---- Generar Frames

def validar_id_bd(datoCedula,datoNombre,datoApellidos):

    conn_local = sqlite3.connect("BD_TargetPerson.sqlite3")
    conn_cursor_local = conn_local.cursor()
    conn_cursor_local.execute("select * from Tbl_TargetPerson where CEDULA={0}".format(datoCedula))

    cantidad_registros =  len(conn_cursor_local.fetchall())

    if cantidad_registros > 0:
        #messagebox.showwarning(title="Alerta!!!", message="La persona ya existe en la BD, no es posible porcesarla")
        conn_local.close()
        validar = 1
    else:
        conn_local.close()
        conn_local = sqlite3.connect("BD_TargetPerson.sqlite3")
        conn_cursor_local = conn_local.cursor()
        conn_cursor_local.execute("INSERT INTO Tbl_TargetPerson VALUES(?,?,?)",(datoCedula,datoNombre,datoApellidos))
        conn_local.commit()
        conn_local.close()
        validar = 0
    return validar







def generarFrames():

    datoCedula = varCedula.get()
    datoNombre = varNombre.get()
    datoApellidos = varApellidos.get()
    #print(varCedula.get())
    pathVideo = lblInfoVideoPath.cget("text")
    #print(pathVideo)

    if datoCedula=="" or datoNombre=="" or datoApellidos=="" or pathVideo=="Aun no se ha seleccionado un video":
        #print("Todos los campos son obligatorios!!!")
        messagebox.showwarning(title="Alerta!!!", message="Todos los campos son obligatorios!!!")
    
    else:

        res_validar = validar_id_bd(datoCedula,datoNombre,datoApellidos)

        if res_validar==1:
            messagebox.showwarning(title="Alerta!!!", message="La persona ya existe!!!")

        else:

            wd = os.getcwd()
            #print("working directory is ", wd)

            #personName = 'Gerardo'
            personName = datoCedula+'-'+datoNombre
            #dataPath = 'E:/autoestudio/ComputerVision y MachineLearning Python/Archive/Data'
            dataPath = wd+'/Data'
            
            personPath = dataPath + '/' + personName

            #print("El personPath  es: ",personPath)
            

            if not os.path.exists(personPath):
                #print('Carpeta creada: ',personPath)
                os.makedirs(personPath)

            # # Video donde se tomaran los rostros

            cap = cv2.VideoCapture(pathVideo)

            faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
            count = 0


            while True:
                ret , frame = cap.read()
                if ret == False: break
                frame = imutils.resize(frame, width=640)
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                auxFrame = frame.copy()

                faces = faceClassif.detectMultiScale(gray,1.3,5)

                for(x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0.255,0),2)
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(personPath+'/rostro_{}.jpg'.format(count),rostro)
                    count = count + 1
                cv2.imshow('frame',frame)

                k = cv2.waitKey(1)
                if k == 27 or count >= 500:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showwarning(title="Mensaje", message="Video Procesado Correctamente")


#def cargarVideo():
#    print("Se va a cargar el video")


# --- Cargar Video

def cargarVideo():
    global cap

    #if cap is not None:
    #    lblVideo.image = ''
    #    cap.release()
    #    cap = None

    video_path = filedialog.askopenfilename(filetypes = [
        ('all video format','.mp4'),
        ('all video format','.avi')])
    #print(video_path)
    #if len(video_path)> 0:
    lblInfoVideoPath.configure(text=video_path)
     #   cap = cv2.VideoCapture(video_path)
     #   visualizar()
    #else:
    #    lblInfoVideoPath.configure(text='Aun no se ha seleccionado un video')


cap = None



# ---- Definición de Variables

varCedula=StringVar()
varNombre=StringVar()
varApellidos=StringVar()


# ---- Definición de Labels:

nlbtTitle = Label(mainFrame,text="Perfilizador de Targets",font=("Comic Sans MS",18))
nlbtTitle.grid(row=0,column=0,sticky='e',pady=20,padx=20,columnspan=3)

cedulaLabel = Label(mainFrame,text="Id: ")
cedulaLabel.grid(row=1,column=0,sticky='e',pady=10,padx=0)

nombreLabel = Label(mainFrame,text="Nombres: ")
nombreLabel.grid(row=2,column=0,sticky='e',pady=10,padx=0)

apellidosLabel = Label(mainFrame,text="Apellidos: ")
apellidosLabel.grid(row=3,column=0,sticky='e',pady=10,padx=0)

lblInfoVideoPath = Label(mainFrame, text='Aun no se ha seleccionado un video')
lblInfoVideoPath.grid(row=5,column=0,columnspan=3)



# ---- Definición de Text:

cuadroCedula = Entry(mainFrame,textvariable=varCedula)
cuadroCedula.grid(row=1,column=1,pady=10,padx=0)

cuadroNombre = Entry(mainFrame,textvariable=varNombre)
cuadroNombre.grid(row=2,column=1,pady=10,padx=0)

cuadroApellidos = Entry(mainFrame,textvariable=varApellidos)
cuadroApellidos.grid(row=3,column=1,pady=10,padx=0)


btnCargarVideo = Button(mainFrame,text="Cargar video",width=30,command=cargarVideo)
btnCargarVideo.grid(row=4,column=0,columnspan=3)

btnGenerarFrames = Button(mainFrame,text="Generar Frames",width=30,command=generarFrames)
btnGenerarFrames.grid(row=6,column=0,columnspan=3,pady=20)


root.mainloop()