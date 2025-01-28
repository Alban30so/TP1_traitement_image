import cv2 as cv
#traitement 1
def traitement1():
    imgsrc = cv.imread("src/images/boules.png", cv.IMREAD_GRAYSCALE)
    binval, imgBinary = cv.threshold(imgsrc, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    print(f"Seuil de binarisation utilisé: {binval}")
    cv.imshow("Boules binarise", imgBinary)
    cv.waitKey(0)