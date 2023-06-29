import cv2
import easyocr
import matplotlib.pyplot as plt

img = cv2.imread('images/frame6.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
det = cv2.QRCodeDetector()
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
info, box_coordinates, _ = det.detectAndDecode(gray)

# Text recognition
reader = easyocr.Reader(['en'])
text_ = reader.readtext(img)
threshold = 0.25  # set higher as needed

for t in text_:
    print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


if box_coordinates is None:
    print('No Code')
else:
    print(info)

if box_coordinates is not None:
    box_coordinates = [box_coordinates[0].astype(int)]
    n = len(box_coordinates[0])
    for i in range(n):
        cv2.line(img, tuple(box_coordinates[0][i]), tuple(box_coordinates[0][(i + 1) % n]), (0, 255, 255), 6)

cv2.imshow('Output', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
