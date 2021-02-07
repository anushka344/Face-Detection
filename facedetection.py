def reverse(string):
    reversed_string=""
    for i in string:
        reversed_string=i+reversed_string
    print("The reversed string is",reversed_string)

import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#loading image
img=cv2.imread("tony.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#to store x y width and values using cascade classifier
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,
minNeighbors = 5)




for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 3)
    
print(type(faces))
print(faces)    
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
