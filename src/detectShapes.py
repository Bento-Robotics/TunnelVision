import cv2


def do_it(value):
    inverted = value
    on_change(150)


def on_change(val):
    t1 = val
    image = cv2.imread('../images/shapes.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, t1, 255, wert)
    contours, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        print(len(approx))
        if len(approx) == 5:
            print("Pentagon")
            cv2.drawContours(image, [cnt], 0, 255, -1)
        elif len(approx) == 3:
            print("Triangle")
            cv2.drawContours(image, [cnt], 0, (0, 255, 0), -1)
        elif len(approx) == 4:
            print("Square")
            cv2.drawContours(image, [cnt], 0, (0, 0, 255), -1)
        # elif len(approx) == 9:
        #   print ("half-circle")
        #   cv2.drawContours(img,[cnt],0,(255,255,0),-1)
        elif len(approx) > 5:
            print("Circle")
            cv2.drawContours(image, [cnt], 0, (0, 255, 255), -1)

    image_copy = image.copy()
    cv2.imshow('img', image_copy)


img = cv2.imread('../images/shapes.png')
wert = 1
cv2.imshow('img', img)
cv2.createTrackbar('Threshold', 'img', 150, 250, on_change)
cv2.createTrackbar('Invert', 'img', 1, 1, do_it)
cv2.waitKey(0)
cv2.destroyAllWindows()
