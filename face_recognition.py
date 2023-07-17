#import module
import cv2

#setting camera　 device ID is 0
cap = cv2.VideoCapture(0)

#update imgae
while True:
    #get image from camera
    ret, frame = cap.read()
    img=frame
    
    #change grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #import Cascade
    cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #detect faces
    face=cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
    print("Face coordinates↓")
    print(face)

    #make frames
    for x,y,w,h in face:#repeat some face
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)#frame the faces


    #peint picture
    cv2.imshow('' , img)

    #break out update with Esc
    key =cv2.waitKey(10)
    if key == 27:
        break

#exit command
cap.release()
cv2.destroyAllWindows()
