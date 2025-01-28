import cv2 as cv
#traitement 1
imgsrc = cv.imread("src/images/GE141002.bmp", cv.IMREAD_GRAYSCALE)
elementStruct = cv.getStructuringElement(cv.MORPH_RECT, (6, 6))

def traitement1():
    binval, imgBinary = cv.threshold(imgsrc, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    print(f"Seuil de binarisation utilisé: {binval}")
    cv.imshow("Boules binarise", imgBinary)
    cv.waitKey(0)
    return imgBinary

#traitement 2
def traitement2():
    imgOuverture = cv.morphologyEx(imgsrc, cv.MORPH_OPEN, elementStruct)
    cv.imshow("Boules ouverture", imgOuverture)
    cv.waitKey(0)
    return imgOuverture

def traitement3(imgOuverture):
    imgFermeture = cv.morphologyEx(imgOuverture, cv.MORPH_CLOSE, elementStruct)
    cv.imshow("Boules fermeture", imgFermeture)
    cv.waitKey(0)