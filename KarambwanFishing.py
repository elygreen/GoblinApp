import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image
import numpy as np

import common_functions as cf
import coordinates
import coordinates as coords

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.4
MINIMAP_RIGHT_SIDE_COORD = [1418, 153]

####################
###    SET UP    ###
####################
# left click ardy cape in 1st slot of inv
# Varrock teleport runes in inv
# left click Varrock teleport to grand exchange
# fairy ring set to dkp

def start():
    #cf.login()
    #cf.screen_scroll(coords.zoom_bar_1)
    #cf.click_compass()
    #cf.angle_up()
    cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, 4)
    # Scroll mininmap up for 4 seconds
    gui.moveTo(MINIMAP_RIGHT_SIDE_COORD)
    start_time = time.monotonic()
    while time.monotonic() < start_time + 3:
        gui.scroll(-300)


def fairy_ring_dkp():
    cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, 4)
    cf.move_and_click(MINIMAP_RIGHT_SIDE_COORD, -1, 12 + random.uniform(0, 2))
    fairy_ring_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if not fairy_ring_location:
        return
    cf.move_and_click(fairy_ring_location, -1, 7)

def begin_fishing():
    fishing_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    while not fishing_location:
        time.sleep(5)
        fishing_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(fishing_location, -1, -1)
    time.sleep(85 + random.uniform(1, 7))


def bank_inventory():
    cf.move_and_click(coordinates.tab_magic, -1, -1)
    varrock_tele_location = (1249, 430)
    cf.move_and_click(varrock_tele_location, -1, -1)
    cf.move_and_click(coordinates.tab_inventory, -1, -1)
    bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(bank_location, -1, 5)
    gui.write("9149", interval=0.27)
    cf.move_and_click(coords.inventory_slot[8], -1, -1)
    gui.press("esc")


def finish():
    gui.press("/")
    cf.logout()


def run():
    start()
    start_time = time.monotonic()
    while time.monotonic() < start_time + RUN_TIME:
        fairy_ring_dkp()
        begin_fishing()
        bank_inventory()