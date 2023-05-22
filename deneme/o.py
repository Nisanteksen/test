import cv2
import numpy as np

# Videonun okunması
video = cv2.VideoCapture("rick.mp4")

# Video boyutlarının alınması
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Yeni video oluşturulması
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("combined_video.mp4", fourcc, 30.0, (2*width, 2*height))

# Döngü ile video işleme
while True:
    ret, frame = video.read()
    if not ret:
        break

    # Keskinleştirilmiş video oluşturma
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(frame, -1, kernel)

    # Mavi renkle maskelenmiş video oluşturma
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,60,60])
    upper_blue = np.array([130,255,255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_mask = cv2.bitwise_not(blue_mask)
    blue_masked = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Kırmızı renkle maskelenmiş video oluşturma
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    red_mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    red_mask2 = cv2.inRange(hsv, lower_red, upper_red)
    red_mask = red_mask1 + red_mask2
    red_mask = cv2.bitwise_not(red_mask)
    red_masked = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Orijinal video
    original = frame

    # Video birleştirme
    top_row = np.concatenate((sharpened, blue_masked), axis=1)
    bottom_row = np.concatenate((red_masked, original), axis=1)
    combined = np.concatenate((top_row, bottom_row), axis=0)

    # Video kaydetme
    out.write(combined)

    # Pencere gösterimi
    cv2.imshow("Combined Video", combined)

    # Çıkış için q tuşuna basın
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırakın ve çıkış yapın
video.release()
out.release()
cv2.destroyAllWindows()