import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_found(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if faces is():
        return False
    
    for(x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        
    return face


cap = cv2.VideoCapture(0)
count = 0

if not cap.isOpened():
    print("Could not open webcam")
    exit()


while cap.isOpened():
    ret, frame = cap.read()
    
    if face_found(frame) is not False:
        count+=1
        
        face = cv2.resize(face_found(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
        file_name_path = 'faces/user'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)
        
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Find',face)
        
    else:
        print("Face not Found")
        pass

    if cv2.waitKey(1) & count == 100:
        break

cap.release()
cv2.destroyAllWindows()
print('Sampling complete!')
