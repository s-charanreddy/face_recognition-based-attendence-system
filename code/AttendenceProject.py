#importing the required libraries
import cv2
import numpy as np
import face_recognition
import os
from encoding import find_encoding
from AttendenceMarker import mark_attendance
#setting up required data folders

path = "C:\\Users\\charanreddy\\PycharmProjects\\labproject\\ClassMatesImages"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
#iterating over the training images and reading and storing them in list
for cl in myList:
    cumImg = cv2.imread(f'{path}/{cl}')
    images.append(cumImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)

#function to find encoding of the images

encodeListKnown = find_encoding(images)

print('Encoding Complete')


cap = cv2.VideoCapture(0)

#reading input video from the camera
while True:
    success, img = cap.read()
    #resizing the images
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    #conversion form bgr to rgb
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #locating faces in the input image
    facesCurFrame = face_recognition.face_locations(imgS)
    #finding encoding of the images
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    #comparing the input encoding with the already existing data
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        #calculating face distances
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        #checking whether matching or not
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            #resixing to normal scale
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            #drawing rectangles over the input images
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            #putting name of the person
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            #marking attendance with the help of function and name
            mark_attendance(name)

    cv2.imshow('Webcam', img)
    #snippet to quit from taking video input
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#destroing all the windows created.
cap.release()
cv2.destroyAllWindows()
