import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    frame = frame[200: int(frame.shape[0]-200), 200:int(frame.shape[1]-200)]
    cv2.imshow("choby zakrut cameru nado nazhat ESC, pomny ob etom!", frame)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()