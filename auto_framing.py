import cv2

zoomed_2 = False
zoomed = False
offset_x, offset_y = 0, 0
offsetValue = 2
tolerance = 20

def move_right(offset_x1, offset_x2, x2):
    if x2 + offsetValue >= framewidth:
        return [offset_x1 + framewidth - x2, offset_x2 + framewidth - x2]
    else:
        return [offset_x1 + offsetValue, offset_x2 + offsetValue]

def move_left(offset_x1, offset_x2, x1):
    if x1 - offsetValue <= 0:
        return [offset_x1 - x1, offset_x2 - x1]
    offset_x1 -= offsetValue
    offset_x2 -= offsetValue
    return [offset_x1, offset_x2]

def move_up(offset_y1, offset_y2, y1):
    if y1 - offsetValue <= 0:
        return [offset_y1 - y1, offset_y2 - y1]
    offset_y1 -= offsetValue
    offset_y2 -= offsetValue
    return [offset_y1, offset_y2]

def move_down(offset_y1, offset_y2, y2):
    if y2 + offsetValue >= frameheight:
        return [offset_y1 + frameheight - y2, offset_y2 + frameheight - y2]
    offset_y1 += offsetValue
    offset_y2 += offsetValue
    return [offset_y1, offset_y2]

def zoom_2x(frame):

    framewidth, frameheight = frame.shape[1], frame.shape[0]
    x1 = framewidth//4 + offset_x
    y1 = frameheight//4 + offset_y
    x2 = 3*framewidth//4 + offset_x
    y2 = 3*frameheight//4 + offset_y
    return [x1, y1, x2, y2]

def zoom_1_5x(frame):
    framewidth, frameheight = frame.shape[1], frame.shape[0]
    x1 = framewidth//6 + offset_x
    y1 = frameheight//6 + offset_y
    x2 = 5*framewidth//6 + offset_x
    y2 = 5*frameheight//6 + offset_y

    return [x1, y1, x2, y2]


cap = cv2.VideoCapture(0)

ret, frame = cap.read()
frameheight, framewidth = frame.shape[:2]
x1, y1, x2, y2 = 0, 0, framewidth, frameheight
detector = cv2.FaceDetectorYN.create("face_detection_yunet_2023mar.onnx", "", (framewidth, frameheight))
while True:
    ret, frame = cap.read()
    if not ret:
        break

    x, y, w, h = 0, 0, 0, 0

    frame = cv2.flip(frame, 1)
    detector.setInputSize((frame.shape[1], frame.shape[0]))
    _, faces = detector.detect(frame)

    if faces is not None:
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        
        main_face = faces[0]
    
        x, y, w, h = map(int, main_face[:4])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        offset_x, offset_y = 0, 0
        zoomed = not zoomed
        zoomed_2 = False
    
    if key == ord('2'):
        offset_x, offset_y = 0, 0
        zoomed_2 = not zoomed_2
        zoomed = False

    if zoomed_2:
        zoom_2x_arr = zoom_2x(frame)
        x1, y1, x2, y2 = zoom_2x_arr[0], zoom_2x_arr[1], zoom_2x_arr[2], zoom_2x_arr[3]


        
    elif zoomed:
        zoom_1_5x_arr = zoom_1_5x(frame)
        x1, y1, x2, y2 = zoom_1_5x_arr[0], zoom_1_5x_arr[1], zoom_1_5x_arr[2], zoom_1_5x_arr[3]


    face_center_x = (2*x + w)//2
    face_center_y = (2*y + h)//2
    frame_center_x = (x1 + x2)//2
    frame_center_y = (y1 + y2)//2

    
    if key == ord('d') or face_center_x > frame_center_x + tolerance:
        move_right_arr = move_right(offset_x, offset_x, x2)
        offset_x, offset_x = move_right_arr[0], move_right_arr[1]

        

    elif key == ord('a') or face_center_x < frame_center_x - tolerance:
        move_left_arr = move_left(offset_x, offset_x, x1)
        offset_x, offset_x = move_left_arr[0], move_left_arr[1]

    
    if key == ord('w') or face_center_y < frame_center_y - tolerance:
        move_up_arr = move_up(offset_y, offset_y, y1)
        offset_y, offset_y = move_up_arr[0], move_up_arr[1]
 
    
    elif key == ord('s') or face_center_y > frame_center_y + tolerance:
        move_down_arr = move_down(offset_y, offset_y, y2)
        offset_y, offset_y = move_down_arr[0], move_down_arr[1]

    if zoomed or zoomed_2:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        showFrame = frame[y1:y2, x1:x2]
        showFrame = cv2.resize(showFrame, (int(1.4*framewidth), int(1.4*frameheight)))

    else:
        showFrame = frame
        showFrame = cv2.resize(showFrame, (int(1.4*framewidth), int(1.4*frameheight)))
    

    cv2.imshow("Webcam", showFrame)
    if key == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()