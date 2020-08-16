
import cv2
cameraNumber=0


fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
cap = cv2.VideoCapture()
cap.open(cameraNumber + 1 + cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FOURCC, fourcc)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 60)