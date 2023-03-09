import cv2
import numpy as np
import pyautogui

# Ekran çözünürlüğü
screen_size = (1920, 1080)

# Video kaydedici için codec ve FPS değerleri
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
fps = 20.0

# Video dosyasını oluştur
out = cv2.VideoWriter("kayit.avi", fourcc, fps, screen_size)

# Ana döngü
while True:
    # Ekran görüntüsü al
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Renk uzayı dönüştürülür
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Video dosyasına ekle
    out.write(frame)

    # "q" tuşuna basılınca kaydı durdur
    if cv2.waitKey(1) == ord("q"):
        break

# Video dosyasını kapat
out.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()
