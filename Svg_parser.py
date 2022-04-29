
import turtle
from Inverse_kinematics import show, show_turtle
import re
from time import sleep
from Svg_parser import write_points

def get_coor_from_str(string):

    match = re.match(r"[(](\d+[.]\d+), (\d+[.]\d+)[)]", string)
    try:
        return float(match.group(1)), float(match.group(2))
    except:
        return

write_points("TD_ROBOTIC_ARM_2.0\Discord.svg", 50)
turtle.hideturtle()
with open('points.txt', "r") as f:

    turtle.tracer(0)
    goto = False

    for line in f:
        if line == "n\n":
            goto = True
        
        else:
            coor = get_coor_from_str(line)
            if coor == None: continue
            if goto:
                turtle.up()
                turtle.goto(coor[0], -coor[1])
                turtle.down()
                goto = False
            else:
                turtle.goto(coor[0], -coor[1])
            show(coor[0], -coor[1], 400)
            turtle.update()
            show_turtle.clear()



turtle.update()
turtle.mainloop()