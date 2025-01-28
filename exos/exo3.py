import cv2 as cv

def exercice3():

    # read the image 
    img = cv.imread("src/images/GE141002.bmp") 
    
    # showing the image 
    cv.imshow('boules', img) 
    cv.waitKey(0)
    # Attend que tu appuis sur une touche pour fermer la fenetre
