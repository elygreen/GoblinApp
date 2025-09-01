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
RUN_TIME = 5.4
TEMPLATE_THRESHOLD = 0.8
OVERCORRECT_PIXELS = 10
BOX_SET_UP_WAIT = 10


def start():
    global fallen_trap_template
    #cf.login()
    cf.screen_scroll(coords.zoom_bar_middle)
    cf.click_compass()
    cf.angle_up()
    fallen_trap_template = load_fallen_trap_template("templates/box_trap.PNG")
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
    time.sleep(2.5)


def fix_fallen_traps():
    fallen_trap = find_fallen_trap_template(fallen_trap_template, cf.DEFAULT_GAME_SCREEN, TEMPLATE_THRESHOLD)
    while fallen_trap is not None:
        x, y = fallen_trap
        cf.move_and_click((x, y), -1, box_set_up_wait_time())
        fallen_trap = find_fallen_trap_template(fallen_trap_template, cf.DEFAULT_GAME_SCREEN, TEMPLATE_THRESHOLD)


def fix_caught_and_failed_traps():
    box_location = find_first_colored_pixel(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if box_location:
        cf.move_and_click(box_location, -1, box_set_up_wait_time())


def box_set_up_wait_time():
    return BOX_SET_UP_WAIT + random.uniform(0, 1)


def load_fallen_trap_template(template_path):
    try:
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        if template is None:
            raise ValueError(f"Could not load template from {template_path}")
        return template
    except Exception as e:
        print(f"Error loading template: {e}")
        return None


def find_fallen_trap_template(template, search_area=None, threshold=TEMPLATE_THRESHOLD):
    try:
        if search_area:
            left, top, right, bottom = search_area
            screenshot = gui.screenshot(region=(left, top, right-left, bottom-top))
            offset_x, offset_y = left, top
        else:
            screenshot = cf.take_screenshot()
            offset_x, offset_y = 0, 0
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            template_h, template_w = template.shape[:2]
            center_x = max_loc[0] + template_w // 2 + offset_x
            center_y = max_loc[1] + template_h // 2 + offset_y
            print(f"Found fallen trap at ({center_x}, {center_y}) with confidence {max_val:.3f}")
            return center_x, center_y
        else:
            print(f"No fallen trap found (best match: {max_val:.3f}, threshold: {threshold})")
            return None
    except Exception as e:
        print(f"Error in template matching: {e}")
        return None



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
