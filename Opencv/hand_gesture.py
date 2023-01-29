import numpy as np
import cv2
import pyautogui

cv2.useOptimized()
hand_cas = cv2.CascadeClassifier("palm.xml")
cap = cv2.VideoCapture(0)
scr_w,scr_h = pyautogui.size()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, scr_w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, scr_h)

while True:
    ret,frame = cap.read()
    img_size = frame.shape
    # print(img_size)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,1)
    hand = hand_cas.detectMultiScale(frame,scaleFactor=1.05,minNeighbors=5)
    for x,y,w,h in hand:
        pyautogui.moveTo(x+w//2,y+h//2, duration = 0.1) 
        # frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),3)
    # print(frame.shape)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



# img = cv2.imread("hands.jpg")
# hand = hand_cas.detectMultiScale(img,scaleFactor=1.01,minNeighbors=2)
# for x,y,w,h in hand:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),3)
# cv2.imshow("image",img)
# cv2.waitKey(0)
