import time
import random

import common_functions as cf
import coordinates as coords

####################
###    SET UP    ###
####################
# Start on tile "ardy course start" (tile ardy course ends on)

DEFAULT_TOLERANCE = 5
RUN_TIME = 2.1

laps_until_pickup = 20
current_laps = 0

obstacle_1_coords = (915, 255)
obstacle_1_wait = 5.1
obstacle_2_coords = (739, 48)
obstacle_2_wait = 8.1
obstacle_3_coords = (621, 291)
obstacle_3_wait = 7.4
mark_of_grace_coords = (785, 296)
mark_of_grace_wait = 2.3
obstacle_4_coords = (644, 297)
obstacle_4_wait = 3.3
obstacle_5_coords = (752, 484)
obstacle_5_wait = 4.4
obstacle_5_midpoint_coords = (754, 468)
obstacle_5_midpoint_wait = 2.23
obstacle_6_coords = (865, 425)
obstacle_6_wait = 6.35
obstacle_7_coords = (771, 320)
obstacle_7_wait = 12.1


def extra_wait():
    return random.uniform(0.03, 0.19)


def start():
    cf.start_script(need_login=True, screen_scroll_value=2, need_click_compass=True, need_angle_up=True)


def ardy_lap():
    global current_laps
    global laps_until_pickup

    # Go through course in obstacle order
    cf.move_and_click(obstacle_1_coords, -1, obstacle_1_wait + extra_wait(), 0, 0)
    cf.move_and_click(obstacle_2_coords, -1, obstacle_2_wait + extra_wait(), 0, 0)
    cf.move_and_click(obstacle_3_coords, -1, obstacle_3_wait + extra_wait(), 0, 0)
    if current_laps >= laps_until_pickup:
        cf.move_and_click(mark_of_grace_coords, -1, mark_of_grace_wait + extra_wait(), 0, 0)
        current_laps = 0
    cf.move_and_click(obstacle_4_coords, -1, obstacle_4_wait + extra_wait(), 0, 0)
    cf.move_and_click(obstacle_5_coords, -1, obstacle_5_wait + extra_wait(), 0, 0)
    cf.move_and_click(obstacle_5_midpoint_coords, -1, obstacle_5_midpoint_wait + extra_wait(), 0, 0)
    cf.move_and_click(obstacle_6_coords, -1, obstacle_6_wait + extra_wait(), 0, 0)
    cf.move_and_click(obstacle_7_coords, -1, obstacle_7_wait + extra_wait(), 0, 0)

    current_laps += 1


def finish():
    cf.logout()


def run():
    start()
    start_time = time.monotonic()
    while start_time < time.monotonic() + RUN_TIME:
        ardy_lap()
    finish()
