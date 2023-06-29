import cv2
cap = cv2.VideoCapture(0)
det = cv2.QRCodeDetector()

while (1):

    # reads frame from a camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera', frame)

    # Wait for 25ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()

    info, box_coordinates, _ = det.detectAndDecode(cap)

    if box_coordinates is None:
        print('No Code')
    else:
        print(info)

    if box_coordinates is not None:
        box_coordinates = [box_coordinates[0].astype(int)]
        n = len(box_coordinates[0])
        for i in range(n):
            cv2.line(cap, tuple(box_coordinates[0][i]), tuple(box_coordinates[0][(i+1) % n]), (0,255,0), 3)

cv2.imshow('Output', cap)
cv2.waitKey(0)
cv2.destroyAllWindows()

