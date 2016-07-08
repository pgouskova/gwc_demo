import cv2
import sys, os

folder= 'C:\Users\pgouskova\Documents\GWC'
# Get user supplied values
cascPath = 'C:\Users\pgouskova\Documents\GWC\haarcascade_frontalface_default.xml'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# i= 0
for img_file in os.listdir(folder+ '\FB_photos'):
     imagePath = folder + '\FB_photos\\' + img_file
     image = cv2.imread(imagePath)
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     # Detect faces in the image
     faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.2,
         minNeighbors=5,
         minSize=(30, 30),
         flags = cv2.cv.CV_HAAR_SCALE_IMAGE
     )
     print "Found {0} faces!".format(len(faces))
     # Draw a rectangle around the faces
     for (x, y, w, h) in faces:
         cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
         # face_gray = gray[y:y+h, x:x+w]
         # cv2.imwrite( folder + "\\faces\\face_"+ str(i) +".jpg", face_gray)
         # i= i+1

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)



