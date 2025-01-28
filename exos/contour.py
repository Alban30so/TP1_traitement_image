import cv2 
import numpy as np 

def contour(image):

    # Finding Contours 
    # Use a copy of the image e.g. edged.copy() 
    # since findContours alters the image 
    contours, hierarchy = cv2.findContours(image, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

    cv2.imshow('Canny Edges After Contouring', image) 
    cv2.waitKey(0) 

    print("Number of Contours found = " + str(len(contours))) 

    # Draw all contours 
    # -1 signifies drawing all contours 
    cv2.drawContours(image, contours, -1, (50, 255, 50), 3) 

    cv2.imshow('Contours', image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
