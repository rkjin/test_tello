from djitellopy import Tello
import cv2

img = cv2.imread('./tello.jpg')
cv2.imshow('img', img)

tello = Tello()
tello.connect()
tello.query_battery()
# tello.takeoff()
# #move
# tello.move_up(150)
# tello.move_forward(100)
# tello.rotate_clockwise(90)
# tello.move_forward(100)
# tello.rotate_clockwise(90)
# tello.move_forward(100)
# tello.rotate_clockwise(90)
# tello.move_forward(100)
# tello.rotate_clockwise(90)
# tello.flip_back() 
# tello.flip_forward()
# tello.land()
while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    elif key == ord('b'):
        tello.move('back', 100)
    elif key == ord('f'):
        tello.move('forward', 100)
    # if key == ord('l'):
    #     tello.move_('left', 100)
    elif key == ord('r'):
        tello.move('right', 100)     
    elif key == ord('u'):
        tello.move('up', 100)
    elif key == ord('d'):
        tello.move('down', 100)
    # if key == ord('l'):
    #     tello.move_('left', 100)
    elif key == ord('r'):
        tello.move('right', 100)        
    elif key == ord('c'):
        tello.rotate_clockwise(30)      

    if key == 27:
        break

cv2.destroyAllWindows()
