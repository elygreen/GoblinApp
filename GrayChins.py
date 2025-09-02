import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image
import numpy as np
import cv2

import common_functions as cf
import coordinates as coords

####################
###    SET UP    ###
####################
# Stand on Gray Chin tile
# Set up box traps

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.27
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
    box_location = find_first_colored_pixel(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if box_location:
        cf.move_and_click(box_location, random.uniform(0.17, .23), box_set_up_wait_time())


def box_set_up_wait_time():
    return BOX_SET_UP_WAIT + random.uniform(0, .7)


def find_first_colored_pixel(target_color, tolerance=0, search_area=None):
    # Crop screen then convert to numpy
    if search_area:
        left, top, right, bottom = search_area
        # Take screenshot of only the search area
        screenshot = gui.screenshot(region=(left, top, right-left, bottom-top))
        offset_x, offset_y = left, top
    else:
        screenshot = cf.take_screenshot()
        offset_x, offset_y = 0, 0

    img_array = np.array(screenshot)
    # Boolean mask for matching pixels
    if tolerance == 0:
        mask = np.all(img_array == target_color, axis=2)
    else:
        # Vectorized tolerance check
        diff = np.abs(img_array - target_color)
        mask = np.all(diff <= tolerance, axis=2)

    # Find matching coordinates
    matching_coords = np.where(mask)

    if len(matching_coords[0]) == 0:
        return None

    # Return the first matching pixel (top-left in reading order)
    first_y = matching_coords[0][0] + offset_y
    first_x = matching_coords[1][0] + offset_x

    return first_x+OVERCORRECT_PIXELS, first_y+OVERCORRECT_PIXELS



def finish():
    gui.press("/")
    cf.logout()


def run():
    start()
    start_time = time.monotonic()
    while time.monotonic() < start_time + RUN_TIME * 60 * 60:
        chin_hunting_loop()
