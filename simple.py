from djitellopy import Tello

tello = Tello()


tello.connect()

tello.query_battery()

tello.takeoff()

tello.land()

pass
