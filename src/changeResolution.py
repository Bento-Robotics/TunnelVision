import cv2
import time


def resize_and_grayscale(image):
    return cv2.cvtColor(cv2.resize(image, (480, 360)), cv2.COLOR_BGR2GRAY)


def set_cap_properties(vcap, width=640, height=480, fps=30):
    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    vcap.set(cv2.CAP_PROP_FPS, fps)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 5)
set_cap_properties(cap, 1280, 720)
success, image = cap.read()

lasttime = time.monotonic().__trunc__()
while success:
    success, image = cap.read()

    cv2.imshow('Lo-Res grayscale', resize_and_grayscale(image))
    # Update high-res every second
    # if lasttime < (time.monotonic().__trunc__()):
    #     cv2.imshow('Lo-Speed Hi-res', image)
    #     lasttime = time.monotonic().__trunc__()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
