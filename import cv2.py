import cv2

try:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while(True):
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

except IOError as e:
    print(f"Error: {e}")