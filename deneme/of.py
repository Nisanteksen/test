import cv2
import numpy as np
# Videoyu yükleyin
video = cv2.VideoCapture("rick.mp4")

# Keskinleştirilmiş videoyu oluşturun
sharp_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
while True:
    ret, frame = video.read()
    if not ret:
        break
    sharp_frame = cv2.filter2D(frame, -1, sharp_kernel)
    cv2.imshow("Sharp Video", sharp_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Mavi alanları beyaz, diğerlerini siyah yaparak videoyu işleyin
blue_thresh = 100
while True:
    ret, frame = video.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, blue_thresh, blue_thresh])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_frame = cv2.bitwise_and(frame, frame, mask=mask)
    gray = cv2.cvtColor(blue_frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow("Blue Video", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kırmızı alanları beyaz, diğerlerini siyah yaparak videoyu işleyin
red_thresh = 100
while True:
    ret, frame = video.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, red_thresh, red_thresh])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, red_thresh, red_thresh])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.bitwise_or(mask1, mask2)
    red_frame = cv2.bitwise_and(frame, frame, mask=mask)
    gray = cv2.cvtColor(red_frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow("Red Video", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Orijinal videoyu göster
video = cv2.VideoCapture("video.mp4")
while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Original Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()