import  cv2
import numpy as np


img = cv2.imread('D:\Python\ImagenesIA\Messi.jpg')
imagenAux =img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('D:\Python\imagenMessi\haar_faces.xml')

faces_rect =haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
count=0

print(f'Numero de caras encontradas  = {len(faces_rect)}')

for(x,y,w,h)in faces_rect:
    #Se hace un triangulo sobre la cara 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #Seguardan las cordenadas de la cara
    rostro = imagenAux[y:y+h,x:x+w]
    #Se redimenciona la cara  
    rostro =cv2.resize(rostro,(150,150))
    #Seguarda la cara y se cambia el color a gris
    rostro2 = cv2.cvtColor(rostro,cv2.COLOR_BGRA2GRAY)


    cv2.imshow('GRAY',rostro2)
    cv2.imshow('imagen',img)
    cv2.waitKey(0) 

    


 
cv2.destroyAllWindows()

