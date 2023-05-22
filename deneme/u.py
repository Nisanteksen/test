import cv2

# Videoların yollarını tanımla
video1_path = "video1.mp4"
video2_path = "video2.mp4"
video3_path = "video3.mp4"
video4_path = "video4.mp4"

# Videoları oku
video1 = cv2.VideoCapture(video1_path)
video2 = cv2.VideoCapture(video2_path)
video3 = cv2.VideoCapture(video3_path)
video4 = cv2.VideoCapture(video4_path)

# Videoların boyutunu al
width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Yeni bir pencere için boyutlar oluştur
window_width = width * 2
window_height = height * 2

# Video yazıcıyı tanımla
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('merged_video.mp4', fourcc, 20.0, (window_width, window_height))

while True:
    # Tüm videoların bir sonraki karesini oku
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    ret3, frame3 = video3.read()
    ret4, frame4 = video4.read()

    # Eğer herhangi bir video bitmişse döngüden çık
    if not ret1 or not ret2 or not ret3 or not ret4:
        break

    # Videoları birleştir
    top_row = cv2.hconcat([frame1, frame2])
    bottom_row = cv2.hconcat([frame3, frame4])
    merged = cv2.vconcat([top_row, bottom_row])

    # Birleştirilmiş videoyu yazdır
    out.write(merged)

    # Pencereyi göster
    cv2.imshow("Merged Video", merged)

    # Q tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tüm pencereleri kapat
cv2.destroyAllWindows()

# Video kaydediciyi ve videoları serbest bırak
out.release()
video1.release()
video2.release()
video3.release()
video4.release()