import cv2
import QRCodeReader

cap = cv2.VideoCapture(0)
det = cv2.QRCodeDetector()

while 1:

    # reads frame from a camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera', frame)

    # Wait for 25ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()

    QRCodeReader.detect_qr(cap)

cv2.imshow('Output', cap)
cv2.waitKey(0)
cv2.destroyAllWindows()
