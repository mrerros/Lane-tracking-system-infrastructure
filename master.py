import cv2
import numpy as np

# Video dosyası ya da kamera akışı için VideoCapture oluştur
cap = cv2.VideoCapture('video.mp4')  # Kamerayı kullanmak için 0, video dosyası için dosya adı

while True:
    # Kameradan bir çerçeve al
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü BGR'den HSV'ye dönüştürme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Beyaz rengi tanımlama (HSV formatında)
    lower_white = np.array([0, 0, 200])  # Alt sınırlar
    upper_white = np.array([255, 30, 255])  # Üst sınırlar
    # Maskeleme yapma
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Maske üzerinde kontur bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Konturun alanını hesapla
        area = cv2.contourArea(contour)
        if area > 100:  # Minimum alanı belirle
            # Konturun dış dikdörtgenini bulma
            x, y, w, h = cv2.boundingRect(contour)
            # Algılanan beyaz şeridi yeşil olarak gösterme
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    # Sonuçları ekranda gösterme
    cv2.imshow('Frame', frame)
    cv2.imshow('Masked Frame', mask)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama nesnesini ve pencereleri serbest bırakma
cap.release()
cv2.destroyAllWindows()
