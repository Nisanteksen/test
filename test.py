import cv2
import numpy as np

# video yükleyelim
video = cv2.VideoCapture(r"C:\Users\NisanSenaTEKŞEN\Downloads\rick-and-morty-theme-song-hd.mp4")
ret, frame = video.read()

# video kaydedicisi oluşturalım
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('merged_video.mp4', fourcc, 20.0, (frame.shape[1]*3, frame.shape[0]))

while video.isOpened():
    ret, frame = video.read()
    if ret:
        kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
        sharpened= cv2.filter2D(frame, -1, kernel)

        # mavi ve kırmızı maske videoları oluşturalım
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        enazmavi = np.array([100,60,60])
        encokmavi = np.array([130,255,255])
        enazred = np.array([0,50,50])
        encokred = np.array([10,255,255])
        maskered = cv2.inRange(hsv,enazred,encokred)
        maskemavi = cv2.inRange(hsv,enazmavi,encokmavi)
        
        # videoları birleştirelim
        merged_video = cv2.merge([maskemavi, maskered, frame])
        merged_video = cv2.resize(merged_video, (frame.shape[1]*3, frame.shape[0]))

        # videoları tek bir pencerede gösterelim
        cv2.imshow('merged', merged_video)

    if cv2.waitKey(25) & 0xFF == ord('c'):
        break

video.release()
out.release()
cv2.destroyAllWindows()