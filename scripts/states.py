from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    if state == 0:
        mycontroller.drive_forwards()

elif state == 1:
        mycontroller.raft.led_on()

        mycontroller.left_turn()
        turns_made += 1


 elif state == 2:
        mycontroller.right_turn()
        turns_made += 1



