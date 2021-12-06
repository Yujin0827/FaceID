import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'faces/'

face_data = [f for f in listdir(data_path) if isfile(join(data_path, f))]

Training_Data, Labels = [], []

for i, files in enumerate(face_data):    
    image_path = data_path + face_data[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if images is None:
        continue    
     
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)


if len(Labels) == 0:
    print("no more data.")
    exit()


Labels = np.asarray(Labels, dtype=np.int32)

recognizer = cv2.face.LBPHFaceRecognizer_create() 
recognizer.train(np.asarray(Training_Data), np.asarray(Labels))

print("Training Finish!")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_found(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if faces is():
        return img, []
    
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        face_img = img[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (200, 200))
        
    return img, face_img

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    
    img, face = face_found(frame)
    
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = recognizer.predict(face)
        
        if result[1] < 500:
            confidence = int(100 * (1 - (result[1]) / 300))
            
            display = str(confidence)+'% Confidence it is user'
            
        cv2.putText(img, display, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
       
        if confidence >= 85:
            cv2.putText(img, "!Unlock!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face ID', img)

        else:
            cv2.putText(img, "Lock", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face ID', img)

    except:
        cv2.putText(img, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face ID', img)
        pass
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
