import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image
import numpy as np

import common_functions as cf
import coordinates as coords

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.4

####################
###    SET UP    ###
####################
# left click ardy cape in 1st slot of inv
# Varrock teleport runes in inv
# left click Varrock teleport to grand exchange

def start():
    #cf.login()
    cf.screen_scroll(coords.zoom_bar_1)
    cf.click_compass()
    cf.angle_up()
    # Scroll mininmap up for 4 seconds
    minimap_rightside_coord = [1418, 153]
    gui.moveTo(minimap_rightside_coord)
    start_time = time.monotonic()
    while time.monotonic() < start_time + 4:
        gui.scroll(3)
        time.sleep(0.1)
    gui.leftClick()
    time.sleep(3)


def fairy_ring_dkp():
    cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, 4)
    cf.m

def enter_arena():
    captain_izzy_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if not captain_izzy_location:
        cf.screen_scroll(coords.zoom_bar_max)
        while not captain_izzy_location:
            captain_izzy_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
            time.sleep(3)
    cf.move_and_click(captain_izzy_location, -1, 3)
    time.sleep(90)
    ladder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if not ladder_location:
        cf.screen_scroll(coords.zoom_bar_max)
        while not ladder_location:
            ladder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
            time.sleep(3)
    cf.move_and_click(ladder_location, -1, 3)
    cf.screen_scroll(coords.zoom_bar_1)
    time.sleep(2)


def get_to_obstacle():
    obstacle_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(obstacle_location, -1, 8)
    cf.move_and_click([720, 450], -1, 8)
    cf.move_and_click([587, 332], -1, 5)
    cf.screen_scroll(coords.zoom_bar_5)
    gui.press("/")


def auto_click():
    time.sleep(1.5)
    cf.move_and_click((989, 360), -1, -1)
    time_start = time.monotonic()
    while time.monotonic() < time_start + RUN_TIME * 60 * 60:
        time.sleep(random.uniform(0.27, 0.47))
        gui.click()


def finish():
    gui.press("/")
    cf.logout()


def run():
    start()