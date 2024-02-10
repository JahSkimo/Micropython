from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    if state == 0:
        mycontroller.drive_forwards()

        if mycontroller.left_odom.get_count() >= 2000 and mycontroller.right_odom.get_count() >=2000:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()

        elif state == 1:
            mycontroller.custom_right_turn(75)
            turns_made += 1

            if turns_made > 1:
                state = 3
            else: 
                state = 0 

                if mycontroller.left_odom.get_count() >= 2000 and mycontroller.right_odom.get_count() >=2000:
                    state = 2
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()

        elif state == 2:
            mycontroller.custom_left_turn(145)
            turns_made += 1

            if turns_made > 1:
                state = 3

            elif state == 3:
                mycontroller.stop

