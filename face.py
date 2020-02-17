"""
   *Face Tracking System Using Arduino - Python Code*
    Close the Arduino IDE before running this code to avoid Serial conflicts.
    Replace 'COM5' with the name of port where you arduino is connected.
    To find the port check Arduino IDE >> Tools >> port.
    Upload the Arduino code before executing this code.

"""
from serial import Serial
import time
import cv2
import numpy as np

#ser = serial.Serial('COM4', 9600, timeout=5)
#time.sleep(2)
#print("Connection to arduino...")

gamma=100

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

def empty(a):
    pass

# This will send data to the arduino according to the x coordinate
def angle_servox(angle):

    if angle>60:
        prov=2
        #ser.write(b'2')
        print("Right")


    elif angle<40:
        prov=1
        #ser.write(b'1')
        print("Left")

    elif angle>40 and angle<60:
        #ser.write(b'0')
        print("Stop")
# This will send data to the arduino according to the y coordinate
def angle_servoy(angle):

    if angle>60:
        prov=3
        #ser.write(b'3')
        print("Down")


    elif angle<40:
        prov=4
        #ser.write(b'4')
        print("Up")

    elif angle>40 and angle<60:
        #ser.write(b'5')
        print("Stop")

print("-> Loading the detector...")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("-> Starting Video Stream")
cap = cv2.VideoCapture(0)
cv2.namedWindow("img")
cv2.resizeWindow("img",640,480)
cv2.createTrackbar("gammacorec","img",gamma,250,empty)
while 1:
    ret, img = cap.read()
    if ret == False:
        print('Failed to capture frame from camera. Check camera index in cv2.VideoCapture(0) \n')
        cv2.destroyAllWindows()
        break
    gamma = 0.01*(cv2.getTrackbarPos('gammacorec', 'img'))
    adjusted = adjust_gamma(img, gamma=gamma)
    #cv2.line(img,(600,250),(0,250),(0,255,0),1) (B,G,R)
    gray  = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(adjusted,(x,y),(x+w,y+h),(0,255,0),5)
        #cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.circle(adjusted, (x, y), 5, (0, 0, 0), -1)
        cv2.circle(adjusted, (x+h, y+w), 5, (255, 0, 0), -1)
        # Center of roi (Rectangle)
        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2
        center = (xx,yy)
        a=int(xx)
        b=int(yy)
        cv2.circle(adjusted, (a, b), 5, (0, 0, 255), -1)
        print ("center is:")
        print(center)
        angle_servox(xx)
        angle_servoy(yy)
        
    cv2.imshow('img',adjusted)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print("-> Ending Video Stream")
        cap.release()
        cv2.destroyAllWindows()
        break
