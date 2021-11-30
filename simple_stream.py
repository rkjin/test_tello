from djitellopy import Tello
import cv2


tello = Tello()
tello.connect()
tello.query_battery()

tello.streamon()
frame = tello.get_frame_read()
while True:
    cv2.imshow('tello',frame.frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

tello.streamoff()

cv2.destroyAllWindows()
