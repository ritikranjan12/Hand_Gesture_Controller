import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode=False,max_hands=2,model_complexity=1,detection_confidence=0.7,tracking_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.model_complexity = model_complexity
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.max_hands,self.model_complexity,self.detection_confidence,self.tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLand, self.mpHands.HAND_CONNECTIONS)
        return img


    def findPosition(self,img, handNo=0,draw=True):

        lm = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, ln in enumerate(myHand.landmark):
                # print(id,ln)
                h, w, c = img.shape
                cx, cy = int(ln.x * w), int(ln.y * h)
                lm.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 2, (255, 0, 0), cv2.FILLED)
        return lm
def main():
    ptime = 0
    ctime = 0
    detector = handDetector()
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

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()
