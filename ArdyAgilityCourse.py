import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image
import numpy as np

import common_functions as cf
import coordinates as coords

####################
###    SET UP    ###
####################
# Start on tile "ardy course start" (tile ardy course ends on)

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.4

obstacle_1_coords = (915, 255)
obstacle_1_wait = 5.1
obstacle_2_coords = (739, 48)
obstacle_2_wait = 8.2
obstacle_3_coords = (618, 289)
obstacle_3_wait = 7.8
mark_of_grace_coords = (785, 296)
mark_of_grace_wait = 2.5
obstacle_4_coords = (644, 297)
obstacle_4_wait = 3.7
obstacle_5_coords = (752, 484)
obstacle_5_wait = 4.9
obstacle_5_midpoint_coords = (754, 468)
obstacle_5_midpoint_wait = (2.6)
obstacle_6_coords = (865, 425)
obstacle_6_wait = 6.8
obstacle_7_coords = (771, 320)
obstacle_7_wait = 12.5



def extra_wait():
    return random.uniform(0.03, 0.37)


def start():
    cf.login()
    cf.screen_scroll(coords.zoom_bar_2)
    cf.click_compass()
    cf.angle_up()
    time.sleep(3)


def ardy_lap():
    cf.move_and_click_variable_coord(obstacle_1_coords, -1, obstacle_1_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_2_coords, -1, obstacle_2_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_3_coords, -1, obstacle_3_wait + extra_wait())
    cf.move_and_click_variable_coord(mark_of_grace_coords, -1, mark_of_grace_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_4_coords, -1, obstacle_4_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_5_coords, -1, obstacle_5_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_5_midpoint_coords, -1, obstacle_5_midpoint_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_6_coords, -1, obstacle_6_wait + extra_wait())
    cf.move_and_click_variable_coord(obstacle_7_coords, -1, obstacle_7_wait + extra_wait())


def finish():
    cf.logout()


def run():
    start()
    for x in range(1000):
        ardy_lap()
    finish()