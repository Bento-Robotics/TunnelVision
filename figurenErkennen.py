import numpy as np
import cv2
def do_it(wert):
    inverted=wert
    on_change(150)
    
def on_change(val):
    t1=val
    img = cv2.imread('/home/david/Bilder/schachbrett.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,t1,255,wert)
    contours,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        print( len(approx))
        if len(approx)==5:
           print ("Fünfeck")
           cv2.drawContours(img,[cnt],0,255,-1)
        elif len(approx)==3:
           print ("Dreieck")
           cv2.drawContours(img,[cnt],0,(0,255,0),-1)
        elif len(approx)==4:
           print ("Viereck")
           cv2.drawContours(img,[cnt],0,(0,0,255),-1)
        #elif len(approx) == 9:
         #   print ("half-circle")
         #   cv2.drawContours(img,[cnt],0,(255,255,0),-1)
        elif len(approx) > 5:
            print ("Kreis")
            cv2.drawContours(img,[cnt],0,(0,255,255),-1)
    
    imageCopy = img.copy()
    cv2.imshow('img', imageCopy)

img = cv2.imread('/home/david/Bilder/schachbrett.jpg')
wert = 1
cv2.imshow('img',img)
cv2.createTrackbar('threshold', 'img', 150, 250, on_change)
cv2.createTrackbar('Invertieren','img',1,1,do_it)
cv2.waitKey(0)
cv2.destroyAllWindows()
