#Defining Container_ID list
Container_ID = [1,2,3,4,5,6]
pick_up_position = (x,y,z)
#Defining all our functions:

def autoclave_bin_location(Container_ID):
    for i in range(len(Container_ID)):
        if Container_ID[i] == 1
            location_ID = (-0.473, 0.172, 0.522)
        elif Container_ID[i] == 2
            location_ID = (-0.673, 0.432, 0.522)
        elif Container_ID[i] == 3
            location_ID = (-0.862, -0.172, 0.522)
        elif Container_ID[i] == 4
            location_ID = (-0.473, 0.172, 0.322)
        elif Container_ID[i] == 5
            location_ID = (-0.673, 0.432, 0.322)
        elif Container_ID[i] == 6
            location_ID = (-0.862, -0.172, 0.322)

    return location_ID

def pick_up:(Container_ID):
    if arm.emg_left()>0.85 and arm.emg_right()==0:
        arm.move_arm(pick_up_position)
        time.sleep(2)
    else:
        pass

def drop_off(Container_ID):
    if arm.emg_left()>0.85 and arm.emg_right()==0:
        drop_off_position = autoclave_bin_location(Container_ID)
        arm.move_arm(location_ID[0],location_ID[1],location_ID[2])
        time.sleep(2)
        arm.home()

def control_gripper(Container_ID,states):
    if states == "open"
        if arm.emg_left()>0.85 and arm.emg_right()>0.85:
            if Container_ID == 1 or 2 or 3:
                arm.control_gripper(40)
            else Container_ID == 4 or 5 or 6:
                arm.control_gripper(30)
        else:
            pass
    elif states == "close"
        if arm.emg_left()>0.85 and arm.emg_right()>0.85:
                if Container_ID == 1 or 2 or 3:
                    arm.control_gripper(-40)
                else Container_ID == 4 or 5 or 6:
                    arm.control_gripper(-30)
            else:
                pass

def control_autoclave_bin(Container_ID):
    if Container_ID == 1 or 2 or 3:
        pass
    elif Container_ID == 4:
        arm.open_red_autoclave(True)
    elif Container_ID == 5:
        arm.open_green_autoclave(True)
    elif Container_ID == 6:
        arm.open_blue_autoclave(True)
    



def main():
    if Container_ID
    if Container_ID = 4:
        arm.open_red_autoclave(True)
        pick_up()
        
