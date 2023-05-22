#import RPi.GPIO
import cv2
import  numpy
import time
import A

kamera=cv2.VideoCapture(0)
A.GPIOset()
enaz=numpy.array([0,50,50])
encok=numpy.array([10,255,255])

while(kamera.isOpened()):
    ret,video=kamera.read()
    hsv=cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
    maske=cv2.inRange(hsv,enaz,encok)
    pikselsayisi = cv2.countNonZero(maske)
    if pikselsayisi > 1000:
        A.GPIOexe()
    cv2.imshow("maske video",maske)
    if cv2.waitKey(1)== ord('c'):
        break
    
kamera.release()
cv2.destroyAllWindows()
