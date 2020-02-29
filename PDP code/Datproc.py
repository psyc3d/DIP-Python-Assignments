import numpy as np


def imm_vel(int1,int2):
    # assuming there is a 10ms delay between readings
    rel_vel = (int1-int2)*10    #Converting to m/s
    return rel_vel

def sorter(int2,int1):
    print(f"The relative speed is {int2} m/s ")
    if int2 > 0:
        time_to_contact = int1/int2
        tc = time_to_contact
        print(f"The time to contact is {tc}s")
        if tc<2.0 and tc>0.0:
            return 1
        elif tc<10.0 and tc>2.0:
            return 2
        elif tc<20.0 and tc>10.0:
            return 3
        elif tc>20.0:
            return 4
    else:
        print("You are lagging")
        return 0

def alert_lvl(argument):
    switcher = {
        0:"Off",
        1:"High Alert",
        2:"Medium Alert",
        3:"Obstacle Detected",
        4:"Off",
        }
    return switcher.get(argument, "nothing")




# Take the input about the displacements

o = 0

while o != 1:
    disp1 = int(input())
    disp2 = int(input())

    rel = imm_vel(disp1,disp2)
    if rel != 0:
        print(alert_lvl(sorter(rel,disp2))) 
    else:
        print("No loss or gain")



