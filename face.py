"""
    Close the Arduino IDE before running this code to avoid Serial conflicts.
    Replace 'COM5' with the name of port where you arduino is connected.
    To find the port check Arduino IDE >> Tools >> port.
    Upload the Arduino code before executing this code.
    Keep the file 'haarcascade_frontalface_default.xml' in the same folder as the program

"""
from serial import Serial
import numpy as np
import serial
import time
import sys
import cv2

ser = serial.Serial('COM4', 9600, timeout=5)
time.sleep(2)
print("Connection to arduino...")

# This will send data to the arduino according to the x coordinate
def angle_servox(angle):

    if angle>60:
        prov=2
        ser.write(b'2')
        print("Right")


    elif angle<40:
        prov=1
        ser.write(b'1')
        print("Left")

    elif angle>40 and angle<60:
        ser.write(b'0')
        print("Stop")
# This will send data to the arduino according to the y coordinate
def angle_servoy(angle):

    if angle>60:
        prov=3
        ser.write(b'3')
        print("Down")


    elif angle<40:
        prov=4
        ser.write(b'4')
        print("Up")

    elif angle>40 and angle<60:
        ser.write(b'5')
        print("Stop")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) #change the no. to change the source of the image/video

while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 600,500)
    #cv2.line(img,(600,250),(0,250),(0,255,0),1)#horizontal line
    #cv2.line(img,(300,0),(300,500),(0,255,0),1)#vertical line
    #cv2.circle(img, (300, 250), 5, (255, 255, 255), -1) #dot at center
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y:y+h, x:x+w}
       #print (arr)
        

        angle_servox(x)
        angle_servoy(y)

      #this is very helpful for calibrating servomotors
        print(x)
        print(y)
    

    cv2.imshow('img',img)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

