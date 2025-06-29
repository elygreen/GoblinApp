import sys
import time
import threading
import pyautogui as gui
import random

import common_functions as cf
import coordinates as coords

FISH_STALL_COORDS = (721, 403)

####################
### REQUIREMENTS ###
####################
# Raw tuna, salmon, and lobster set to left click drop
# Lure thief

def Run():
    cf.click_compass()
    cf.scroll_in()
    start_time = time.monotonic()
    while time.monotonic() < start_time + 5.5 * 60 * 60:
        cf.move_and_click_variable_coord(FISH_STALL_COORDS, -1, -1)
        cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, -1)
        time.sleep(random.uniform(8, 8.7))
