import cv2

zoomed_2 = False
zoomed = False
def zoom_2x(frame):
    framewidth, frameheight = frame.shape[1], frame.shape[0]

    zoomed = frame[frameheight//4: 3*frameheight//4, framewidth//4: 3*framewidth//4]
    zoomed = cv2.resize(zoomed, (frame.shape[1], frame.shape[0]))
    return zoomed

def zoom_1_5x(frame):
    framewidth, frameheight = frame.shape[1], frame.shape[0]

    zoomed = frame[frameheight//6: 5*frameheight//6, framewidth//6: 5*framewidth//6]
    zoomed = cv2.resize(zoomed, (frame.shape[1], frame.shape[0]))
    return zoomed


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        zoomed = not zoomed
        zoomed_2 = False
    
    if key == ord('2'):
        zoomed_2 = not zoomed_2
        zoomed = False

    if zoomed_2:
        showFrame = zoom_2x(frame) 
        
    elif zoomed:
        showFrame = zoom_1_5x(frame)
        
    else:
        showFrame = frame
    
    cv2.imshow("Webcam", showFrame)
    if key == ord('q'):
        break
# def left(x1, y1, x2, y2):
#     x1, y1, x2, y2 = x1-1, y1, x2-1, y2
#     frame = 
# import cv2

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)
# zoom_level = 0.9
# i = 10
# while True:
#     if i == 20:
#         i = 0
#     else:
#         i += 1
#     ret, frame = cap.read()
#     frameheight, framewidth = frame.shape[:2]
#     aspect_ratio = framewidth / frameheight
#     if not ret:
#         break
#     frame = cv2.flip(frame, 1)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     if i> 0:
#         faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#         x, y, w, h = faces[0] if len(faces) > 0 else (0, 0, 0, 0)
#     if w != 0 and h > 0:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 200, 200), 2)

#     face_center_x, face_center_y = x + w/2, y + h/2



#     if (w > 0 and i == 0):
#         print (i)
#         x1 = int(max(0, x - w))
#         y1 = int(max(0, y - h//2))
#         x2 = int(min(framewidth, x + w*2))
#         y2 = int(min(frameheight, aspect_ratio * (x2 - x1) + y1))

#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         zoomed = frame[y1:y2, x1:x2]
#         zoomed = cv2.resize(zoomed, (int(1.3*framewidth), int(1.3*frameheight)))




#     # if (w > 0):
#     #     zoom_level = 0.9
#     #     crop_w = int(zoom_level * framewidth)
#     #     crop_h = int(crop_w * frameheight / framewidth)
#     #     x1 = max(0, int(face_center_x - crop_w/2))
#     #     y1 = max(0, int(face_center_y - crop_h/2))
#     #     x2 = min(framewidth, x1 + crop_w)
#     #     y2 = min(frameheight, y1 + crop_h)
#     #     zoomed = frame[y1:y2, x1:x2]
#     #     zoomed = cv2.resize(zoomed, (int(1.3*framewidth), int(1.3*frameheight)))
#     # elif (i == 0 and w >= 100 and w < 200):
#     #     zoom_level = 0.8
#     #     crop_w = int(zoom_level * framewidth)
#     #     crop_h = int(crop_w * frameheight / framewidth)
#     #     x1 = max(0, int(face_center_x - crop_w/2))
#     #     y1 = max(0, int(face_center_y - crop_h/2))
#     #     x2 = min(framewidth, x1 + crop_w)
#     #     y2 = min(frameheight, y1 + crop_h)

#     #     zoomed = frame[y1:y2, x1:x2]
#     #     zoomed = cv2.resize(zoomed, (int(1.3*framewidth), int(1.3*frameheight)))
#     else:
#         zoomed = cv2.resize(frame, (int(1.3*framewidth), int(1.3*frameheight)))
#     cv2.imshow("Webcam", zoomed)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()