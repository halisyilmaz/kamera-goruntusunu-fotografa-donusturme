import cv2
from os import path

cap = cv2.VideoCapture(0)   # Programa bilgisayarınızın kamerasını video kaynağı olarak tanıtır
                            # Dahili webcam için 0 veya 1 kullanın. Videolar için 0 olan değeri "dosyanın_yeri/video.mp4"
                            # şeklinde değiştirip videoları da fotoğraf olarak kaydedebilirsiniz
i = 0                       # i en son kaydedilen fotoğrafın numarasını saklar
while True:                 # Daha önceden yapılan dönüştürmeleri kaybetmemek için programın kaldığı yeri bulmasını sağlayan döngü
    if path.exists("fotograflar/goruntu"+ str(i) +".jpg"):
        i += 1
    else:
        break

while True:
    ret, frame = cap.read() # Her döngüde kameradan görüntüyü alır ve frame değişkenine atar

    cv2.imwrite("fotograflar/goruntu"+ str(i) +".jpg",frame) # Kameradan gelen görüntüyü belirtilen adrese kaydeder
    cv2.imshow('Frame',frame)   # Kamera görüntüsünü görmenizi sağlar
    i += 1  # Son kaydedilen fotoğraf numarasını günceller

    if cv2.waitKey(1) & 0XFF == ord('q'):   # "q" tuşuna basınca kayıttan çıkmayı sağlar
        break

cap.release()   # Programı kapatırken kamerayı serbest bırakır ki daha sonra tekrar kamerayı kullanmak istediğimizde
                # kamera kullanımda hatası almayalım
cv2.destroyAllWindows() # Programı kapatır