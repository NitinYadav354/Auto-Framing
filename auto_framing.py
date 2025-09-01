import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
zoom_level = 0.9
i = 0
while True:
    ret, frame = cap.read()
    frameheight, framewidth = frame.shape[:2]
    aspect_ratio = framewidth / frameheight
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 0:
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        x, y, w, h = faces[0] if len(faces) > 0 else (0, 0, 0, 0)
    if w > 0 and h > 0:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 200, 200), 2)

    face_center_x, face_center_y = x + w/2, y + h/2
    print (w)


    if (w > 0):
        x1 = int(max(0, x - w))
        y1 = int(max(0, y - h//2))
        x2 = int(min(framewidth, x + w*2))
        y2 = int(min(frameheight, aspect_ratio * (x2 - x1) + y1))

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        zoomed = frame[y1:y2, x1:x2]
        zoomed = cv2.resize(zoomed, (int(1.3*framewidth), int(1.3*frameheight)))




    # if (w > 0):
    #     zoom_level = 0.9
    #     crop_w = int(zoom_level * framewidth)
    #     crop_h = int(crop_w * frameheight / framewidth)
    #     x1 = max(0, int(face_center_x - crop_w/2))
    #     y1 = max(0, int(face_center_y - crop_h/2))
    #     x2 = min(framewidth, x1 + crop_w)
    #     y2 = min(frameheight, y1 + crop_h)
    #     zoomed = frame[y1:y2, x1:x2]
    #     zoomed = cv2.resize(zoomed, (int(1.3*framewidth), int(1.3*frameheight)))
    # elif (i == 0 and w >= 100 and w < 200):
    #     zoom_level = 0.8
    #     crop_w = int(zoom_level * framewidth)
    #     crop_h = int(crop_w * frameheight / framewidth)
    #     x1 = max(0, int(face_center_x - crop_w/2))
    #     y1 = max(0, int(face_center_y - crop_h/2))
    #     x2 = min(framewidth, x1 + crop_w)
    #     y2 = min(frameheight, y1 + crop_h)

    #     zoomed = frame[y1:y2, x1:x2]
    #     zoomed = cv2.resize(zoomed, (int(1.3*framewidth), int(1.3*frameheight)))
    # else:
    #     zoomed = cv2.resize(frame, (int(1.3*framewidth), int(1.3*frameheight)))
    cv2.imshow("Webcam", zoomed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()