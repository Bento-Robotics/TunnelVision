import easyocr
import matplotlib.pyplot as plt
import cv2


def detect_text(image):
    # Text recognition
    reader = easyocr.Reader(['en'])
    text_ = reader.readtext(image)
    threshold = 0.25  # set higher as needed

    for t in text_:
        print(t)

        bbox, text, score = t

        if score > threshold:
            cv2.rectangle(image, bbox[0], bbox[2], (0, 255, 0), 5)
            cv2.putText(image, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()


image = cv2.imread('../images/road-warning-sign.jpg')
detect_text(image)
