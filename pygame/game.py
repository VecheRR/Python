import pygame
import math
import numpy as np
import cv2
import face_recognition

cap = cv2.VideoCapture(0)
face_locations = []

while(True):
    ret, frame = cap.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(len(face_locations))

    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
