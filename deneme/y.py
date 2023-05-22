import cv2
import numpy as np

# Videonun yüklenmesi
video = cv2.VideoCapture("rick.mp4")



# Video boyutlarının alınması
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 2x2 çerçeve boyutlarının oluşturulması
grid_width = frame_width * 2
grid_height = frame_height * 2

# 2x2 çerçevenin oluşturulması
grid = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)

# Video frame'lerinin okunması
while True:
    ret, frame = video.read()
    if not ret:
        break
    
    # Mavi renk maskesi
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([100,60,60])
    blue_upper = np.array([130,255,255])
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    blue_masked = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Kırmızı renk maskesi
    red_lower = np.array([0,50,50])
    red_upper = np.array([10,255,255])
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    red_masked = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Keskinleştirme
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(frame, -1, kernel)

    # 2x2 çerçeveye frame'lerin yerleştirilmesi
    grid[0:frame_height, 0:frame_width] = frame
    grid[0:frame_height, frame_width:grid_width] = sharpened
    grid[frame_height:grid_height, 0:frame_width] = blue_masked
    grid[frame_height:grid_height, frame_width:grid_width] = red_masked

    # Çerçevenin gösterilmesi
    cv2.imshow("4 Videos in 2x2 Grid", grid)

    if cv2.waitKey(1) == ord("q"):
        break

# Temizleme
video.release()
cv2.destroyAllWindows()