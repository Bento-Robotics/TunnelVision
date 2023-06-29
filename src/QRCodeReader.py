import cv2


def detect_qr(image):
    # Grayscale image and Binary Thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Show binary image
    cv2.imshow('Binary Image', binary_img)
    cv2.waitKey(0)

    # Detect QR code
    det = cv2.QRCodeDetector()
    info, box_coordinates, _ = det.detectAndDecode(binary_img)

    # Print a QR code's data if found
    print('No code found' if box_coordinates is None else info)

    # Draw box around QR code
    if box_coordinates is not None:
        box_coordinates = [box_coordinates[0].astype(int)]
        n = len(box_coordinates[0])
        for i in range(n):
            cv2.line(image, tuple(box_coordinates[0][i]), tuple(box_coordinates[0][(i + 1) % n]), (0, 255, 255), 6)

    # Show original image with box
    cv2.imshow('Output', image)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()


image = cv2.imread('../images/wifi-sign.jpg')
detect_qr(image)
