import time
import pyautogui as gui
import random

import common_functions as cf
import coordinates
import coordinates as coords

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.7
MINIMAP_RIGHT_SIDE_COORD = [1418, 153]

first_bank = True

####################
###    SET UP    ###
####################
# left click ardy cape in 1st slot of inv
# Varrock teleport runes in inv
# left click Varrock teleport to grand exchange
# fairy ring set to dkp

def start():
    cf.start_script(need_login=False, screen_scroll_value=3, need_click_compass=True, need_angle_up=True)
    print("Start")


def fairy_ring_dkp():
    cf.move_and_click(coords.inventory_slot[0], -1, 3, precision=5)
    cf.move_and_click(MINIMAP_RIGHT_SIDE_COORD, -1, 10 + random.uniform(0, 2))
    cf.move_and_click((988, 201), -1, 6)
    fairy_ring_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if not fairy_ring_location:
        return
    cf.move_and_click(fairy_ring_location, -1, 10)


def begin_fishing():
    fishing_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    while not fishing_location:
        print("searching for fishing spot")
        time.sleep(3)
        fishing_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(fishing_location, -1, -1)
    time.sleep(110 + random.uniform(1, 7))


def bank_inventory():
    cf.move_and_click(coordinates.tab_magic, -1, -1)
    varrock_tele_location = (1255, 450)
    cf.move_and_click(varrock_tele_location, -1, 3)
    cf.move_and_click(coordinates.tab_inventory, -1, -1)
    bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(bank_location, -1, 4)
    global first_bank
    if first_bank:
        gui.write("9149", interval=0.27)
        first_bank = False
    cf.move_and_click(coords.inventory_slot[8], -1, -1)
    gui.press("esc")


def finish():
    gui.press("/")
    cf.logout()


def run():
    start()
    start_time = time.monotonic()
    while time.monotonic() < start_time + RUN_TIME * 60 * 60:
        fairy_ring_dkp()
        begin_fishing()
        bank_inventory()
