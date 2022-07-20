import handtrackingmodule as hm
import cv2
import time
import numpy as np
import math
import pyautogui

ptime = 0

wcam , hcam = 640,480
detector = hm.handDetector()
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
while True:
    success, img = cap.read()
    img = detector.findHands(img, True)
    ln = detector.findPosition(img,draw=False)
    if len(ln) != 0:
        x1,y1 = ln[4][1] ,ln[4][2]
        x2,y2 = ln[8][1] ,ln[8][2]

        cx,cy = (x1+x2)//2 , (y1+y2)//2

        cv2.circle(img,(x1,y1),5,(255,0,0),cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,255,255),2)

        length = math.hypot(x2-x1,y2-y1)
        if length < 59 :
            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 5, (255, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (255, 255, 0), cv2.FILLED)
            pyautogui.press("volumedown",15,0.00001)
        if length > 60:
            pyautogui.press("volumeup",5,0.00001)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, "FPS : " + str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
