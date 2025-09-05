import time
import pyautogui as gui
import random
import numpy as np

import common_functions as cf
import coordinates as coords

####################
###    SET UP    ###
####################
# Stand on Gray Chin tile
# Set up box traps

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.7
TEMPLATE_THRESHOLD = 0.5
OVERCORRECT_PIXELS = 3
BOX_SET_UP_WAIT = 8.4
FULL_SET_UP = False


def start():
    global fallen_trap_template
    if FULL_SET_UP:
        cf.login()
        cf.screen_scroll(coords.zoom_bar_middle)
        cf.click_compass()
        cf.angle_up()
    fallen_trap_template = cf.load_image_template("templates/box_trap.PNG")
    if fallen_trap_template is None:
        print("Error loading fallen trap template")
        quit()
    time.sleep(2)


def chin_hunting_loop():
    # Check for fallen traps first
    fix_fallen_traps()
    # Check for other traps
    fix_caught_and_failed_traps()
    # Wait period
    time.sleep(.15)


def fix_fallen_traps():
    fallen_trap = cf.find_template_on_screen(fallen_trap_template, cf.DEFAULT_GAME_SCREEN, TEMPLATE_THRESHOLD)
    while fallen_trap is not None:
        x, y = fallen_trap
        cf.move_and_click((x, y), random.uniform(0.17, .23), box_set_up_wait_time())
        fallen_trap = cf.find_template_on_screen(fallen_trap_template, cf.DEFAULT_GAME_SCREEN, TEMPLATE_THRESHOLD)


def fix_caught_and_failed_traps():
    box_location = cf.find_first_colored_pixel(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if box_location:
        box_location = (box_location[0] + OVERCORRECT_PIXELS, box_location[1] + OVERCORRECT_PIXELS)
        cf.move_and_click(box_location, random.uniform(0.17, .23), box_set_up_wait_time())


def box_set_up_wait_time():
    return BOX_SET_UP_WAIT + random.uniform(0, .7)



def finish():
    gui.press("/")
    cf.logout()


def run():
    start()
    start_time = time.monotonic()
    while time.monotonic() < start_time + RUN_TIME * 60 * 60:
        chin_hunting_loop()
