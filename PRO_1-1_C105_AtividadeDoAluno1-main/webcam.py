import cv2
vid = cv2.VideoCapture(0)
if (vid.isOpened() == False):
    print("nao foi possivel reproduzir")
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

while(True):
    ret,frame = vid.read()
    cv2.imshow("cam", frame)
    if cv2.waitKey(500) == 32:
        break
vid.release()
