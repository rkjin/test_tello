from djitellopy import Tello
import cv2

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

key = cv2.waitKey(1)
if key == ?:
    