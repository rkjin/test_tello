from djitellopy import Tello

tello = Tello()


tello.connect()

tello.query_battery()

tello.takeoff()

#move 
tello.move_up(150)
tello.move_forward(100)
tello.rotate_clockwise(90)
tello.move_forward(100)
tello.rotate_clockwise(90)
tello.move_forward(100)
tello.rotate_clockwise(90)
tello.move_forward(100)
tello.rotate_clockwise(90)
tello.flip_back()
tello.flip_forward()


tello.land()

pass
