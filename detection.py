# -*- coding: utf-8 -*-
"""Copy of Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DEdBmsqD-om4t89-9y19047bVI3NgIEK
"""

import cv2
import numpy as np
import time
#from google.colab.patches import cv2_imshow

videosPath = '/content/drive/MyDrive/videos/AVSS_E2.avi'
cap = cv2.VideoCapture(videosPath)
whT = 320
confThreshold = 0.5
nmsThreshold = 0.3

classesFile ="model/coco3.names";
classNames = []
with open(classesFile,"rt") as f:
    classNames =  [line.strip() for line in f.readlines()]
#print(classNames)
#print(len(classNames))

modelConfiguration = "model/yolov4n.cfg";
modelWeights = "model/yolov4n.weights";

net = cv2.dnn.readNet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObjects(outputs,img):
    
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold and classId in(1,2):
                w,h = int(det[2]* wT), int(det[3]*hT)
                x,y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))


    #print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs,confThreshold,nmsThreshold)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x,y,w,h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img,f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',
                    (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,0,255),2)

    

def baggage(cap):
    
    while True:
        img = cap

        blob = cv2.dnn.blobFromImage(img, 1/255,(whT,whT),[0,0,0],crop=False)
        net.setInput(blob)

        layerNames = net.getLayerNames()
        outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]

        outputs = net.forward(outputNames)
        findObjects(outputs,img)
       
        return img
        #cv2.imshow('Image', img)
        #cv2.waitKey(1)
    
        
