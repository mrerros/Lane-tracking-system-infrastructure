import cv2
import numpy as np


cap = cv2.VideoCapture('video.mp4')  

while True:
   
    ret, frame = cap.read()
    if not ret:
        break

  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   
    lower_white = np.array([0, 0, 200])  # Alt sınırlar
    upper_white = np.array([255, 30, 255])  # Üst sınırlar
    
    mask = cv2.inRange(hsv, lower_white, upper_white)

    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        
        area = cv2.contourArea(contour)
        if area > 100:  
            
            x, y, w, h = cv2.boundingRect(contour)
           
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

   
    cv2.imshow('Frame', frame)
    cv2.imshow('Masked Frame', mask)

  
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Video yakalama nesnesini ve pencereleri serbest bırakma
cap.release()
cv2.destroyAllWindows()
