import sys
import time
import threading
import pyautogui as gui
import random

import common_functions as cf
import coordinates as coords

FISH_STALL_COORDS = (721, 403)
CROSSBOW_STALL_COORDS = (830, 472)
SPICE_STALL = (769, 399)

####################
### REQUIREMENTS ###
####################
# Raw tuna, salmon, and lobster set to left click drop
# Lure thief

def Run():
    time.sleep(2)
    start_time = time.monotonic()
    while time.monotonic() < start_time + 5.5 * 60 * 60:
        #cf.move_and_click_variable_coord(SPICE_STALL, -1, -1)
        cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, random.uniform(.1, .3))
        cf.move_and_click_variable_coord(SPICE_STALL, -1, random.uniform(0, .3))
        for i in range(20):
            wait_time = time.monotonic() + 5.3 + random.uniform(.2, .5)
            while time.monotonic() < wait_time:
                gui.click()
                time.sleep(random.uniform(.1, .3))
        for i in range(21):
            cf.move_and_click_variable_coord(coords.inventory_slot[i], random.uniform(.13, .27), random.uniform(.1, .2))
