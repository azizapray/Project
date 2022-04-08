from cv2 import VideoWriter
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

delay=60
frameTime= 1

cap = cv2.VideoCapture('atc.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')
classifier =load_model(r'C:\Users\Sandika\Desktop\DATA SCIENCE\PHASE_2\MILESTONE 2 DATASET\final project\model_vehicle_v4.h5')
vehicle_labels = ['bike', 'bus', 'car', 'truck']
frameTime = 100

while True:
    _, frame = cap.read()
    labels = []
    cars = car_cascade.detectMultiScale(frame, 1.15, 4)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray = frame[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(224,224),interpolation=cv2.INTER_AREA)
        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=vehicle_labels[prediction.argmax()]
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
             cv2.putText(frame,'UFO',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Vehicle Detector',frame)
 
    if cv2.waitKey(frameTime) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()