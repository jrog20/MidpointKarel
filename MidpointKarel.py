from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

def main():
    """
    Karel will start at the southwestern most point, place a beeper in that corner, and the southeastern most point.
    Karel will then ping pong back and forth on the southern wall, moving the two beepers closer to the center.
    What remains is one beeper at the center of the southern wall.
    """

    if front_is_blocked():
        put_beeper()
    else:
        place_initial_beepers()
        move_to_wall()
        place_initial_beepers()
        turn_around()
        move()
        while no_beepers_present():
            move()
        while beepers_present():
            relocate_beeper()
        put_beeper()

def place_initial_beepers():
    if no_beepers_present():
        put_beeper()

#pre: Karel, while moving away from center, runs into a beeper
#post: Karel is now facing toward the center, and has moved the beeper one space toward the center.

def relocate_beeper():
    while beepers_present():
        pick_beeper()
        turn_around()
        move()
        if no_beepers_present():
            put_beeper()
            move()
            while no_beepers_present():
                move()
        else:
            pick_beeper()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
