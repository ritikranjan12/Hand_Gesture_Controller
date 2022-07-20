import cv2
import mediapipe as mp
import time
import handtrackingmodule as htm

# Hand Detection Model has 21 points or landmark that it detects on our hand


ptime = 0
ctime = 0
detector = htm.handDetector()
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = detector.findHands(img,True)
    ln = detector.findPosition(img)
    if len(ln) != 0:
       print(ln[4])
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)